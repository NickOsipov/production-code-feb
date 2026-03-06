FROM python:3.12.8-slim-bookworm

ENV APP_HOME=/app

WORKDIR $APP_HOME

# uv 
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync
ENV PYTHONPATH="$APP_HOME"
ENV PATH="$APP_HOME/.venv/bin:$PATH"

COPY src src
COPY scripts scripts
COPY config config
COPY data data

ENV FLASK_APP=src/app.py
EXPOSE 5000
CMD ["bash", "scripts/entrypoint.sh"]