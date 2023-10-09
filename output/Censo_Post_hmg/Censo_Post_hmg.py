import os
import time
import shutil
import menssage.Pidgin as Pidgin
import APIs.Homologacao.Api_Censo_hmg as api_censo


def post_arquivos_Norte_hmg():
    count = 0
    pasta = r"C:\Arquivos_CTI\Homologacao\Norte"
    erros_norte = r"C:\Arquivos_CTI\Homologacao\Erros\Norte"
    nomes_arquivos = os.listdir(pasta)
    try:
        api_censo.auth_hmg()
    except Exception as e:
        Pidgin.main(f"Olá, ocorreu um erro no robô ao buscar o Token no Auth. Erro: {e.args}")
    
    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        try:
            api_censo.post_CtiNorte_hmg(nome_csv,nome)
        except Exception as e:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_NORTE com o arquivo: {nome} . O mesmo está separado para avaliação na pasta: //10.0.0.239/automacao_faturamento/CTI/Producao/Erros/Sul. Erro {e.args}")
            time.sleep(1)
            shutil.move(nome_csv,erros_norte)
            continue
        try:
            api_censo.post_GED_hmg(nome_csv,nome)
        except Exception as e:
            Pidgin.main(f"Olá, ocorreu um erro no robô ao Subir um arquivo para a S3 - CTI_NORTE. Erro: {e.args}")

        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-NORTE")


def post_arquivos_Sul_hmg():
    count = 0
    pasta = r"C:\Arquivos_CTI\Homologacao\Sul"
    erros_sul = r"C:\Arquivos_CTI\Homologacao\Erros\Sul"
    nomes_arquivos = os.listdir(pasta)
    try:
        api_censo.auth_hmg()
    except Exception as e:
        Pidgin.main(f"Olá, ocorreu um erro no robô ao buscar o Token no Auth. Erro {e.args}")

    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        try:
            api_censo.post_CtiSul_hmg(nome_csv,nome)
        except Exception as e:
            Pidgin.main(f"Olá, erro no robô ao fazer o post na API do censo - CTI_SUL com o arquivo: {nome} . O mesmo foi separado para avaliação na pasta: //10.0.0.239/automacao_faturamento/CTI/Producao/Erros/Sul. Erro {e.args}")
            time.sleep(1)
            shutil.move(nome_csv,erros_sul)
            continue
        try:
            api_censo.post_GED_hmg(nome_csv,nome)
        except Exception as e:
            Pidgin.main(f"Olá, ocorreu um erro no robô ao Subir um arquivo para a S3 - CTI_SUL. Erro {e.args}")

        time.sleep(1)
        os.remove(nome_csv)
        print(f"O arquivo {nome_csv} foi removido da sua pasta")
        count = count + 1
        print(count,"Post na API - CTI-SUL")

post_arquivos_Norte_hmg()

time.sleep(2)

post_arquivos_Sul_hmg()