#!/bin/sh

ollama serve &

# Aguarda até que o serviço ollama esteja pronto
until curl -s http://localhost:11434/; do
    echo "Waiting for the Ollama service to be ready..."
    sleep 5
done

# Executa os comandos necessários
ollama pull nomic-embed-text
ollama pull llama2

tail -f /dev/null
