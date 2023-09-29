import src.Bot_Homologacao.Cti_Norte_hmg as cti_n_hmg
import src.Bot_Homologacao.Cti_Sul_hmg as cti_s_hmg

def automacao():

    cti_n_hmg.iniciar_CtiNorte()
    
    cti_s_hmg.iniciar_CtiSul()

automacao()