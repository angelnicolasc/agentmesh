"""`agentmesh scan` — Scan a project for governance/compliance gaps.

Offline-first: all analysis runs locally using AST. No network calls
unless --upload is passed. No signup or API key required for basic use.
"""

from __future__ import annotations

import sys

import click


@click.command()
@click.argument("directory", default=".", type=click.Path(exists=True))
@click.option(
    "--format", "output_format",
    type=click.Choice(["terminal", "json", "sarif"]),
    default="terminal",
    help="Output format (default: terminal with Rich)",
)
@click.option(
    "--upload",
    is_flag=True,
    help="Upload results to AgentMesh for shareable URL and badge",
)
@click.option(
    "--api-key",
    envvar="AGENTMESH_API_KEY",
    default=None,
    help="API key for authenticated upload (env: AGENTMESH_API_KEY)",
)
@click.option(
    "--endpoint",
    default="https://api.useagentmesh.com",
    envvar="AGENTMESH_ENDPOINT",
    help="Backend endpoint for --upload",
)
@click.option(
    "--framework",
    default=None,
    help="Comma-separated frameworks to detect (e.g. crewai,langgraph)",
)
@click.option(
    "--threshold",
    type=int,
    default=None,
    help="Minimum governance score. Exit 1 if score < threshold.",
)
@click.option(
    "--fail-on",
    type=click.Choice(["critical", "high", "medium", "low"], case_sensitive=False),
    default=None,
    help="Exit 1 if any finding at or above this severity.",
)
@click.option(
    "--diff",
    default=None,
    help="Git ref to diff against (e.g. HEAD~1, main). Only scan changed files.",
)
@click.option(
    "--include-tests",
    is_flag=True,
    help="Include tests/, test/, and fixtures/ directories in the scan.",
)
@click.option(
    "--details",
    is_flag=True,
    help="Show full findings with code snippets and fix suggestions.",
)
@click.option(
    "--project",
    default=None,
    help="Project name for upload and badge URL. Defaults to directory name.",
)
def scan(
    directory: str,
    output_format: str,
    upload: bool,
    api_key: str | None,
    endpoint: str,
    framework: str | None,
    threshold: int | None,
    fail_on: str | None,
    diff: str | None,
    include_tests: bool,
    details: bool,
    project: str | None,
) -> None:
    """Scan your AI agent project for governance and compliance gaps.

    Analyzes the project at DIRECTORY (defaults to current directory)
    and generates a governance score, Agent BOM, and actionable findings.

    All analysis runs offline — no network calls, no signup required.
    """
    # Lazy imports keep CLI startup fast
    from agentmesh.cli.scanner import run_scan

    # Parse framework filter
    framework_filter = None
    if framework:
        framework_filter = [f.strip() for f in framework.split(",") if f.strip()]

    # ---- Run offline scan ----
    result = run_scan(directory, framework_filter=framework_filter, include_tests=include_tests)

    # ---- Filter by --diff if requested ----
    if diff:
        from agentmesh.cli.diff_filter import get_changed_files, filter_findings_by_files

        changed = get_changed_files(directory, diff)
        if changed is not None:
            result.findings = filter_findings_by_files(result.findings, changed)
            # Recalculate score after filtering
            if result.findings or result.score is not None:
                from agentmesh.cli.scoring import calculate_score, score_to_grade
                result.score = calculate_score(result.findings)
                result.grade = score_to_grade(result.score)

    # ---- Output based on format ----
    if output_format == "json":
        from agentmesh.cli.formats.json_fmt import format_json
        click.echo(format_json(result))

    elif output_format == "sarif":
        from agentmesh.cli.formats.sarif import format_sarif
        click.echo(format_sarif(result))

    else:
        # Terminal output with Rich
        from agentmesh.cli.report import render_report
        render_report(
            bom=result.bom,
            findings=result.findings,
            score=result.score,
            grade=result.grade,
            metadata=result.metadata,
            scan_duration_ms=result.scan_duration_ms,
            details=details,
        )

    # ---- Upload if requested ----
    if upload:
        from agentmesh.cli.upload import upload_results
        import httpx

        # Resolve project name: --project flag > directory name
        project_name = project or result.metadata.root.name
        base_endpoint = endpoint.rstrip("/")

        click.echo()
        if api_key:
            click.echo(click.style("  [upload] ", fg="green") + "Uploading results (authenticated)...")
        else:
            click.echo(click.style("  [upload] ", fg="green") + "Uploading results (anonymous, expires in 7 days)...")

        try:
            resp = upload_results(
                result, api_key=api_key, endpoint=endpoint, project_name=project_name,
            )
            scan_id = resp.get("scan_id", "?")
            scan_url = resp.get("url", "")
            click.echo(click.style("  [upload] ", fg="green") + f"Scan ID: {scan_id}")
            if scan_url:
                click.echo(
                    click.style("  [upload] ", fg="green")
                    + "Report: "
                    + click.style(scan_url, fg="cyan", underline=True)
                )

            # Badge URL
            badge_url = f"{base_endpoint}/api/v1/scans/badge/{project_name}"
            click.echo(
                click.style("  [badge]  ", fg="green")
                + "Badge: "
                + click.style(badge_url, fg="cyan", underline=True)
            )
            click.echo()
            click.echo("  Add to your README:")
            click.echo(
                click.style(
                    f"  ![AgentMesh]({badge_url})",
                    fg="white",
                )
            )
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                click.secho("  [error]  Rate limit exceeded. Try again later or use an API key.", fg="red")
            elif e.response.status_code == 401:
                click.secho("  [error]  Invalid API key.", fg="red")
            else:
                click.secho(f"  [error]  Upload failed: HTTP {e.response.status_code}", fg="red")
        except httpx.ConnectError:
            click.secho("  [error]  Could not connect to AgentMesh backend.", fg="red")
            click.echo("           Try: --endpoint http://localhost:8000")
        except httpx.ReadTimeout:
            click.secho("  [error]  Upload timed out.", fg="red")

    # ---- Exit code based on findings ----
    _SEVERITY_ORDER = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}

    if fail_on:
        min_level = _SEVERITY_ORDER.get(fail_on.upper(), 0)
        for f in result.findings:
            if _SEVERITY_ORDER.get(f.severity, 0) >= min_level:
                sys.exit(1)
    elif threshold is not None:
        if result.score is not None and result.score < threshold:
            sys.exit(1)
    else:
        # Default: exit 1 on CRITICAL (backward compatible)
        if any(f.severity == "CRITICAL" for f in result.findings):
            sys.exit(1)
