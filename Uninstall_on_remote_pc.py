import subprocess

pc_name = "pc470spn" #input("Podaj nazwe pc do połącznia ")
"""command_return = subprocess.run(["powershell", "-Command", "Get-WmiObject Win32_Product -ComputerName ", pc_name, " | Select-Object -Property IdentifyingNumber, Name"], capture_output=True)
print(command_return)"""
numer_programu = ["{A37CDB58-AAE8-0000-8C13-E0F7BACB0D5F}",
                  "{A37CDB58-AAE8-0001-8C13-E0F7BACB0D5F}",
                  "{ABE2F70B-8D94-44E9-AA04-F0DB35063D62}"]

for numer in numer_programu:
 subprocess.run(["powershell", "-Command", " (Get-WmiObject Win32_Product -ComputerName ", pc_name, " Where-Object {$_.IdentifyingNumber -eq ", numer,"}).Uninstall()"], shell=True)