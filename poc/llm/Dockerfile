FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y curl

COPY llm_setup.sh ./llm_setup.sh

RUN chmod +x ./llm_setup.sh

ENTRYPOINT ["./llm_setup.sh"]
