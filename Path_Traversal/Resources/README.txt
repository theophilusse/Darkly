Path Traversal / Local File Inclusion
=====================================

URL vulnérable :

http://IP_DARKLY/index.php?page=...

Description :

L'application utilise le paramètre "page" afin de choisir la page ou le
fichier à charger. Cette valeur est contrôlée par l'utilisateur et le
serveur ne vérifie pas correctement que le chemin reste dans le dossier
autorisé du site.

Sous Unix et Linux, la séquence "../" signifie remonter d'un niveau dans
l'arborescence. En la répétant, il est possible de sortir du répertoire
prévu par l'application.

Exploitation :

Le chemin utilisé est :

../../../../../../../etc/passwd

URL complète :

http://IP_DARKLY/index.php?page=../../../../../../../etc/passwd

Le fichier /etc/passwd existe sur les systèmes Unix/Linux et contient des
informations sur les comptes locaux. Il est couramment utilisé pour
prouver une faille de path traversal.

Commande de reproduction :

./Resources/exploit.sh http://IP_DARKLY

Le serveur suit le chemin fourni par l'utilisateur, atteint le fichier
/etc/passwd et affiche le flag du challenge.

Impact :

- Lecture de fichiers hors du répertoire web prévu ;
- divulgation de code source et de fichiers de configuration ;
- fuite possible de credentials, tokens, clés ou journaux ;
- divulgation d'informations sur le système.

Correction :

- Ne jamais utiliser directement une entrée utilisateur comme chemin ;
- utiliser une whitelist de pages autorisées ;
- associer des identifiants fixes à des fichiers connus ;
- normaliser le chemin et vérifier qu'il reste dans le répertoire prévu ;
- stocker les fichiers sensibles hors de la racine web ;
- appliquer des permissions strictes au niveau du système de fichiers.

OWASP :

A01 - Broken Access Control
Path Traversal / Local File Inclusion

À retenir :

Le paramètre "page" permettait de sortir du dossier autorisé grâce à
"../" et de demander un fichier présent sur le serveur.
