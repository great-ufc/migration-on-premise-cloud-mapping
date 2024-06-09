FROM ubuntu:22.04 AS builder

RUN apt-get update && apt-get install -y p7zip-full p7zip-rar \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY chroma.rar /build/

RUN 7z x chroma.rar -ochroma \
    && mv chroma/ /build/unpack \
    && rm chroma.rar

FROM python:3.11-slim AS runner

WORKDIR /app

COPY --from=builder /build/unpack /backend/chroma

RUN ls -la /backend/chroma

COPY ./backend /backend
COPY ./data /data

WORKDIR /backend

RUN pip3 install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
