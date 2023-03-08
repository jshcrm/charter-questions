import random

with open("macaddresses.txt", "w") as file:
    for x in range(100000):
        mac_address = "02:00:00:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        file.write(f"{mac_address} \n")
