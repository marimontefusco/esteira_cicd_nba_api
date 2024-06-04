# Imagem base do Python 
FROM python:3.9

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia os arquivos para o diretório de trabalho
COPY . .

# Porta que a aplicação vai rodar
EXPOSE 5003

# Comando para rodar a aplicação
CMD ["python", "app/app.py"]
