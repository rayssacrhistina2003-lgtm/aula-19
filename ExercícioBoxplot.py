
import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\rayssa.christina\Downloads\funcionarios.csv")


print(df)

lucro = df["lucro"].to_numpy()

print(lucro)

q1 = np.percentile(lucro, 25)
q2 = np.percentile(lucro, 50)
q3 = np.percentile(lucro, 75)

print("Primeiro Quartil\n")
print(q1)
print("\nMediana\n")
print(q2)
print("\nTerceiro Quartil\n")
print(q3)

i = q3 - q1
Limite_inferior = q1 - 1.5 * i

Limite_max = q3 + 1.5 * i

outliers = lucro[(lucro < Limite_inferior) | (lucro > Limite_max)]

dentro = lucro[(lucro >= Limite_inferior) & (lucro <= Limite_max)]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print("Limite inferior: \n")
print(Limite_inferior)
print("\nLimite Superior: \n")
print(Limite_max)
print("\nOutliers: \n")
print(outliers)
print("\nBigode inferior: \n")
print(bigode_inf)
print("\nbigode superior: \n")
print(bigode_sup)
