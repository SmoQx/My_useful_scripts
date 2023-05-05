import os
import sys
import time
import subprocess
import re


def main(argv):
    def run_command(cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed


    def wpisz_komende(komenda):
        return run_command(cmd=komenda).stdout


    try:
        if argv[1] == '-t':
            ilosc_razy = 9999999999
        else:
            ilosc_razy = int(argv[1])
    except IndexError:
        ilosc_razy = 1


    for x in range(ilosc_razy):
        try:
            try:
                string_z = str(wpisz_komende(komenda='ping '+ argv[0]+ ' -n 1').decode())

                sting_odpowiedni = re.search(r"Reply.*TTL=\d+", string_z)
                if sting_odpowiedni == None:
                    print(string_z)
                    pass
                else:
                    print(sting_odpowiedni[0], end=' ')
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                print(current_time)
            except IndexError:
                print('Brak IP lub nazyw')
        except KeyboardInterrupt:
            print('Koniec')
            break




if __name__ == "__main__":
    sys.argv = ['asd', "PC1026SPN", "-t"]
    main(sys.argv[1:])
    tablica_na = ['MD29SPN', 'PC610SPN', 'PC612SPN', 'PC625SPN', 'PC626SPN', 'PC637SPN', 'PC998SPN']