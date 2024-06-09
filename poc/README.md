# Etapa de construção
FROM python:3.11-slim AS builder

# Instalar 7zip para extrair o arquivo RAR
RUN apt-get update && apt-get install -y p7zip-full p7zip-rar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY chroma.rar /build/

# Extrair o conteúdo do arquivo chroma.rar
RUN 7z x chroma.rar -ochroma \
    && mv chroma/chroma /build/chroma \
    && rm chroma.rar

# Etapa final
FROM python:3.11-slim AS runner

WORKDIR /app

# Copiar os arquivos necessários da etapa de construção
COPY --from=builder /build/chroma /backend/chroma

COPY ./backend /backend
COPY ./data /data

WORKDIR /backend

RUN pip3 install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
