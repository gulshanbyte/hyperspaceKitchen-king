FROM python:3.12

RUN apt update && apt upgrade -y && apt install python3-poetry -y
WORKDIR /app
COPY . /app

RUN poetry install
CMD ["poetry", "run", "gunicorn", "main:app"]
