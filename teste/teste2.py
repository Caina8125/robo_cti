import requests
import Authentic



proxies = {
        "http": f"http:// + {Authentic.login_proxy}:{Authentic.senha_proxy}@10.0.0.230:3128/",
        "https": f"http://{Authentic.login_proxy}:{Authentic.senha_proxy}@10.0.0.230:3128/"
}

url = 'https://censo-api-hmg.amhp.com.br/api/Upload/upload-csv-cti/11'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjYjE4NzdmNS00YTg5LTc2ZjgtZTA1MC0xNGM5ZTcwMjE2ODIiLCJ1bmlxdWVfbmFtZSI6Imx1Y2FzLmNhaW5hIiwianRpIjoiMzk4YTViYzUtNWQyOC00MmY5LWJlZDgtYmIyMTZiZTk2YjFiIiwibmJmIjoxNjkzOTExMTkwLCJpYXQiOjE2OTM5MTExOTAsImlkIjoiNDM1OTAyNTEiLCJub21lIjoiTHVjYXMgQ2FpbsOjIiwicGVzc29hX2Zpc2ljYSI6InRydWUiLCJyb2xlIjpbIkZ1bmNpb25hcmlvQU1IUCIsIkFkbWluaXN0cmFkb3IiXSwiZXhwIjoxNjkzOTQ3MTkwLCJpc3MiOiJBTUhQIiwiYXVkIjoiaHR0cHM6Ly9obWdhbWhwdGlzcy5hbWhwZGYubG9jYWwifQ.9FShaDQQpQqcyAII9hunzfb87vY2KZdQ3x8oUfVEU1s'

headers = {
    'api-key': 'E3AA97B8-7BEA-4E68-AA8D-55EA7A7E76F5',
    'Authorization': f'Bearer {token}'
}

data = {
    'unidadeAtendimento': 11
}

files = {
    'file': ('r_censo_retro.csv', open(r'C:\Users\lucas.timoteo\Desktop\r_censo_retro.csv', 'rb'))
}

response = requests.post(url, headers=headers, data=data, files=files, proxies=proxies)

files['file'][1].close()

print(response)