import os
import shutil
import time
import menssage.Pidgin as Pidgin
import APIs.Producao.Api_Censo as api_censo


def post_arquivos_Norte():
    count = 0
    pasta = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Norte"
    erros_norte = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Erros\Norte"
    nomes_arquivos = os.listdir(pasta)
    try:
        api_censo.auth()
    except:
        Pidgin.main("Olá, ocorreu um erro no robô ao buscar o Token no Auth")
    
    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        try:
            api_censo.post_CtiNorte(nome_csv,nome)
        except:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_NORTE com o arquivo: {nome} . O mesmo está separado para avaliação na pasta: //10.0.0.239/automacao_faturamento/CTI/Producao/Erros/Sul")
            time.sleep(1)
            shutil.move(nome_csv,erros_norte)
            continue
        try:
            api_censo.post_GED(nome_csv,nome)
        except:
            Pidgin.main("Olá, ocorreu um erro no robô ao Subir um arquivo para a S3 - CTI_NORTE")

        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-NORTE")


def post_arquivos_Sul():
    count = 0
    pasta = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Sul"
    erros_sul = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Erros\Sul"
    nomes_arquivos = os.listdir(pasta)
    try:
        api_censo.auth()
    except:
        Pidgin.main("Olá, ocorreu um erro no robô ao buscar o Token no Auth")

    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        try:
            api_censo.post_CtiSul(nome_csv,nome)
        except:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_SUL com o arquivo: {nome} . O mesmo foi separado para avaliação na pasta: //10.0.0.239/automacao_faturamento/CTI/Producao/Erros/Sul")
            time.sleep(1)
            shutil.move(nome_csv,erros_sul)
            continue
        try:
            api_censo.post_GED(nome_csv,nome)
        except:
            Pidgin.main("Olá, ocorreu um erro no robô ao Subir um arquivo para a S3 - CTI_SUL")

        time.sleep(1)
        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-SUL")

post_arquivos_Norte()

time.sleep(2)

post_arquivos_Sul()