FROM python:3
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "./app.py" ]
