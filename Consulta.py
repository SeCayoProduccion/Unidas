import sqlite3
import pandas as pd
conn = sqlite3.connect("desaparecidos.db")

query = """
SELECT entidad_desaparicion, COUNT(*) as total
FROM casos
WHERE fecha_desaparicion IS NOT NULL
AND sexo = 'MUJER'
GROUP BY entidad_desaparicion
"""

df_combo = pd.read_sql(query, conn)
print(df_combo)


conn.close()
