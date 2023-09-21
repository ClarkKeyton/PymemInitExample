import pymem as p
import pymem.exception as except_x
import winsound as ws
import os
import time
looping = ws.SND_FILENAME | ws.SND_ASYNC | ws.SND_LOOP
def Main():
    ws.PlaySound("Chipscape_TPazolite.wav", looping)
    while True:
        try:
            handle = p.Pymem("HoloCure.exe")
            os.system("cls")
            hexadec = hex(handle.base_address)
            ws.PlaySound(None, ws.SND_PURGE)
            print(str(hexadec))
            time.sleep(3)
            break
        except(except_x.ProcessNotFound, AttributeError) as error_founded:
            os.system("cls")
            print("WAITING TO LAUNCH HOLOCURE...")
            time.sleep(5)
            continue
if __name__ == "__main__":
    Main()
