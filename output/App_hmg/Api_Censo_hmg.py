import requests
import json
import src.Authentic


def auth():
    global token
    global proxies

    urlAuth = 'https://hmg.amhp.com.br/api/Auth'

    proxies = {
        "http": f"http:// + {src.Authentic.login_proxy}:{src.Authentic.senha_proxy}@10.0.0.230:3128/",
        "https": f"http://{src.Authentic.login_proxy}:{src.Authentic.senha_proxy}@10.0.0.230:3128/"
    }

    usuario_login = {
        "Usuario": src.Authentic.login_censo,
        "Senha" : src.Authentic.senha_censo
    }

    post = requests.post( urlAuth,
                        usuario_login,
                        proxies=proxies)
    
    content = json.loads(post.content)

    token = content['AccessToken']
    print('Token =>',token)


def post_Cti_Norte():

    # urlPostDebug = 'https://localhost:7009/api/Upload/upload-csv-cti/11'

    urlPost = 'https://censo-api-hmg.amhp.com.br/api/Upload/upload-csv-cti/11'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'unidadeAtendimento': 11
    }

    files = {
        'file': ('R_CENSO.csv', open(r'C:\Users\lucas.timoteo\Downloads\R_CENSO.csv', 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)

    files['file'][1].close()
    print(response)
    print(f"Relatório de pacientes internados na CTI_Norte inseridos na API com sucesso")


def post_Cti_Sul():

    urlPost = 'https://censo-api-hmg.amhp.com.br/api/Upload/upload-csv-cti/8'

    headers = {
        'api-key': 'E3AA97B8-7BEA-4E68-AA8D-55EA7A7E76F5',
        'Authorization': f'Bearer {token}'
    }

    data = {
        'unidadeAtendimento': 8
    }

    files = {
        'file': ('r_censo_retro.csv', open(r'C:\Users\lucas.timoteo\Downloads\R_CENSO.csv', 'rb'))
    }

    response = requests.post(urlPost, headers=headers, data=data, files=files, proxies=proxies)

    files['file'][1].close()

    print(response.text)
#-------------------------------------------------------------------------------------------------------
def executarPost():
    auth()

    post_Cti_Norte()

