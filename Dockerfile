FROM python:3.10-slim

#  la salida de python se envíe # directamente al terminal sin ser primero almacenada en búfer.
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el contenido del directorio actual al contenedor en /code
COPY . /code/
EXPOSE 8000
# Ejecutar el comando para iniciar la aplicación.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]