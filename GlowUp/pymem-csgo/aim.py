import pymem
import pymem.process
import keyboard
import requests
from math import sqrt, pi, atan

try:    
    hazedumper = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()
except (ValueError, requests.RequestException):
    exit("[-] Failed to fetch the latests offsets from hazedumper!")

pm = pymem.Pymem("csgo.exe")

client = pymem.process.module_from_name(pm.process_handle,"client.dll").lpBaseOfDll
engine = pymem.process.module_from_name(pm.process_handle,"engine.dll").lpBaseOfDll

aimfov = 120

def normalizeAngles(viewAngleX, viewAngleY):
    if viewAngleX > 89:
        viewAngleX -= 360
    if viewAngleX < -89:
        viewAngleX += 360
    if viewAngleY > 180:
        viewAngleY -= 360
    if viewAngleY < 180:
        viewAngleY += 360
    return viewAngleX, viewAngleY

def checkAngles(x,y):
    if x > 89:
        return False
    if 