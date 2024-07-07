## Tutorial

### Elements

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/poc/media/guide%20screen%201.png" title="Guide 1" height="500" width="850" />
</p>

### Chatting

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/poc/media/guide%20screen%203.png" title="Guide 1" height="500" width="850" />
</p>

### Usage Example Video

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/poc/media/Make-a-question.gif" title="Guide 1" height="500" width="850" />
</p>

### Api docs usage example vide

<p align="center">
  <img src="https://raw.githubusercontent.com/great-ufc/migration-on-premise-cloud-mapping/main/poc/media/API-Make-a-question.gif" title="Guide 1" height="500" width="850" />
</p>

## Get Started to use

### Prepare enviroment variables

If you're on linux, you'll need to create an .env in the root of the backend folder. 
Contents of the .env:
```
OLLAMA_BASE_URL=http://localhost:8000
```

### Running server

You'll need ``docker`` started to run the following command:
```
docker compose up -d
```

* Obs.: This command needs to be executed in the poc folder
  
#### Using GPU (optional)

If you have a GPU and want to use it, then run the file ``gpu_setup.sh``

And You'll need ``docker`` started to run the following command :
```
docker compose -f docker-compose-gpu.yml up
```
### Prepare LLM models (⚠️ important for users with poor internet)
> If your internet isn't very fast, then you'll need to download the templates separately. 
> First, comment out line 9 ``ENTRYPOINT [“./llm_setup.sh”]`` from the llm/Dockerfile. 
> Then run inside the containers :

You'll nedd run the folliwing commands in llm container:
```
ollama pull nomic-embed-text
ollama pull llama2
```
## Local Running

You can also run the system separately by following the instructions described [here](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/frontend) for the front-end and [here](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/backend) for the back-end.

## How to access

### Web App

You can view the web interface at http://localhost:3000/

### API

You can access the API documentation at the following link: http://localhost:8000/

### CLI

You can also access the CLI and just run the questions from the command line, 
see how to do this in the section [cli-comands](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/backend#cli-command).

## Possible problems

1. Communication error with the server:
> This error is probably due to a misconfiguration of the environment variables. Therefore, check the .env file that should be inside the backend folder. It should count OLLAMA_BASE_URL as http://localhost:8000 if you use linux or mac, otherwise the value should be http://llm:8000.

## Stacks and others

To check the technologies used, check the specific documentation for each point:
- [front-end](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/frontend)
- [back-end](https://github.com/great-ufc/migration-on-premise-cloud-mapping/tree/main/poc/backend)
