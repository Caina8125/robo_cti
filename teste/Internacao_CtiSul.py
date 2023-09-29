import requests

def obterInternacao():
    # urlPostDebug = 'https://localhost:7009/api/Upload/upload-csv-cti/11'

    urlPost = 'https://censo-api-hmg.amhp.com.br/api/Internacao/obter-por-evolucao/3/11'

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




# Api_Censo_hmg.auth_hmg()