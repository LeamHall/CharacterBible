FROM python:3

WORKDIR /app
VOLUME /data

RUN python -m pip install --upgrade pip
COPY docker/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY docker/main.py .
COPY docker/app .

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]
