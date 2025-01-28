# deepseek-ai
A small POC of a containerised DeepSeek chat written in Python

---

### Container Build Instructions
To build the Docker container, run the following command:

```bash
docker build -t deepseek-api-container .
```

### API is set as an Environment Variable so it can easily be stored as a secret (and never accidentally commited into code!)
```bash
docker run -e DEEPSEEK_API_KEY="your-deepseek-api-key" deepseek-api-container
```
