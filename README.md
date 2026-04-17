# UNIDAS


Unidas busca crear difusión y memoria colectiva sobre temas de violencia física y sexual hacia mujeres en México.

Buscamos implementar un mapa interactivo donde se pueda observar el índice de estos crímenes por estado.
Además, consideramos que sus casos no deben ser tratados solo como datos y estadísticas, queremos que sus historias
sean contadas y recordadas sin caer en la revictimización. 
Por último, identificaremos los factores de riesgo en diferentes ámbitos.

-------------------------------------------------------------------------------------------------------------------------------
# UNIDAS


Unidas Unidas aims to raise awareness and collective memory on issues of physical and sexual violence against women in Mexico. 


We seek to implement an interactive map that displays the rate of these crimes by state. Additionally, we believe they should not be treated merely as data and statistics; we want their stories to be told and not forgotten, without revictimizing them. Finally, we will attempt to identify the risk factors in different areas.

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
