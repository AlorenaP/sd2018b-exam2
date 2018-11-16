FROM python:3.6-slim

WORKDIR /aplicacion

COPY . /aplicacion

RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME World

# Run aplicacion.py
CMD ["python", "aplicacion.py"]
