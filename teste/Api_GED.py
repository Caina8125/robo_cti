import requests
import Authentication.Authentic 
import json
import time


def auth():
    global token
    global proxies

    urlAuth = 'https://amhptiss.amhp.com.br/api/Auth'
    # urlAuth = 'https://hmg.amhp.com.br/api/Auth'

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
    print('Token =>',token)



def post_GED():

    urlPost = 'https://amhpged.amhp.com.br/api/CensoArquivo/adicionar-arquivo'

    # urlPost = 'https://localhost:7222/api/CensoArquivo/adicionar-arquivo'

    headers = {
        'Authorization': f'bearer {token}'
    }

    data = {
        'Id': 1,
        'CensoId': 6,
        'TipoDocumentoId': 21
    }

    files = {
        'file': ('R_CENSO.csv', open(r'C:\Users\lucas.timoteo\Downloads\R_CENSO.csv', 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, verify=False)
    time.sleep(2)
    files['file'][1].close()
    print(response)
    print(f"Relatório de pacientes internados na CTI_Norte inseridos na API com sucesso")

auth()
post_GED()