FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# instala uv
RUN pip install --no-cache-dir uv

# copia arquivos de dependência (cache eficiente)
COPY pyproject.toml uv.lock ./

# cria venv
RUN uv venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# instala dependências conforme lock
RUN uv sync --frozen

# copia o restante do código
COPY . .

EXPOSE 8000

# comando padrão (produção)
CMD ["gunicorn", "-w", "2", "-b", "localhost:8000", "app:app"]
