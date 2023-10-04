import os
import time
import shutil
from abc import ABC
import src.Api_Censo_hmg
from datetime import datetime
from selenium import webdriver
# from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageElement(ABC):
    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = url
    def open(self):
        self.driver.get(self.url)

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
    lista_uti = ["84","82","111"]
    

    def Emitir_relatorio(self):
        global count

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
        self.driver.switch_to.frame('child_APOIO.HTML,ATEND.HTML,DIAGN.HTML,EXTENSION.HTML,GLOBAL.HTML,INTER.HTML')
        print("Acesso ao site renderizado concluído")
        # try:
        csv = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH,'//*[@id="frames10_ac"]')))
        driver.find_element(*self.opcao_csv).click()
        time.sleep(1)
        driver.find_element(*self.opcao_csv).clear()
        time.sleep(2)
        driver.find_element(*self.opcao_csv).send_keys('CSV')
        time.sleep(1)

        i = 0
        count = 0
        
        for i in range(3):
            print("Emitindo relatório")
            time.sleep(1)
            self.driver.find_element(*self.info_uti).click()
            time.sleep(1)
            self.driver.find_element(*self.info_uti).clear()
            time.sleep(1)
            self.driver.find_element(*self.info_uti).send_keys(*self.lista_uti[count])
            print("Relatório emitido com sucesso")
            time.sleep(1)
            self.driver.find_element(By.ID, "frames23").click()
            time.sleep(5)

            src.Api_Censo_hmg.executarPost()
            
            
            relatorio(driver, url).movePath()
            
            count = count + 1

        driver.quit()
        # except:
        #     print('Ocorreu um erro no MV')


    def movePath(self):
        global lista_relatorio

        lista_relatorio = ['UTI A', 'UTI B', 'UTI C']

        

        arqLocal = r"C:\Users\lucas.timoteo\Downloads\R_CENSO.csv"

        atual = datetime.now()
        date = atual.strftime("%d-%m-%Y %H-%M-%S")

        data = os.path.getmtime(arqLocal)
        dataFormat = time.ctime(data)
        objLocal = time.strptime(dataFormat)
        trasnfLocal = time.strftime("%d-%m-%y %H:%M:%S", objLocal)
        print(trasnfLocal)

        arqDest = r"\\10.0.0.239\informatica\Relatorios_cti\R_CENSO.csv"
        renomear = r"\\10.0.0.239\informatica\Relatorios_cti\Norte" + f"\\{lista_relatorio[count]} "+ f"{date}" + ".csv"

        shutil.move(arqLocal,arqDest)

        time.sleep(2)

        os.replace(arqDest,renomear)

        print("Arquivo renomeado e guardado com sucesso")
    
#------------------------------------------------------------------------------------------------------------------------------------------

def iniciar():
    global driver
    global url

    url = 'http://soulmv.gruposanta.com.br/mvautenticador-cas/login?service=http%3A%2F%2Fsoulmv.gruposanta.com.br%3A80%2Fsoul-mv%2Fcas'

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome()

    driver.maximize_window()
    login_page = Login(driver , url)
    time.sleep(2)
    login_page.open()
    login_page.exe_login(
        usuario = "ully.vieira",
        senha = "09282605"
        )

    relatorio(driver, url).Emitir_relatorio()