from math import ceil
FRAMES = [128, 64, 32, 16, 8, 4, 2, 1]
CLASSES = [
    {
        "name": "A",
        "octet_net": 24,
        "min": 1,
        "max": 126,
    },
    {
        "name": "B",
        "octet_net": 16,
        "min": 128,
        "max": 191,
    },
    {
        "name": "C",
        "octet_net": 8,
        "min": 192,
        "max": 223,
    },
]
def Menu():
    print("""
        1. Chia subnet
        2. Tim subnet cho host
        """)
def getInput(scene):
    # ip = input("Enter an ip: ")
    ip = "192.168.1.158"
    # bit = input("Enter a bit: ")
    bit = 28
    vay = ""
    if scene == 2:
        vay = input("So bit muon: ")
    return ip, bit, vay
def Scene(scene, inp):
    # try:
        ip, bit, n = inp
        ip = list(map(int, ip.split(".")))
        bit = int(bit)
        class_ip = {}
        for cls in CLASSES:
            if ip[0] >= cls["min"] and ip[0] <= cls["max"]:
                class_ip = cls
                break
        if class_ip == {}:
            return False
        n = int(n) if len(n) != 0 else ceil((bit - class_ip['octet_net']) / 8)
        ip_pos = ceil(int(bit) / class_ip['octet_net']) - 1
        ip[ip_pos] /= FRAMES[n]
        ip[ip_pos] = int(ip[ip_pos]) * FRAMES[n]
        print(ip)
    # except:
    #     print("Your input isn't true form.")

if __name__ == "__main__":
    Menu()
    scene = int(input("Choose a scene: "))
    Scene(scene, getInput(scene))
