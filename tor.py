# coding:utf-8
# reference below, but I modified, because it's not totally for me.
# http://www.learn4master.com/programming-language/python/install-and-use-tor-on-ubuntu-for-python-requests
import time
import socket
import socks
import requests
from stem import Signal
from stem.control import Controller

url = '127.0.0.1'

controller = Controller.from_port(address=url, port=9051)


def connectTor():
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, url, 9050, True)
    socket.socket = socks.socksocket


def renew_tor():
    controller.authenticate(password="123456")
    controller.signal(Signal.NEWNYM)
    pass


def showmyip():
    r = requests.get('http://icanhazip.com/')
    ip_address = r.text.strip()
    print(ip_address)


def ip():
    for i in range(5):
        renew_tor()
        connectTor()
        showmyip()
        time.sleep(10)

if __name__ == '__main__':
    ip()
