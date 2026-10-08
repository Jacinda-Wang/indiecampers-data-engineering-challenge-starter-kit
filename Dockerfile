FROM python:3.12.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY pyproject.toml README.md constraints.txt ./
COPY src ./src
COPY tests ./tests
COPY data ./data
COPY starter-kit ./starter-kit

RUN python -m pip install --no-cache-dir -c constraints.txt -e ".[dev]"

CMD ["python", "-m", "booking_pipeline", "--help"]
