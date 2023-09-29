import src.Bot_Producao.Cti_Norte as cti_n
import src.Bot_Producao.Cti_Sul as cti_s
import time

def automacao():

    cti_n.iniciar_CtiNorte()

    time.sleep(2)
    
    cti_s.iniciar_CtiSul()

automacao()