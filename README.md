# Run Locally 
Run a Deepseek AI locally using docker. Including a chat interface to interact with it. 

## Docker Compose
Simple as ```docker compose up```

## Manual components if you don't want to use the Docker Compose

#### CPU only Deepseek AI (amd and nvidia available) 
https://hub.docker.com/r/ollama/ollama 
```docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama```

#### Download the Model
https://ollama.com/library/deepseek-1  
```docker exec -it ollama ollama run deepseek-r1:7b```

### Chat UI to conect to it 
```docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main```
