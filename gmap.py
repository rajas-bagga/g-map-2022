import socket
from threading import Thread
import time

stop_threads = False
G = '\033[32m'
RESET = '\033[0m'
start_time = time.time()
ip = input("Enter ip or domain of site> ")

print("OPEN PORT              SERVICE")

def scan(start, end, echo=False):
    global stop_threads
    for i in range(start, end):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.7)

            addr = ((ip, i))

            r = s.connect_ex(addr)

            if r == 0:

                try:
                    service = socket.getservbyport(i)
                except:
                    service = "Unable to detect service"

                print(("    " + str(i) + "\t" + service).expandtabs(25))
            
            if stop_threads:
                break
            
            if echo:
                percent = int(((i-start)/100)*100)
                print(f"Scan {percent}% completed", end='\r')

                if percent == 99:
                    print(
                        f"{G}Scan completed in {int(time.time() - start_time)} seconds{RESET}")
                    stop_threads = True
                    break
            s.close()
        except:
            pass


start = 0
end = 100
j = 1
while j <= 655:

    if j == 655:
        Thread(target=scan, args=(start, end, True)).start()
    else:
        Thread(target=scan, args=(start, end)).start()
    start += 100
    end += 100
    j += 1


