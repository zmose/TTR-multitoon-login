import os
import sys
import subprocess
import requests
import time
from config import *


class Account:
    def __init__(self, username, password, success = "false", cookie = "-1", queueToken = "-1"):
        self.username = username
        self.password = password
        self.success = success
        self.cookie = cookie
        self.queueToken = queueToken

    def createRequest(self):
        if(self.queueToken == "-1"):
            body = {"username": self.username, "password": self.password}
        else:
            body = {"username": self.username, "password": self.password, "queueToken": self.queueToken}
        return body
        


def request(account):
    x = requests.post(url=url, data=account.createRequest())
    data = x.json()
    print(data)
    account.success = data["success"]
    if("queueToken" in data):
        account.queueToken = data["queueToken"]
    if("cookie" in data):
        account.cookie = data["cookie"]


def launch(cookie = ""):
    os.environ['TTR_PLAYCOOKIE'] = cookie
    
    os.popen(launcher)


def main():
    os.environ['TTR_GAMESERVER'] = TTR_GAMESERVER
    accounts = []
    for user, password in zip(users, passwords):
        account = Account(user, password)
        accounts.append(account)

    for account in accounts:
        while(account.success != "true"):
            request(account)
            time.sleep(1)
        
        launch(account.cookie)

    return


if __name__ == "__main__":
    main()