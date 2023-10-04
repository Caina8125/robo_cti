import json
import time
import requests
import Authentication.Authentic




def auth_hmg():
    global token
    global proxies

    urlAuth = 'https://hmg.amhp.com.br/api/Auth'

    proxies = {
        "http": f"http:// + {Authentication.Authentic.login_proxy}:{Authentication.Authentic.senha_proxy}@10.0.0.230:3128/",
        "https": f"http://{Authentication.Authentic.login_proxy}:{Authentication.Authentic.senha_proxy}@10.0.0.230:3128/"
    }

    usuario_login = {
        "Usuario": Authentication.Authentic.login_censo,
        "Senha" : Authentication.Authentic.senha_censo
    }

    post = requests.post( urlAuth, usuario_login, proxies=proxies)
    time.sleep(1)
    content = json.loads(post.content)
    time.sleep(1)
    token = content['AccessToken']
    print("")
    print('Token =>',token)
    print("")




def post_GED_hmg(pasta,nomeArquivo):

    urlPost = 'https://amhpged.amhp.com.br/api/CensoArquivo/adicionar-arquivo'
    # urlPost = 'https://localhost:7222/api/CensoArquivo/adicionar-arquivo'

    headers = {
        'Authorization': f'bearer {token}'
    }

    data = {
        'Id': 1,
        'CensoId': NumeroId,
        'TipoDocumentoId': 1
    }

    files = {
        'file': (nomeArquivo, open(pasta, 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, verify=False)
    time.sleep(2)
    files['file'][1].close()
    print("")
    print("GED =>", response)
    print("")
    print(f"Relatório de pacientes internados na CTI_Norte inseridos na API com sucesso")





def post_CtiNorte_hmg(pasta,nomeArquivo):
    global NumeroId

    # urlPostDebug = 'https://localhost:7009/api/Upload/upload-csv-cti/11'

    urlPost = 'https://censo-api-hmg.amhp.com.br/api/Upload/upload-csv-cti/11'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'unidadeAtendimento': 11
    }

    files = {
        'file': (nomeArquivo, open(pasta, 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)
    files['file'][1].close()
    print("")
    print("CTI_NORTE =>",response)
    print("")
    print(f"Relatório de pacientes internados na CTI_Norte inseridos na API com sucesso")
    print("")
    content = json.loads(response.content)
    NumeroId = content['internacao']['idAuditoria']
    print("Id_Arquivo =>", NumeroId)
    print("")






def post_CtiSul_hmg(pasta,nomeArquivo):

    urlPost = 'https://censo-api-hmg.amhp.com.br/api/Upload/upload-csv-cti/8'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'unidadeAtendimento': 8
    }

    files = {
        'file': (nomeArquivo, open(pasta, 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)
    time.sleep(2)
    files['file'][1].close()
    print("")
    print(response)
    print("")
    print(f"Relatório de pacientes internados na CTI_Sul inseridos na API com sucesso")
    print("")
    content = json.loads(response.content)
    NumeroId = content['internacao']['idAuditoria']
    print("")
    print("Id_Arquivo =>", NumeroId)
    print("")






def getInternacao_cti_norte_hmg():

    urlGet = 'https://censo-api-hmg.amhp.com.br/api/Internacao/obter-por-evolucao/3/11'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'evolucao' : 3,
        'idUnidadeAtendimento' : 11
    }
    
    get = requests.get( urlGet, headers=headers , data=data , proxies=proxies)
    time.sleep(2)
    print(get)

    content = json.loads(get.content)
    print(content)
    
    valores = content['total'],content['censoPacientes']
    return valores



def getInternacao_cti_sul_hmg():

    urlGet = 'https://censo-api-hmg.amhp.com.br/api/Internacao/obter-por-evolucao/3/8'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'evolucao' : 3,
        'idUnidadeAtendimento' : 8
    }
    
    get = requests.get( urlGet, headers=headers , data=data , proxies=proxies)
    time.sleep(2)
    print(get)

    content = json.loads(get.content)
    qtd_internados = content['total']
    pacientes = content['censoPacientes']
    print(qtd_internados)
    print(pacientes)
    return qtd_internados
