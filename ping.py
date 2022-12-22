from ping3 import ping
from env import IP_ADDRESS
import os


def is_host_up():
    stream = os.popen(f'nmap -p 1234 {IP_ADDRESS} -Pn | grep "(1 host up)"')
    output = stream.read()
    return bool(output)


def is_online():
    result = ping(IP_ADDRESS)
    return bool(result)

