# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta src para o container
COPY src/ ./src/

# Expõe a porta que o FastAPI vai usar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]