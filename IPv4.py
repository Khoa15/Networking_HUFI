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
    ip = "192.168.1.0"
    # bit = input("Enter a bit: ")
    bit = 24
    # vay = 0
    vay = 2
    # if scene == 2:
    #     vay = input("So bit muon: ")
    return ip, bit, vay
def getClass(ip = []):
    for cls in CLASSES:
        if ip[0] >= cls["min"] and ip[0] <= cls["max"]:
            return cls
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
        n = int(n) if n != 0 else ceil((bit - class_ip['octet_net']) / 8)
        m = class_ip['octet_net'] - n
        int(pow(2, n))
        ip_pos = ceil(int(bit) / class_ip['octet_net']) - 1
        ip[ip_pos] /= FRAMES[n]
        ip[ip_pos] = int(ip[ip_pos]) * FRAMES[n]
        print(ip)
    # except:
    #     print("Your input isn't true form.")
def ipToIpBin(ip = []):
    ip_bin = []
    for x in ip:
        ip_bin.append("{0:08b}".format((x)))
    return ip_bin
def convertToIpMask(ip = [], bit):
    ipToIpBin(ip)
    l = []
    for x in ip:

def Scene_1(inp):
    ip, bit, n = inp
    ip = list(map(int, ip.split(".")))
    bit = int(bit)
    class_ip = getClass(ip)
    n = ceil((bit - class_ip['octet_net']) / 8)
    ip_pos_x = ceil(bit / class_ip['octet_net']) - 1
    ip[ip_pos_x] /= FRAMES[n]
    ip[ip_pos_x] = int(ip[ip_pos_x]) * FRAMES[n]

    print(ip)
def Scene_2(inp):
    ip, bit, n = inp
    ip = list(map(int, ip.split(".")))
    bit = int(bit)
    n = int(n)
    class_ip = getClass(ip)
    m = class_ip['octet_net'] - n
    print(f"So bit host con lai: {m} host")
    print(f"So subnet co the co: {pow(n, 2)} subnet")
    print(f"So host tren mot subnet: {pow(2, 6) - 2} host/subnet")
    print(f"Subnetmask moi: ")

def cleanIp(ip = ""):
    return list(map(int, ip.split('.')))

if __name__ == "__main__":
    Menu()
    # scene = int(input("Choose a scene: "))
    # scene = 2
    # Scene(scene, getInput(scene))
    print(ipToIpBin(cleanIp("192.168.1.0")))
