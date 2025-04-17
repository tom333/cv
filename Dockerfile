FROM python:3.12-slim


WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD uv.lock .
ADD pyproject.toml . 

ADD src .
EXPOSE 8501
RUN uv sync --frozen

CMD ["uv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
