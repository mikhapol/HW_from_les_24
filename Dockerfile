#FROM python:3.11
#
#WORKDIR /app
#
##COPY ./pyproject.toml /code/pyproject.toml
#COPY pyproject.toml poetry.lock ./
#RUN poetry export -f requirements.txt --output requirements.txt
#
#RUN pip3 install poetry
#
#RUN poetry install --no-root
#
#COPY . .

#CMD python manage.py runserver

FROM python:3.10-slim-buster AS poetry
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt

FROM python:3.10-slim-buster
WORKDIR /app
COPY --from=poetry /app/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
