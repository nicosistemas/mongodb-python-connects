FROM python:3-slim
RUN pip3 install pymongo
WORKDIR /app
COPY . .
CMD ["python", "mongo-query.py"]
