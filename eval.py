# pip install GitPython
# import git
# from git import Repo
import getpass
import os
import paramiko
import nmap

# -----------------------------------------------------
#  Telecharger vulmap-linux
# ------------------------------------------------------


workspace = "./"
os.system("clear")
os.chdir(workspace)

# checker si le dossier exist

if not os.path.exists("Vulmap"):
    print("\nTelechargement de vulmap ..\n")
    os.system("git clone https://github.com/vulmon/Vulmap.git")
    #Repo.clone_from("https://github.com/vulmon/Vulmap.git", "./")
    #git.Git("./").clone("https://github.com/vulmon/Vulmap.git") # ne marche pas sur docker
    
else:
    print("Vulmap est deja telechargee")

vulmapPath = workspace + "Vulmap/Vulmap-Linux/vulmap-linux.py"

# -------------------------------------------------------
# Saisie d'informations
# --------------------------------------------------------

print("\nconnexion a la machine cible via SSH \n")


hostname = input("Address IP > ")
username = input("UserName > ")
password = getpass.getpass()
source = vulmapPath
dest = input("Chemin de destination > ")
port = input("Port > ")  # shall be 22



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password)
print("\nConnection ssh reussie ..\n")

# ----------------------------------------------------
# transfert du fichier vers la machine cible
# ----------------------------------------------------

print("\nTransfert de donnees vers la machine cible\n")
if os.path.isfile(vulmapPath):
    ftp_client = ssh.open_sftp()
    ftp_client.put(vulmapPath, dest, callback=None, confirm=True)
    ftp_client.close()

print("\nTransfert de donnees reussie..\n")

# ----------------------------------------------------
# lancement du script vulmap sur la machine cible
# ----------------------------------------------------


print("\nLancement du script vulmap sur la machine cible\n")

comande = "python3 " + "-v " + dest

stdin, stdout, stderr = ssh.exec_command(comande)
stdin.close()
vulmapOutput = stdout.read().decode().strip()
print(vulmapOutput)

ssh.close()


# ----------------------------------------------------------
# scan de la machine avec NMAP pour les ports ouverts
# ----------------------------------------------------------

print("\nPort scaning on : {} ....\n".format(hostname))

nmScan = nmap.PortScanner()
scanResult = nmScan.scan(hostname, '21-22')  # ports entre 21 et 80
print("\nNmap scan finished ..\n")

# ----------------------------------------------------------
# exporter les resultats sur un fichiers text
# ----------------------------------------------------------

print("\nExport des resultats du scan..\n")

with open("output.txt", 'w') as f:
    f.write("\n==> resultat du scan via Vulmap : \n\n")
    f.write(str(vulmapOutput))
    f.write("\n\n==> resultat du scan via Nmap : \n\n")
    f.write(str(scanResult))

print("\nExportation Reussie..\n")

