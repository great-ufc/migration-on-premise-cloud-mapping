## Get Started

### Create virutal env
```python -m venv venv```

### Activate virutal env
```source venv/Scripts/activate```

### Install libs
```pip install -r ./backend/requirements.txt```

### Configure local envs
Following .env.example setup your configs, create file .env:
```
OLLAMA_BASE_URL=http://localhost:8000
```

* Obs.: Running in windows the host need be "llm"

## Running llm

### First step up container
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### Second step prepare models in container
```
ollama pull nomic-embed-text
ollama pull llama2
```
* Obs.: This step will create the folder ollama with the llm models

### Prepaper embedding database

You'll extract chroma.rar to backend/ folder

## CLI commands

### Populate database
```python ./backend/populate_chomadb.py```

### Make a question
```python ./backend/query_data.py "make question here"```

## Execute API

### Local
```python ./backend/src\app.py```

### Like a server
```python ./backend/server.py```

## Running in Container

### Requirements
1. Llama container running
2. Navigate to folder "poc"

### Build image
```docker build -t 'api' -f backend/Dockerfile .```

### Run image
```docker run -d -p 8000:8000 --name 'api' api```

## Stacks

- Python
- FastAPI
- Ollama: server for llama2
- ChromaDB: vectorized db
