import APIs.Homologacao.Api_Censo_hmg as api_censo_hmg
import os



def post_arquivos_Norte():
    pasta = r"\\10.0.0.239\automacao_faturamento\CTI\Homologacao\Norte"
    nomes_arquivos = os.listdir(pasta)
    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        api_censo_hmg.auth_hmg()
        api_censo_hmg.post_CtiNorte_hmg(nome_csv,nome)
        api_censo_hmg.post_GED_hmg(nome_csv,nome)



def post_arquivos_Sul():
    pasta = r"\\10.0.0.239\automacao_faturamento\CTI\Homologacao\Sul"
    nomes_arquivos = os.listdir(pasta)
    for nome in nomes_arquivos:
        nome_csv = os.path.join(pasta, nome)
        api_censo_hmg.auth_hmg()
        api_censo_hmg.post_CtiSul_hmg(nome_csv,nome)
        api_censo_hmg.post_GED_hmg(nome_csv,nome)


post_arquivos_Norte()