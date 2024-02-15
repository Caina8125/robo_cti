import os
import time
import shutil
import tkinter.messagebox
import pathlib


# global initial_count

def criarPastas():
    try:
        pathBot_CTI = r"C:\CTI"
        os.mkdir(pathBot_CTI)
        print("Pasta criada")
    except:
        tkinter.messagebox.showerror( 'Erro' , 'O programa ja está instalado na sua máquina' )


def baixarBot_MV():
    # global initial_count
    atualizaBot_MV = r"\\10.0.0.239\atualiza\CTI\Bot_MV"
    pathLocal = r"C:\CTI\Bot_MV"
    print("Fazendo instalação...")
    shutil.copytree(atualizaBot_MV, pathLocal)



def baixarCenso_Post():
    atualizaCenso_Post = r"\\10.0.0.239\atualiza\CTI\Censo_Post"
    pathLocal_ = r"C:\CTI\Censo_Post"
    shutil.copytree(atualizaCenso_Post, pathLocal_)
    print("Instalação executada...")



def Scripts():
    criarPastas()
    time.sleep(1)
    baixarBot_MV()
    time.sleep(1)
    baixarCenso_Post()


Scripts()