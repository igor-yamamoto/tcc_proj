FROM python:3.6.1-alpine
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