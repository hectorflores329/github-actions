import pandas as pd

def descargarDatos():
    df = pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/MPG/main/Prueba/Geo2_NI_provinces_.csv")
    df.to_excel("new_file.xlsx")

    return

def numerar():
    for i in range(10):
        print(i)


if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    descargarDatos()
    print('Se finalizó el proceso de descarga.')
    numerar()
    numerar()
    numerar()
    numerar()