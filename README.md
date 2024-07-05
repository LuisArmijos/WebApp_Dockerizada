# WebApp Dockerizada que Consuma un Servicio SaaS (Imagga)

## Descripción

Este proyecto implementa una aplicación web utilizando Flask y Docker, que consume el servicio SaaS de Imagga para realizar análisis de imágenes.

## Requisitos

- **Docker**: Necesario para construir y ejecutar el contenedor Docker.
- **Python 3**: Opcionalmente, para ejecutar el servidor Flask localmente fuera del contenedor.
- **Flask**: Biblioteca de Python para crear aplicaciones web.
- **requests**: Biblioteca de Python para realizar solicitudes HTTP.

## Instalación de Dependencias

Para instalar las dependencias necesarias, se sigue los siguientes pasos:

1. **Instalar Docker:**
   - Instala Docker siguiendo las instrucciones para tu sistema operativo desde Docker Installation Guide: https://docs.docker.com/get-docker/

2. **Instalar Python y Flask:**
   - Instala Python 3 y Flask utilizando pip:
     ```bash
     pip install Flask requests
     ```

## Configuración y Ejecución

Sigue estos pasos para configurar y ejecutar la WebApp:

1. **Construir y Ejecutar el Contenedor Docker**
   - Construye la imagen Docker:
     ```bash
     docker build -t webapp-dockerizada .
     ```
   - Construye la imagen Docker:
     ```bash
     docker run -p 5000:5000 webapp-dockerizada
     ```

2. **Acceder a la Aplicación**
   - Abre tu navegador web y visita:
     ```bash
     http://localhost:5000
     ```

## Autor

Luis Armijos

