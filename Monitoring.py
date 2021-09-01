import EmailNotification
import Ping
import time
import Servers

PING_INTERVAL = 1
RUN_INTERVAL = 5
cont = 0

while 1:

    for i in range(len(Servers.ipsList)):
        try:
            print(Ping.doPing(Servers.ipsList[i]))
        except:
            cont+=1
            if cont == 2:
                EmailNotification.send(i)
                cont = 0

        time.sleep(PING_INTERVAL)

time.sleep(RUN_INTERVAL)
