FROM python:3.8-alpine

WORKDIR /usr/src/app

COPY requirements/install.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "figures", "--verbose", "serve", "--port", "8080"]

EXPOSE 8080
