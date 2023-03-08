from typing import Union

mac_addresses = []

def find_mac_address(mac_address: str) -> Union[str, None]:
    with open("macaddresses.txt", "r") as file:
        for x in file.readlines():
            if mac_address == x.strip():
                return mac_address

find_mac_address("02:00:00:cd:ba:d9")
