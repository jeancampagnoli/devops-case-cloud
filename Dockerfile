# 1. Imagem base com Python
FROM python:3.9-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o resto do código da aplicação
COPY . .

# 6. Expõe a porta que a aplicação vai usar
EXPOSE 5000

# 7. Comando para iniciar a aplicação quando o container rodar
CMD ["python", "app.py"]