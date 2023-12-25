from os import system
import time
import sys
import platform
import colorama
from colorama import Fore, init, Style
import win32ui
import requests
import subprocess


mytitle = "Eno's Universal ADBlock Script v1.0"
CUSTOM_HOSTS_FILE = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
ORIGINAL_HOSTS_FILE = "https://pastebin.com/raw/DHxjqw3G"
REQUIRMENTS_FILE = "https://pastebin.com/raw/E7EG59SG"
FILE = "C:\\Windows\\System32\\drivers\\etc\\hosts"


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        

def install_hosts():
    try:
        # Daten von der URL herunterladen
        response = requests.get(CUSTOM_HOSTS_FILE)
        response.raise_for_status()  # Überprüfen auf Fehler

        # Inhalt der neuen hosts-Datei
        new_data = response.text

        # Die bestehende hosts-Datei überschreiben
        with open(FILE, 'w') as file:
            file.write(new_data)

        win32ui.MessageBox("Successfully installed the Universal ADBlock Script!\nThank you for using this script!", f"{mytitle}")
        time.sleep(3)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(2)
        sys.exit()


def uninstall_hosts():
    try:
        # Daten von der Original-URL herunterladen
        response = requests.get(ORIGINAL_HOSTS_FILE)
        response.raise_for_status()  # Überprüfen auf Fehler

        # Inhalt der Original-Hosts-Datei
        original_data = response.text

        # Die bestehende hosts-Datei überschreiben
        with open(FILE, 'w') as file:
            file.write(original_data)

        win32ui.MessageBox("Successfully uninstalled the Universal ADBlock Script!\nThank you for using this script!", f"{mytitle}")
        time.sleep(3)
        main()

    except requests.RequestException as e:
        win32ui.MessageBox(f"Error:\n{e}", f"{mytitle}")
        time.sleep(2)
        sys.exit()


def exit_script():
    system("cls")
    win32ui.MessageBox(f"Exiting... Thank you for using this script!", f"{mytitle}")
    time.sleep(2)
    sys.exit()


def install_requirements():
    try:
        # Anforderungen von der Pastebin-RAW-URL abrufen
        response = requests.get(REQUIRMENTS_FILE)
        response.raise_for_status()

        # Inhalt der requirements.txt
        requirements_data = response.text

        # requirements.txt temporär speichern
        with open("temp_requirements.txt", "w") as temp_file:
            temp_file.write(requirements_data)

        # Installiere die erforderlichen Pakete
        subprocess.check_call(["pip", "install", "-r", "temp_requirements.txt"])

        # Lösche temporäre requirements.txt
        subprocess.check_call(["del", "temp_requirements.txt"], shell=True)

        # Wenn die Installation erfolgreich ist, informiere den Benutzer
        system("cls")
        win32ui.MessageBox(f"Successfully installed the requirements!\nNow you can use this Script without Problems!", f"{mytitle}")
        time.sleep(2)
        main()

    except Exception as e:
        # Bei einem Fehler die Fehlermeldung anzeigen und das Skript beenden
        system("cls")
        win32ui.MessageBox(f"Error installing requirements:\n{e}", f"{mytitle}")
        time.sleep(2)
        sys.exit()


def main():
    system("title "+mytitle)
    os = platform.system()
    if os == "Windows":
        system("cls")
    else:
        system("clear")
        print(chr(27) + "[2J")
    print(f"""{Fore.CYAN}
──────────────────────────────────────────────────────────────────────────────────────────────

▓█████  ███▄    █  ▒█████    ██████      ██████  ▄████▄   ██▀███   ██▓ ██▓███  ▄▄▄█████▓
▓█   ▀  ██ ▀█   █ ▒██▒  ██▒▒██    ▒    ▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▓██▒▓██░  ██▒▓  ██▒ ▓▒
▒███   ▓██  ▀█ ██▒▒██░  ██▒░ ▓██▄      ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒ ▓██░ ▒░
▒▓█  ▄ ▓██▒  ▐▌██▒▒██   ██░  ▒   ██▒     ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▒██▄█▓▒ ▒░ ▓██▓ ░ 
░▒████▒▒██░   ▓██░░ ████▓▒░▒██████▒▒   ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒░██░▒██▒ ░  ░  ▒██▒ ░ 
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░  ▒ ░░   
 ░ ░  ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░   ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░ ▒ ░░▒ ░         ░    
   ░      ░   ░ ░ ░ ░ ░ ▒  ░  ░  ░     ░  ░  ░  ░          ░░   ░  ▒ ░░░         ░      
   ░  ░         ░     ░ ░        ░           ░  ░ ░         ░      ░                    
                                                ░                                       
──────────────────────────────────────────────────────────────────────────────────────────────
{Style.RESET_ALL}
                                {Fore.MAGENTA} > Developed by: 3n3scan{Style.RESET_ALL}
                                
{Fore.CYAN}> Choose an option:{Style.RESET_ALL}
{Fore.GREEN}> [1] Install Custom Hosts File{Style.RESET_ALL}
{Fore.RED}> [2] Uninstall Custom Hosts File{Style.RESET_ALL}
{Fore.CYAN}> [3] Install requirements{Style.RESET_ALL}
{Fore.YELLOW}> [4] Exit{Style.RESET_ALL}
""")
    choice = input(f"""{Fore.BLUE}
╭─({Fore.RED}root@3n3scan{Fore.BLUE})-[{Style.RESET_ALL}~{Fore.BLUE}]
╰─{Fore.RED}#{Fore.LIGHTGREEN_EX} Enter the number of your choice:{Style.RESET_ALL} """)


    if choice == "1":
        install_hosts()
    elif choice == "2":
        uninstall_hosts()
    elif choice == "3":
        install_requirements()
    elif choice == "4":
        exit_script()
    else:
        print(f"{Fore.RED}> Invalid choice. Please enter '{Fore.CYAN}1{Fore.RED}', '{Fore.CYAN}2{Fore.RED}', '{Fore.CYAN}3{Fore.RED}' '{Fore.CYAN}3{Fore.RED}' <{Style.RESET_ALL}")
        time.sleep(2)
        main()
        

if __name__ == "__main__":
    main()
