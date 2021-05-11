FROM python:3.7
WORKDIR /lds
ADD . /lds/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uwsgi", "--ini", "uwsgi.ini"]
