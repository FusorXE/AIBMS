# FusorX Energy – AI‑Driven Battery Management System (BMS) MVP

This monorepo contains a *minimal, production‑ready scaffold* for an AI‑driven Battery Management System (BMS) MVP.

**Microservices**

| Service        | Tech           | Purpose                          |
| -------------- | -------------- | -------------------------------- |
| ingestion      | FastAPI + InfluxDB client | Streams raw battery telemetry |
| api_gateway    | FastAPI        | AuthN/Z & public REST API        |
| ml_engine      | FastAPI + PyTorch | Hosts SoH & optimization models |

**Frontend**

A React + TypeScript dashboard providing real‑time monitoring and control.

**DevOps**

Docker Compose for local dev, Kubernetes manifests for prod, GitHub Actions CI/CD pipeline, plus Prometheus/Grafana metrics stubs.

> **Note**: Replace placeholder credentials, expand business logic, and harden security before going live.
