from ping3 import ping
from env import IP_ADDRESS


def is_online():
    result = ping(IP_ADDRESS)
    return bool(result)
