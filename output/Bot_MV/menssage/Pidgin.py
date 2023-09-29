import xmpp
import Authentication.Authentic

pidgin_Id= Authentication.Authentic.host_pidgin
senha    = Authentication.Authentic.senha_pidgin
msg      = "Bot_CTI Funcionando"

devs     = [
                "heloisa.silva@chat.amhp.local",
                "hugo.oliveira@chat.amhp.local",
                "lucas.timoteo@chat.amhp.local", 
                "lucas.paz@chat.amhp.local",
                "thiago.borges@chat.amhp.local",
                "michael.ribeiro@chat.amhp.local"
            ]

def main(texto):
    count = 0
    jid = xmpp.protocol.JID(pidgin_Id)
    connection = xmpp.Client(server=jid.getDomain())
    connection.connect()
    connection.auth(user=jid.getNode(), password=senha, resource=jid.getResource())
    for i in range(6):
        connection.send(xmpp.protocol.Message(to=devs[count], body=texto))
        count = count + 1

if __name__ == "__main__":
    main()