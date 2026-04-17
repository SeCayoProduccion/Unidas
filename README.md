# UNIDAS

Unidas busca crear difusión y memoria colectiva acerca de desapariciones en México.

Buscamos implementar un servicio que permita identificar el riesgo de ser víctima según tu edad, localización y género. Además, se mostrará la información con un mapa interactivo

La información fue recopilada de https://volveradesaparecer.datacivica.org/datos-abiertos
-------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------

## Consulta

Para obtener el número de desapariciones de mujeres por entidad federativa (excluyendo registros sin fecha de desaparición), utilizamos una consulta SQL sobre la base de datos `desaparecidos.db`. El script en Python es el siguiente:

```python
import pandas as pd

df = pd.read_csv("./RNPDNO-22-08-2023-limpio.csv", encoding="latin-1")

consulta = df[df["Sexo"] == "MUJER"].groupby("Entidad de desaparición").size()

print(consulta)

```
en el que se obtiene 

``` entidad_desaparicion  total
0        AGUASCALIENTES     28
1       BAJA CALIFORNIA    137
2   BAJA CALIFORNIA SUR     20
3              CAMPECHE      3
4               CHIAPAS     64
5             CHIHUAHUA    118
6      CIUDAD DE MEXICO    375
7              COAHUILA    214
8                COLIMA     64
9               DURANGO     23
10     ESTADO DE MEXICO   1254
11           GUANAJUATO     76
12             GUERRERO    199
13              HIDALGO     50
14              JALISCO    178
15           MICHOACAN     280
16              MORELOS    129
17              NAYARIT     19
18           NUEVO LEON    381
19               OAXACA     21
20               PUEBLA     31
21           QUERETARO      23
22         QUINTANA ROO     56
23      SAN LUIS POTOSI     33
24         SE DESCONOCE     23
25              SINALOA    106
26               SONORA    242
27              TABASCO     21
28           TAMAULIPAS    985
29             TLAXCALA      5
30            VERACRUZ     334
31              YUCATAN      5
32            ZACATECAS    145

```
-------------------------------------------------------------------------------------------------------------------------------

## Integrantes
- Lider : Indra Cortes
- Testing : Cristian Lopez
- Ingeniero de Tecnologia : Jorge Bolaños
