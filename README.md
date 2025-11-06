# 📊 Dashboard de Doações - ONG

Este projeto foi desenvolvido com o objetivo de analisar e visualizar os dados de doações realizadas para uma ONG, utilizando uma arquitetura baseada em **microserviços** e **conteinerização com Docker**.  
A solução integra **Banco de Dados**, **API** e **Dashboard** de forma organizada e escalável.

---

## 🎯 Objetivos do Projeto

- Aplicar conceitos de **DevOps** e **Docker** na prática.
- Demonstrar comunicação entre serviços utilizando **Docker Compose**.
- Disponibilizar uma interface visual interativa para análise de doações.
- Oferecer uma base clara para expansão futura com dados reais da ONG.

---

## 🧱 Arquitetura da Aplicação

DASHBOARD-ONG/
│
├── docker-compose.yml # Define e orquestra todos os serviços
├── init.sql # Script de criação/população do banco
│
├── api/ # Serviço da API
│ ├── Dockerfile
│ ├── app.py # Fornece os dados em formato JSON
│ └── requirements.txt
│
└── dashboard/ # Serviço do Dashboard (Streamlit)
├── Dockerfile
├── app.py # Interface de visualização dos dados
└── requirements.txt

yaml
Copiar código

---

## 🔗 Fluxo de Comunicação entre Serviços

| Serviço | Função | Porta | Conecta-se a |
|--------|--------|-------|--------------|
| `db` | Banco PostgreSQL | 5432 | API |
| `api` | Fornece dados em JSON | 5000 | Dashboard |
| `dashboard` | Interface visual (Streamlit) | 8501 | API |

A comunicação interna acontece via rede Docker, utilizando:

http://api:5000/doacoes

yaml
Copiar código

---

## 🐳 Executando a Aplicação

### 1. Acesse a pasta raiz do projeto:
```bash
cd DASHBOARD-ONG
2. Suba os serviços:
bash
Copiar código
docker compose up --build
3. Acesse os serviços no navegador:
Serviço	URL
Dashboard	http://localhost:8501
API (endpoint JSON)	http://localhost:5000/doacoes

🧪 Banco de Dados
O banco PostgreSQL é iniciado automaticamente com os dados definidos em:

csharp
Copiar código
init.sql
Você pode editar este arquivo para adicionar informações reais da ONG.

📊 Dashboard
O Dashboard exibe:

Gráficos de distribuição das doações por mês

Resumo geral em tabela

Total arrecadado no período

A interface foi construída utilizando:

Streamlit (interface)

Plotly (gráficos)

Pandas (tratamento de dados)

Requests (integração com API)

📦 Tecnologias Utilizadas
Tecnologia	Função
Python	Linguagem principal
Streamlit	Dashboard interativo
Flask ou FastAPI	API REST (dependendo da implementação usada)
PostgreSQL	Banco de dados
Docker e Docker Compose	Conteinerização e orquestração
Plotly	Visualização gráfica
Pandas	Manipulação de dados
