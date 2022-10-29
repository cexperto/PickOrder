FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

ENV DJANGO_SETTINGS_MODULE=pickorder.settings

RUN mkdir /pick_order

RUN python3 -m pip install --upgrade pip

WORKDIR /pick_order

COPY ./requirements.txt .

RUN python3 -m pip install --root-user-action=ignore --no-cache-dir --upgrade -r requirements.txt

RUN python3 manage.py makemigrations order

RUN python3 manage.py migrate

COPY . .

RUN python3 

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]