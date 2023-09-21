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
            print(handle.base_address)
            break
        except(except_x.ProcessNotFound, AttributeError) as error_founded:
            os.system("cls")
            print("WAITING TO LAUNCH HOLOCURE...")
            time.sleep(5)
            continue
if __name__ == "__main__":
    Main()