from ping3 import ping
from env import IP_ADDRESS, PORT
import os


def is_host_up():
    command = f'nmap -p {PORT} {IP_ADDRESS} -Pn | grep open'
    stream = os.popen(command)
    output = stream.read()
    return bool(output)


def is_online():
    result = ping(IP_ADDRESS)
    return bool(result)

