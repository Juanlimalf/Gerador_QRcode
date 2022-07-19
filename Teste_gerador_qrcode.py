import pandas as pd
import pyqrcode as pqr
import numpy as np
import os

dados = pd.read_excel(r'C:\Users\juan.costa\Desktop\Python_Nagumo\usuarios.xlsx')

for lojas in set(dados.loja):
    try:
        os.makedirs(str(lojas))
    except FileExistsError as erro:
        print(f"Pasta {lojas} existente.")

for conf in set(dados.conferente):
    print("\n",conf)
    cod = pqr.create(conf)
    cod.png(conf+'.png', scale=5)
    print(cod.terminal(quiet_zone=1,))