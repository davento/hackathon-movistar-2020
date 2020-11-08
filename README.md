# hackathon-movistar-2020
## Integrantes
**Grupo rɐunaɹ**

* Aguilar, Anthony
* Castro, Eduardo
* Flores, Christopher
* Lozada, Juan Carlos
* Vento, Daniela Abril

## Objetivo
Automatizar el control de evidencias para Movistar

## Funciones de Control

Identificar conformidades en
* Formulario de Atención
* Evidencias fotográficas

## Dependencias para el web-scrapping
Descargar la versión adecuada para tu versión de Chrome u otro buscador
> https://sites.google.com/a/chromium.org/chromedriver/downloads

Luego extraerlo en esta misma carpeta

Corre el comando
> source .henv/bin/activate

para entrar al virtual enviroment

y luego
> pip install -r requirements.txt

Al final prueba con
> python scraping.py

y ejecuta
> deactivate

para salir del virtual env

## Dependencias para la detección de imágenes

Instalar Ximilar-client
> pip install ximilar-client