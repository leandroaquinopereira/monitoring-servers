import EmailNotification
import Ping
import time
import Servers

PING_INTERVAL = 900 #verificação a cada 15 minutos (900 segundos)

while 1:

    for i in range(len(Servers.ipsList())):
        try:
            print(Ping.doPing(Servers.ipsList()[i]))
        except:
            EmailNotification.send(Servers.ipsList()[i])

    time.sleep(PING_INTERVAL)
