FROM python:3.7.3-slim-stretch 

WORKDIR /
COPY checkpoint /checkpoint

RUN apt-get -y update && apt-get -y install gcc libatlas-base-dev gfortran nginx supervisor


RUN useradd --no-create-home nginx


COPY requirements.txt /requirements.txt
COPY app.py /app.py
COPY uwsgi.ini /uwsgi.ini
COPY wsgi.py /wsgi.py
COPY nginx.conf /etc/nginx/
COPY pokesite.conf /etc/nginx/conf.d/
COPY supervisord.conf /etc/supervisor/

RUN mkdir -p /var/log/uwsgi
RUN chown -R nginx:nginx /var/log/uwsgi


RUN pip3 --no-cache-dir install -r requirements.txt

RUN rm /etc/nginx/sites-enabled/default


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["usr/bin/supervisord"]
