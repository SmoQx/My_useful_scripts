import os
import subprocess
import time

def run_command(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed


def wpisz_komende(komenda):
    return run_command(cmd=komenda).stdout


def cmd_run(komenda):
    os.system(komenda)


def main2():
    tablica = pobierzlsite_pc()

    for pc in tablica:
        #print('copy C:\\temp3\gfx_win101.2115.exe \\\\' + pc + '\\temp')
        if os.path.exists("\\\\"+ pc + "\\c$\\temp"):
            print(run_command(cmd='copy C:\\temp3\\gfx_win_101.2115.exe \\\\' + pc + '\\c$\\temp'))
        else:
            print(run_command(cmd="mkdir \\\\" + pc + "\\c$\\temp"))
            print(run_command(cmd='copy C:\\temp3\\gfx_win_101.2115.exe \\\\' + pc + '\\c$\\temp'))
    print("Zakończono kopiowanie")
    time.sleep(120)

def main():
    tablica = pobierzlsite_pc()
    for pc in tablica:
        komenda_polacz = "psexec \\\\" + pc + " powershell.exe Start-Process c:\\temp\\gfx_win_101.2115.exe -ArgumentList '/silent' -Wait"
        #komenda_install = "Start-Process c:\\temp\\gfx_win_101.2115.exe -ArgumentList '/silent' -Wait"
        print(run_command(cmd=komenda_polacz))
        #print(run_command(cmd=komenda_install))
        print(run_command(cmd='exit'))
    print("Zakończono instalację")


def pobierzlsite_pc():
    tablica_zmiennych = []
    with open('SJM.txt', mode="r") as lista_pc:
        pokaz_liste = lista_pc.readlines()
    for lines in pokaz_liste:
        dlugosc_nazw = lines.find("SJM")+3
        tablica_zmiennych.append(lines[0:dlugosc_nazw])
    return tablica_zmiennych


if __name__ == "__main__":
    co_zrobic = input("Co zrobic? copy czy install ")
    if co_zrobic == 'copy':
        print('rozpoczęto kopiowanie')
        main2()
    elif co_zrobic == 'install':
        print("rozpoczeto instalacje")
        main()
        time.sleep(60)
    #print(main(sys.argv[1:]))
    #tablica = pobierzlsite_pc()
    #print(tablica)
    os.path.exists()