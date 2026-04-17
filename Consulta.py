import pandas as pd
df = pd.read_csv("./RNPDNO-22-08-2023-limpio.csv", encoding="latin-1")
consulta = df[df["Sexo"] == "MUJER"].groupby("Entidad de desaparición").size()
print(consulta)
