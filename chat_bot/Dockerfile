FROM python:3.12-slim-bullseye

WORKDIR /app
RUN python3 -m venv /opt/venv

COPY requirements.txt ./
RUN /opt/venv/bin/pip install -U -r requirements.txt

COPY rag.py ./

COPY chainlit.md ./
COPY .chainlit ./

ENV HOST=0.0.0.0
ENV LISTEN_PORT 8000
EXPOSE 8000

CMD ["/opt/venv/bin/chainlit", "run", "rag.py"]