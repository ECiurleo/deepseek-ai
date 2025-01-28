# deepseek-ai
A small POC of a containerised DeepSeek chat written in Python

## docker build -t deepseek-api-container .

## API is set as an Environment Variable so it can easily be stored as a secret (and never accidentally commited into code!)
docker run -e DEEPSEEK_API_KEY="your-deepseek-api-key" deepseek-api-container