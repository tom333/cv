FROM python:3.12-slim-bullseye

WORKDIR /app


COPY requirements.txt ./
RUN pip install -U -r requirements.txt

COPY rag.py ./

COPY chainlit.md ./

ADD .chainlit .chainlit

ENV CHAINLIT_HOST=0.0.0.0   
ENV CHAINLIT_PORT=8000
EXPOSE 8000

CMD ["chainlit", "run", "rag.py"]