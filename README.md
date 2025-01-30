# Docker Compose

Simple as ```docker compose up```

# Manual run 

## CPU only - https://hub.docker.com/r/ollama/ollama 
```docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama```
Run it in docker (optimisations available)

### https://ollama.com/library/deepseek-r1
```docker exec -it ollama ollama run deepseek-r1:7b```
Download the model you want

### UI to conect to it 
```docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main```