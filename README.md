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
### Instrucciones alternativas de uso
Se debera tener instalado python 3.8 y pip
se ejecuta el siguiente comando para instalar
* Adicionalmente se toma en cuenta que ya se tiene un servidor de base de datos MySQL instalado.
```
$ pip install .
```
#### Configuración variables para base datos
Se deben dar de alta las siguientes variables de entorno en el SO
* HOST_DB : este corresponde a el host ip:puerto
* USER_DB : este a el usuario
* PASS_DB : este a la contraseña
* DATABASE_DB : este a el esquema o base que se va a conectar

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