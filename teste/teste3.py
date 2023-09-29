import time
from abc import ABC
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

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
        time.sleep(2)
        self.driver.find_element(*self.usuario).send_keys(usuario)
        self.driver.find_element(*self.senha).send_keys(senha)
        self.driver.find_element(*self.logar).click()
        time.sleep(4)


class caminho(PageElement):
    pesquisar = (By.XPATH, '//*[@id="workspace-menubar"]/ul/li[1]/label')
    escrever = (By.XPATH, '//*[@id="menu-filter-1"]')
    censo = (By.XPATH, '//*[@id="workspace-menubar"]/ul/li[2]/a')
    confere = (By.XPATH, '//*[@id="status"]/div/span[5]')
    teste = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div/form/div/div')
    imprimir = (By.XPATH,'//*[@id="frames23"]')

    def exe_caminho(self):
        time.sleep(2)
        
        try:
            self.driver.find_element(*self.pesquisar).click()
        except:
            driver.get(url)
            time.sleep(2)
            self.driver.find_element(*self.pesquisar).click()

        self.driver.find_element(*self.escrever).send_keys('Censo retroativo')
        time.sleep(2)
        self.driver.find_element(*self.censo).click()
        time.sleep(20)
        # self.driver.find_element(*self.imprimir).click()

        time.sleep(100)
        

#------------------------------------------------------------------------------------------------------------------------------------------

url = 'http://soulmv.gruposanta.com.br/mvautenticador-cas/login?service=http%3A%2F%2Fsoulmv.gruposanta.com.br%3A80%2Fsoul-mv%2Fcas'

servico = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.binary_location = r"C:\centbrowser_4.0.9.112_portable\chrome.exe"

driver = webdriver.Chrome()

driver.maximize_window()
login_page = Login(driver , url)
time.sleep(2)
login_page.open()
login_page.exe_login(
    usuario = "ully.vieira",
    senha = "09282605"
)

caminho(driver, url).exe_caminho()