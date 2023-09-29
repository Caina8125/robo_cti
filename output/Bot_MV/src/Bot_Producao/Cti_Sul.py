import os
import time
from abc import ABC
from datetime import datetime
from selenium import webdriver
import menssage.Pidgin as Pidgin
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageElement(ABC):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url
    def open(self):
        atual = datetime.now()
        date = atual.strftime("%d-%m-%Y às %H:%M:%S")
        try:
            self.driver.get(self.url)
        except:
            Pidgin.main(f'Olá, Ocorreu um erro no Bot_CTI_Sul ao tentar fazer login no MV, o sistema não responde. Data: {date}')

class Login(PageElement):
    usuario = (By.XPATH, '//*[@id="username"]')
    senha = (By.XPATH, '//*[@id="password"]')
    logar = (By.XPATH, '//*[@id="context_login"]/section[4]/input[7]')
    path = (By.XPATH, '//*[@id="serverURL"]')

    def exe_login(self, usuario, senha):
        time.sleep(1)
        print('Logando no MV...')
        self.driver.find_element(*self.usuario).send_keys(usuario)
        self.driver.find_element(*self.senha).send_keys(senha)
        self.driver.find_element(*self.logar).click()
        print('Login executado')
        time.sleep(2)

class relatorio(PageElement):
    pesquisar = (By.XPATH, '//*[@id="workspace-menubar"]/ul/li[1]/label')
    escrever = (By.XPATH, '//*[@id="menu-filter-1"]')
    censo = (By.XPATH, '//*[@id="workspace-menubar"]/ul/li[2]/a')
    confere = (By.XPATH, '//*[@id="status"]/div/span[5]')
    teste = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div/form/div/div')
    imprimir = (By.ID, "frames23")
    id_iframe = 'child_APOIO.HTML,ATEND.HTML,DIAGN.HTML,EXTENSION.HTML,GLOBAL.HTML,INTER.HTML'
    opcao_csv = (By.XPATH,'//*[@id="frames10_ac"]')
    info_uti = (By.XPATH,'//*[@id="inp:cdUnidInt"]')
    lista_uti = ["62","85","10","56","57"]

    def Emitir_relatorio(self):
        global count
        atual = datetime.now()
        date = atual.strftime("%d-%m-%Y às %H:%M:%S")

        try:
            time.sleep(2)
            print('Buscando relatórios de pacientes internados...')
            try:
                self.driver.find_element(*self.pesquisar).click()
            except:
                driver.get(url)
                time.sleep(2)
                self.driver.find_element(*self.pesquisar).click()

            self.driver.find_element(*self.escrever).send_keys('Censo')
            time.sleep(2)
            self.driver.find_element(*self.censo).click()
            time.sleep(5)
            print("Ativando o acesso ao site renderizado...")
            self.driver.switch_to.frame('child_APOIO.HTML,ATEND.HTML,DIAGN.HTML,GLOBAL.HTML,INTER.HTML')
            print("Acesso ao site renderizado concluído")
            csv = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="frames10_ac"]')))
            driver.find_element(*self.opcao_csv).click()
            time.sleep(1)
            driver.find_element(*self.opcao_csv).clear()
            time.sleep(2)
            driver.find_element(*self.opcao_csv).send_keys('CSV')
            time.sleep(1)
        except:
            Pidgin.main(f'Olá, Ocorreu um erro no Bot_CTI_Sul ao Buscar o relatório no MV, o sistema não responde. Data: {date}')

        i = 0
        count = 0
        
        for i in range(5):
            try:
                print("Emitindo relatório")
                info = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="inp:cdUnidInt"]')))
                self.driver.find_element(*self.info_uti).click()
                time.sleep(1)
                self.driver.find_element(*self.info_uti).clear()
                time.sleep(1)
                self.driver.find_element(*self.info_uti).send_keys(*self.lista_uti[count])
                print("Relatório emitido com sucesso")
                button = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, "frames23")))
                self.driver.find_element(By.ID, "frames23").click()
                time.sleep(5)
            except:
                Pidgin.main(f'Olá, Ocorreu um erro no Bot_CTI_Sul ao Buscar o relatório no MV, o sistema não responde. Data: {date}')

            # self.producao()

            try:
                time.sleep(2)
                relatorio(driver, url).movePath()
            except:
                Pidgin.main(f'Olá, Ocorreu um erro no Bot_CTI_Sul ao renomear o arquivo na data:{date}')
            count = count + 1
        driver.quit()


    def movePath(self):
        global lista_relatorio

        lista_relatorio = ['UTI B2', 'UTI B3', 'UTI C1','UTI C2','UTI C3']
        atual = datetime.now()
        date = atual.strftime("%d-%m-%Y às %H-%M-%S")
        nameAtual = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Sul\R_CENSO.csv"
        renomear = r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Sul" + f"\\{lista_relatorio[count]} "+ f"{date}" + ".csv"
        # shutil.move(arqLocal,arqDest)
        time.sleep(2)
        os.replace(nameAtual,renomear)
        print("Arquivo renomeado e guardado com sucesso")
    
    # def producao(self):
    #     Api.upload_CtiSul() 

#------------------------------------------------------------------------------------------------------------------------------------------

def iniciar_CtiSul():
    global driver
    global url

    url = 'http://soulmv.gruposanta.com.br/mvautenticador-cas/login?service=http%3A%2F%2Fsoulmv.gruposanta.com.br%3A80%2Fsoul-mv%2Fcas'

    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', { "download.default_directory": r"\\10.0.0.239\automacao_faturamento\CTI\Producao\Sul",
                                                      "download.prompt_for_download": False,
                                                      "download.directory_upgrade": True,
                                                      "plugins.always_open_pdf_externally": True
                                                       })
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    login_page = Login(driver , url)
    time.sleep(2)
    login_page.open()
    login_page.exe_login(
        usuario = "guilherme.nunes",
        senha = "86247979"
        )
    
    relatorio(driver, url).Emitir_relatorio()
    
