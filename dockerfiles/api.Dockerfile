# Usar a imagem oficial do Ubuntu como base
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho para a aplicação
WORKDIR /app

# Copiar o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt /app/

# Instalar as dependências do projeto (pip requirements)
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY track_api/ /app/

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expôr a porta da aplicação (por exemplo, a porta padrão do Django)
EXPOSE 8000

# Comando para rodar as migrações e iniciar o servidor
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
