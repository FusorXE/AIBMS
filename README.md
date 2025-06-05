# FusorX Energy – AI‑Driven Battery Management System (BMS) MVP

This monorepo contains a *minimal, production‑ready scaffold* for an AI‑driven Battery Management System (BMS) MVP.

**Microservices**

| Service        | Tech           | Purpose                          |
| -------------- | -------------- | -------------------------------- |
| ingestion      | FastAPI + InfluxDB client | Streams raw battery telemetry |
| mqtt_bridge    | FastAPI + MQTT client | Bridges MQTT telemetry to REST |
| api_gateway    | FastAPI        | AuthN/Z & public REST API        |
| ml_engine      | FastAPI + PyTorch | Hosts SoH & optimization models |

**Frontend**

A React + TypeScript dashboard providing real‑time monitoring and control.

**DevOps**

Docker Compose for local dev, Kubernetes manifests for prod, GitHub Actions CI/CD pipeline, plus Prometheus/Grafana metrics stubs.

## Telemetry Emulator

`scripts/telemetry_emulator.py` publishes fake cell data over MQTT so integrators can run the stack locally via `docker-compose up`.

> **Note**: Replace placeholder credentials, expand business logic, and harden security before going live.
