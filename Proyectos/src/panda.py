import pandas as pd

fichero_csv = "prueba.csv"
df = pd.read_csv(fichero_csv)

if __name__ == "__main__":
    print(df)
