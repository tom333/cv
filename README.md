python -m http.server 9000

# chat bot
docker buildx build -t chatbot . 

docker run -p 8000:8000 --net host chatbot


kubectl port-forward svc/cv-qdrant 6333:6333 -n cv
