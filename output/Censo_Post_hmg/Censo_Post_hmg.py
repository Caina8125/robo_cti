import os
import time
import shutil
import asyncio
import menssage.Pidgin as Pidgin
# import menssage.Telegram as telegram
import APIs.Homologacao.Api_Censo_hmg as api_censo


def post_arquivos_Norte_hmg():
    count          = 0
    pasta          = r"C:\Arquivos_CTI\Homologacao\Norte"
    erros_norte    = r"C:\Arquivos_CTI\Homologacao\Erros\Norte"
    nomes_arquivos = os.listdir(pasta)
    lista_ordenada = ordenarArquivos(nomes_arquivos,pasta)
    
    try:
        api_censo.auth_hmg()
    except Exception as e:
        Pidgin.main(f"Olá, ocorreu um erro no robô ao buscar o Token no Auth. {e.__class__.__name__}: {e}")
        # asyncio.run(telegram.Dev(f"Olá, ocorreu um erro ao buscar o Token no Auth.  {e.__class__.__name__}: {e}"))

    for arquivo in lista_ordenada:
        nome_csv = os.path.join(pasta, arquivo[1])
        try:
            api_censo.post_CtiNorte_hmg(nome_csv,arquivo[1])
        except Exception as e:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_NORTE com o arquivo: {arquivo[1]} . O mesmo está separado para avaliação na pasta do servidor: C://Arquivos_CTI/Producao/Erros/Norte. {e.__class__.__name__}: {e}")
            # asyncio.run(telegram.Dev(f"Erro ao fazer o post na API do censo - CTI_NORTE com o arquivo: {arquivo[1]} . O mesmo está separado para avaliação na pasta do servidor: C://Arquivos_CTI/Producao/Erros/Norte. {e.__class__.__name__}: {e}"))
            time.sleep(1)
            shutil.move(nome_csv,erros_norte)
            continue
        
        try:
            api_censo.post_GED_hmg(nome_csv,arquivo[1])
        except Exception as e:
            Pidgin.main(f"Olá, ocorreu um erro no robô ao Subir o arquivo {arquivo[1]} para a S3 - CTI_NORTE. Erro: {e.__class__.__name__}: {e}")
            # asyncio.run(telegram.Dev(f"Ocorreu um erro ao Subir o arquivo {arquivo[1]} para a S3 - CTI_NORTE. Erro: {e.__class__.__name__}: {e}"))

        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-NORTE")


def post_arquivos_Sul_hmg():
    count          = 0
    pasta          = r"C:\Arquivos_CTI\Homologacao\Sul"
    erros_sul      = r"C:\Arquivos_CTI\Homologacao\Erros\Sul"
    nomes_arquivos = os.listdir(pasta)
    lista_ordenada = ordenarArquivos(nomes_arquivos,pasta)

    try:
        api_censo.auth_hmg()
    except Exception as e:
        Pidgin.main(f"Olá, ocorreu um erro no robô ao buscar o Token no Auth. {e.__class__.__name__}: {e}")
        # asyncio.run(telegram.Dev(f"Olá, ocorreu um erro ao buscar o Token no Auth.  {e.__class__.__name__}: {e}"))

    for arquivo in lista_ordenada:
        nome_csv = os.path.join(pasta, arquivo[1])
        try:
            api_censo.post_CtiSul_hmg(nome_csv,arquivo[1])
        except Exception as e:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_SUL com o arquivo: {arquivo[1]} . O mesmo foi separado para avaliação na pasta do servidor: C://Arquivos_CTI/Producao/Erros/Sul. Erro {e.__class__.__name__}: {e}")
            # asyncio.run(telegram.Dev(f"Erro ao fazer o post na API do censo - CTI_SUL com o arquivo: {arquivo[1]} . O mesmo está separado para avaliação na pasta do servidor: C://Arquivos_CTI/Producao/Erros/Sul. Erro {e.__class__.__name__}: {e}"))
            time.sleep(1)
            shutil.move(nome_csv,erros_sul)
            continue
        try:
            api_censo.post_GED_hmg(nome_csv,arquivo[1])
        except Exception as e:
            Pidgin.main(f"Olá, ocorreu um erro no robô ao Subir um arquivo para a S3 - CTI_SUL. Erro {e.__class__.__name__}: {e}")
            # asyncio.run(telegram.Dev(f"Ocorreu um erro ao Subir o arquivo {arquivo[1]} para a S3 - CTI_SUL. Erro: {e.__class__.__name__}: {e}"))
            
        time.sleep(1)
        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-SUL")

def ordenarArquivos(nomes_arquivos,pasta):
    lista_arquivos = []

    for nome in nomes_arquivos:
        data = os.path.getmtime(f"{pasta}/{nome}")
        lista_arquivos.append((data,nome))
        lista_arquivos.sort()
        print(lista_arquivos)
    return lista_arquivos

post_arquivos_Norte_hmg()

time.sleep(2)

post_arquivos_Sul_hmg()