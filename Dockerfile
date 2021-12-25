FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app/acme_platform
COPY requirements.txt /app/acme_platform/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app/acme_platform
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000