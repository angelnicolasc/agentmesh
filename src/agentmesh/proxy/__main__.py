"""Allow running the proxy with: python -m agentmesh.proxy"""

import os
from agentmesh.proxy.proxy_server import run_server

if __name__ == "__main__":
    port = int(os.environ.get("AGENTMESH_PROXY_PORT", "8990"))
    run_server(port=port)
