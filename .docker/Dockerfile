FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    gcc python3-gevent file make \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry"

WORKDIR /app
COPY . .

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi


COPY .docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 8000
ENTRYPOINT [ "/entrypoint.sh" ]
CMD ["gunicorn", "--bind", ":8000", "--graceful-timeout=900", "--timeout=900", "--workers", "3", "--error-logfile", "-", "--access-logfile", "-", "app.wsgi:application"]