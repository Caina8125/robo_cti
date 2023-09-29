from datetime import datetime
import time
import os
import shutil

def movePath():
    # t = 0
    lista_relatorio = ['UTI A', 'UTI B1', 'UTI C']

    arqLocal = r"C:\Users\lucas.timoteo\Downloads\R_CENSO.csv"

    atual = datetime.now()
    date = atual.strftime("%d/%m/%Y, %H:%M:%S")

    data = os.path.getmtime(arqLocal)
    dataFormat = time.ctime(data)
    objLocal = time.strptime(dataFormat)
    trasnfLocal = time.strftime("%d-%m-%y %H:%M:%S", objLocal) 
    print(trasnfLocal)

    arqDest = r"\\10.0.0.239\informatica\Relatorios_cti\R_CENSO.csv"
    renomear = r"\\10.0.0.239\informatica\Relatorios_cti" + f"\\{lista_relatorio[1]} " + f"{date}" + ".csv"

    shutil.move(arqLocal,arqDest)

    time.sleep(2)

    os.replace(arqDest,renomear)

movePath()
    
