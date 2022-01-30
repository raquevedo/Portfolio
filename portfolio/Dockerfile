FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /web_service
WORKDIR /web_service
ADD ./portfolio/ ./web_service/
RUN pip install -r web_service/requirements.txt
EXPOSE 8000