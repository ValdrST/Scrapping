# Scrapper-ejemplo-python
## Instrucciones de uso 

Hay que tener docker y docker-compose instalado

Se ejecuta el siguiente comando la primera vez que se utiliza
```
$ docker-compose build
```
Se ejecuta el siguiente comando cada que se quiera levantar
```
$ docker-compose up
```

### Configuración de variables para base de datos

dentro de [docker-compose.yml](docker-compose.yml)
modificar las variables de las secciones **environment** para cambiar el usuario y la contraseña de la base de datos mysql que se va a levantar.

### Cambio de puerto de base de datos mysql 

La sección ports se encuentra configurada por defecto en el puerto 3306 si se desea tener otro se se cambia '3306:3306' por '{puerto}:3306'.

## Vista de dashboard
El dashboard se debe poder visualizar asi, los datos se traen de la base de datos

![dashboard](Dashboard_powerBI.png)

El archivo del dashboard es:
* [archivo dashboard](modelo_bd.pbix)
* [informe pdf](modelo_bd.pdf)