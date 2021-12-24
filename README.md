# Ejercicio: Consumir API GeckoCoin
1 - Definir los id_coins a consumir:

Agregar los coins dentro del archivo *coins.txt* separados por un salto de linea.

2 - Inicializar BD

> chmod a-x init_db.sh
> 
> bash init_db.sh

3 - Ejecutar app que consulta API

> chmod a-x init_app.sh
> 
> bash init_app.sh

o 

> docker ps #obtener id del container
> 
> docker exec -it #id del container# bash
> 
> EJ: python3 main.py #id_coin# --start-date 15-12-2021 --end-date 23-12-2021

* El log se encuentra ubicado en ./logs/app.log.
* Los archivos resultados del consumo del API se almacenan en formato .json dentro del directorio ./Files/#coin#/yyyy/mm/dd/.