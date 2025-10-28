# Usa uma imagem base leve com Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos locais para dentro do container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Streamlit usa
EXPOSE 8501

# Comando para iniciar o Streamlit quando o container for executado
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
