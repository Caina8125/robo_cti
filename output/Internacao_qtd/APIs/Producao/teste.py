import json
import time
import requests
# import menssage.Pidgin as Pidgin
# import Authentication.Authentic
from datetime import datetime


def auth():
    global token
    global proxies

    urlAuth = 'http://soulhosp.gruposanta.com.br/soul-product-forms/services/message/message?user=ULLY.VIEIRA'
    # proxies = {
    #     "http": f"http:// + {Authentication.Authentic.login_proxy}:{Authentication.Authentic.senha_proxy}@10.0.0.230:3128/",
    #     "https": f"http://{Authentication.Authentic.login_proxy}:{Authentication.Authentic.senha_proxy}@10.0.0.230:3128/"
    # }

    # usuario_login = {
    #     "Usuario": "ully.vieira",
    #     "Senha" : "09282605"
    # }

    post = requests.post( urlAuth ,verify=False)
    print(post)

    # content = json.loads(post.content)
    # time.sleep(1)
    # token = content['AccessToken']
    # time.sleep(1)
    # print('Token =>',token)




# def post_GED(pasta,nomeArquivo):

#     urlPost = 'https://amhpged.amhp.com.br/api/CensoArquivo/adicionar-arquivo'

#     headers = {
#         'Authorization': f'bearer {token}'
#     }

#     data = {
#         'Id': 1,
#         'CensoId': NumeroId,
#         'TipoDocumentoId': 21
#     }

#     files = {
#         'file': (nomeArquivo, open(pasta, 'rb'))
#     }

#     response = requests.post(urlPost, headers=headers, data=data, files=files, verify=False)
#     time.sleep(2)
#     files['file'][1].close()
#     print("")
#     print("GED =>", response)
#     print("")
#     print(f"O arquivo: {nomeArquivo} foi armazenado na S3")
#     print("")





# def post_CtiNorte(pasta,nomeArquivo):
#     global NumeroId

#     urlPost = 'https://censo-api.amhp.com.br/api/Upload/upload-csv-cti/11'

#     headers = {
#         'Authorization': f'Bearer {token}'
#     }

#     data = {
#         'unidadeAtendimento': 11
#     }

#     files = {
#         'file': (nomeArquivo, open(pasta, 'rb'))
#     }

#     response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)
#     files['file'][1].close()
#     print("")
#     print("CTI_NORTE =>",response)
#     print("")
#     print(f"Relatório de pacientes internados na CTI_Norte inseridos na API com sucesso")
#     print("")
#     content = json.loads(response.content)
#     NumeroId = content['internacao']['idAuditoria']
#     print("Id_Arquivo =>", NumeroId)
#     print("")



# def post_CtiSul(pasta,nomeArquivo):
#     global NumeroId

#     urlPost = 'https://censo-api.amhp.com.br/api/Upload/upload-csv-cti/8'

#     headers = {
#         'Authorization': f'Bearer {token}'
#     }

#     data = {
#         'unidadeAtendimento': 8
#     }

#     files = {
#         'file': (nomeArquivo, open(pasta, 'rb'))
#     }

#     response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)
#     time.sleep(2)
#     files['file'][1].close()
#     print("")
#     print("CTI_SUL =>",response)
#     print("")
#     print(f"Relatório de pacientes internados na CTI_Sul inseridos na API com sucesso")
#     print("")
#     content = json.loads(response.content)
#     NumeroId = content['internacao']['idAuditoria']
#     print("")
#     print("Id_Arquivo =>", NumeroId)
#     print("")


   