python -m http.server 9000

# chat bot
docker build -t chatbot . 
docker run -p 8000:8000 chatbot