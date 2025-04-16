# Dockerfile

# Etapa 1: imagem base
FROM python:3.13-alpine

# Etapa 2: variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Etapa 3: diretório de trabalho
WORKDIR /app

# Etapa 4: instalar dependências
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Etapa 5: copiar arquivos do projeto
COPY . .

# Etapa 6: comando para rodar Gunicorn
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]

# Etapa 7: # Coleta os arquivos estáticos
RUN python manage.py collectstatic --noinput