FROM python:3
WORKDIR /skachki
COPY . .
RUN pip install flask
CMD ["python3", "app.py"]
