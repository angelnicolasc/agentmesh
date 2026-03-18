{{/*
Expand the name of the chart.
*/}}
{{- define "agentmesh-proxy.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
*/}}
{{- define "agentmesh-proxy.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Common labels
*/}}
{{- define "agentmesh-proxy.labels" -}}
helm.sh/chart: {{ include "agentmesh-proxy.name" . }}-{{ .Chart.Version | replace "+" "_" }}
{{ include "agentmesh-proxy.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "agentmesh-proxy.selectorLabels" -}}
app.kubernetes.io/name: {{ include "agentmesh-proxy.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
