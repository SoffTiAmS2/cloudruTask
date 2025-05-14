FROM python:3.11-slim

WORKDIR /echo_server

RUN pip install Flask

COPY echo_server.py .

ENV AUTHOR="Default Author"

EXPOSE 8000

CMD ["python", "echo_server.py"]