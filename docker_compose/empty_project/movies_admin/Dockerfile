FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'

WORKDIR /opt/app

COPY requirements.txt /opt/app/requirements.txt
RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . /opt/app/

RUN chmod +x /opt/app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/app/entrypoint.sh"]