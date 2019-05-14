FROM python:3.6

RUN pip install pipenv

WORKDIR /app

COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

RUN pipenv install

COPY . .

CMD ["pipenv", "run", "python", "/app/main.py"]

ENTRYPOINT [ "pipenv", "run", "python", "/app/main.py" ]