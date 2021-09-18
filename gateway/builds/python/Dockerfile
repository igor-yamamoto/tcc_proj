FROM python:3.6.1-alpine
RUN apk update 
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./code/requirements.txt ./
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY ./code/scripts/* ./
# CMD ["mqtt_consumer.py"]
# ENTRYPOINT ["python3"]
CMD tail -f /dev/null