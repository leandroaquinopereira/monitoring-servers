import pandas as pd

table = pd.read_excel('ServersList.xlsx','Sheet1')

def ipsList():

    ips = []

    for i in range(len(table)):
        ips.append(table['IP'][i])

    ips = list(set(ips))

    return ips


def usersList():

    users = []

    for i in range(len(table)):
        users.append(table['Users'][i])

    users = list(set(users))

    return users