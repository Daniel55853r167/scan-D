import os
import subprocess
from termcolor import colored

# Arte ASCII
ART = """
░██████╗░█████╗░░█████╗░███╗░░██╗░░░░░░██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░██║░░░░░░██╔══██╗
╚█████╗░██║░░╚═╝███████║██╔██╗██║█████╗██║░░██║
░╚═══██╗██║░░██╗██╔══██║██║╚████║╚════╝██║░░██║
██████╔╝╚█████╔╝██║░░██║██║░╚███║░░░░░░██████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═════╝░
 TIkTOK Daniel55853R github Daniel55853R167
"""

# Función para imprimir arte ASCII en verde
def print_art():
    print(colored(ART, 'green'))

# Función para ejecutar el escaneo
def run_nmap_scan(targets, scan_args):
    command = f"nmap {scan_args} {targets}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

# Función para colorear el resultado del escaneo
def colorize_scan_result(scan_result):
    lines = scan_result.splitlines()
    colored_result = []
    
    for line in lines:
        if "open" in line:
            # Colorea puertos abiertos y servicios
            parts = line.split()
            if len(parts) >= 3:
                port = parts[0]
                service = parts[2]
                colored_line = line.replace(port, colored(port, 'green')).replace(service, colored(service, 'yellow'))
                colored_result.append(colored_line)
            else:
                colored_result.append(colored(line, 'green'))
        else:
            colored_result.append(line)
    
    return "\n".join(colored_result)

# Función para guardar el resultado en un archivo
def save_to_file(content, file_path):
    with open(file_path, "w") as f:
        f.write(content)
    print(colored(f"Resultados guardados en {file_path}", 'blue'))

# Función para mostrar el menú de opciones con colores
def show_menu():
    print(colored("\nSelecciona el tipo de escaneo:", 'cyan'))
    print(colored("1. Escaneo ruidoso (-T4 -A -p- --script=vuln)", 'magenta'))
    print(colored("2. Escaneo moderado (-T3 -A -p- --script=vuln)", 'magenta'))
    print(colored("3. Escaneo silencioso (-T2 -A -p- --script=vuln)", 'magenta'))
    print(colored("4. Escaneo rápido (-T5 -F)", 'magenta'))
    print(colored("5. Escaneo de versión (-sV)", 'magenta'))
    print(colored("6. Escaneo de sistema operativo (-O)", 'magenta'))
    print(colored("7. Escaneo con scripts NSE (--script=all)", 'magenta'))
    print(colored("8. Escaneo de puertos específicos (-p 22,80,443)", 'magenta'))
    print(colored("9. Escaneo agresivo (-A)", 'magenta'))
    print(colored("10. Escaneo en modo sin estado (-sP)", 'magenta'))
    print(colored("11. Escaneo de red (-sn)", 'magenta'))
    print(colored("12. Escaneo de puertos en rango (-p 1-1000)", 'magenta'))
    print(colored("13. Escaneo en paralelo (-T4)", 'magenta'))
    print(colored("14. Escaneo sin resolver nombres (-n)", 'magenta'))
    print(colored("15. Escaneo con tiempo de espera largo (-T1)", 'magenta'))
    print(colored("0. Salir", 'red'))

# Función para obtener la entrada del usuario
def get_user_input():
    show_menu()
    choice = input("Ingrese el número del tipo de escaneo: ")

    scan_options = {
        '1': "-T4 -A -p- --script=vuln",
        '2': "-T3 -A -p- --script=vuln",
        '3': "-T2 -A -p- --script=vuln",
        '4': "-T5 -F",
        '5': "-sV",
        '6': "-O",
        '7': "--script=all",
        '8': "-p 22,80,443",
        '9': "-A",
        '10': "-sP",
        '11': "-sn",
        '12': "-p 1-1000",
        '13': "-T4",
        '14': "-n",
        '15': "-T1"
    }

    scan_args = scan_options.get(choice, "-T4 -A -p- --script=vuln")
    targets = input("Ingrese la IP o dominio a escanear: ")
    
    return targets, scan_args

# Función principal
def main():
    while True:
        print_art()
        
        # Obtener entrada del usuario
        targets, scan_args = get_user_input()

        # Ejecutar escaneo
        print(colored(f"Ejecutando escaneo con argumentos: {scan_args}...", 'yellow'))
        scan_result = run_nmap_scan(targets, scan_args)
        
        # Mostrar resultado en la terminal con colores
        colored_result = colorize_scan_result(scan_result)
        print(colored("Resultados del escaneo:", 'green'))
        print(colored_result)

        # Preguntar si el usuario quiere guardar el resultado
        save_option = input(colored("¿Desea guardar el resultado en un archivo de texto en el escritorio? (y/n): ", 'cyan'))
        if save_option.lower() == 'y':
            desktop_path = os.path.expanduser("~/Desktop")
            file_path = os.path.join(desktop_path, "scan_result.txt")
            save_to_file(scan_result, file_path)

        # Mostrar información de contacto y aviso legal
        print(colored("\nTikTok: @Daniel55853R", 'yellow'))
        print(colored("GitHub: https://github.com/Daniel55853R167", 'yellow'))
        print(colored("El creador no se hace responsable del uso de la herramienta.", 'red'))

        # Preguntar si el usuario desea volver al menú
        exit_option = input(colored("\n¿Desea volver al menú principal? (y/n): ", 'cyan'))
        if exit_option.lower() != 'y':
            print(colored("Saliendo del programa. ¡Hasta luego!", 'blue'))
            break

if __name__ == "__main__":
    main()
