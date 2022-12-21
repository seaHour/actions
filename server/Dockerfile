FROM python:3.9.16-buster

WORKDIR /tmp

RUN apt-get update && apt-get install -y \
    procps \
    supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./conf/supervisord.conf /etc/supervisor/conf.d/

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile Pipfile.lock /tmp/
RUN pipenv sync --system
RUN rm Pipfile Pipfile.lock

COPY /app /app

WORKDIR /app

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
