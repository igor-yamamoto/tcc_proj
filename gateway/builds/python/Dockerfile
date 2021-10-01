FROM amd64/python:3.9.7-alpine3.14
RUN apk update 
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY ./code/requirements.txt ./
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY ./code/scripts/* ./
COPY ./.env ./.env
# ENTRYPOINT ["python3"]
CMD ["python","/usr/src/app/mqtt_consumer.py"]

# CMD tail -f /dev/null