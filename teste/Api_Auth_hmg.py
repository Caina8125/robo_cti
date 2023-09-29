import requests
import Authentication.Authentic
import json

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
    content = json.loads(post.content)
    token = content['AccessToken']
    print('Token =>',token)
    return token