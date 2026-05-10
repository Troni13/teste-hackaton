# 1. Usa uma imagem oficial e enxuta do Python
FROM python:3.10-slim

# 2. Define a pasta raiz dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências ANTES do código
# Isso é um truque de infra: se o código mudar, o Docker não precisa baixar as dependências tudo de novo
COPY requirements.txt .

# 4. Instala as dependências sem guardar cache inútil
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o restante do seu projeto para dentro do container
COPY . .

# 6. Expõe a porta 5000 (a mesma do Gunicorn/Flask)
EXPOSE 5000

# 7. O comando que inicia o servidor quando o container ligar
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]