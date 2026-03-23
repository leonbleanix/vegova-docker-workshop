FROM python:3.13-slim

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "dev"]
