import os
import time
import shutil
import pathlib
import threading
import customtkinter
import tkinter.messagebox
# import Install.Instalacao as instalacao

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x160")
janela.title("Bot_Cti")
janela.resizable(width=False, height=False)


texto = customtkinter.CTkLabel(janela,text="Deseja executar a instalação do Bot_CTI na sua máquina?",font=customtkinter.CTkFont(size=13, weight="bold"))
texto.pack(padx=10, pady=10)


button =  customtkinter.CTkButton(janela, height=30,width=100 ,text="Fazer instalação", command=lambda: threading.Thread(target=barra).start())
button.pack(padx=10, pady=10)

Percentage = customtkinter.CTkLabel(janela,text="0%",font=customtkinter.CTkFont(size=12, weight="bold"))

# Progress bar
progressBar = customtkinter.CTkProgressBar(janela,width=400)
progressBar.set(0)

textInstall = customtkinter.CTkLabel(janela,text='Instalando...',font=customtkinter.CTkFont(size=12, weight="bold"))

def barra():
    Percentage.pack()
    progressBar.pack()
    textInstall.pack()
    button.pack_forget()
    Scripts()

def dowloandEvent():
    qtdArquivos = count_BotMV
    per = str(int(qtdArquivos))
    Percentage.configure(text=per + '%')
    Percentage.update()

    progressBar.set(float(qtdArquivos) / 100)




#--------------------------------------------------------------------------------------------------------------------------------------------------

# Scripts de Instalação
def criarPastas():
    try:
        pathBot_CTI = r"C:\CTI"
        os.mkdir(pathBot_CTI)
        print("Pasta criada")
    except:
        tkinter.messagebox.showerror( 'Erro' , 'O programa ja está instalado na sua máquina' )


def baixarBot_MV():
    global count_BotMV
    atualizaBot_MV = r"\\10.0.0.239\atualiza\CTI\Bot_MV"
    pathLocal = r"C:\CTI\Bot_MV"


    lista_arquivos = os.listdir(atualizaBot_MV)
    count_BotMV = 0
    for arquivo in lista_arquivos:
        shutil.copytree(atualizaBot_MV,pathLocal)
        count_BotMV += 1
        dowloandEvent()



    # print("Fazendo instalação")
    # shutil.copytree(atualizaBot_MV, pathLocal)
    # print("Instalação executada")
    # count_BotMV = 0
    # for pathLocal in pathlib.Path(".").iterdir():
    #     # if pathLocal.is_file():
    #     count_BotMV += 1
        
    #     dowloandEvent()
    #     return count_BotMV



def baixarCenso_Post():
    global count_Censo
    atualizaCenso_Post = r"\\10.0.0.239\atualiza\CTI\Censo_Post"
    pathLocal_ = r"C:\CTI\Censo_Post"
    print("Fazendo instalação")
    shutil.copytree(atualizaCenso_Post, pathLocal_)
    print("Instalação executada")
    count_Censo = 0
    for pathLocal_ in pathlib.Path(".").iterdir():
        # if pathLocal_.is_file():
        count_Censo += 1
        dowloandEvent()
        return count_Censo



def Scripts():
    criarPastas()
    time.sleep(1)
    valArquivoBot = baixarBot_MV()
    time.sleep(1)
    valArquivoCenso = baixarCenso_Post()

    somaAquivos = valArquivoBot / valArquivoCenso * 100
    return somaAquivos

janela.mainloop()

