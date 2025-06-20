# GPT DevOps API

## 🚀 Como rodar localmente:

```bash
docker-compose up --build
```

Acesse em: http://localhost:8000

## 🚀 Como fazer deploy no Google Cloud Run:

- Configure sua conta de serviço no GitHub Secrets como `GCP_SA_KEY`.
- Faça push no branch `main`.
- O deploy será feito automaticamente no Google Cloud Run.

## 🐳 Build manual Docker:

```bash
docker build -t gpt-devops-api .
docker run -p 8000:8000 gpt-devops-api
```

Acesse: http://localhost:8000

## 🔗 Endpoints:

- `/` → Status da API
- `/execute` → Executa comandos no servidor
- `/health` → Healthcheck

