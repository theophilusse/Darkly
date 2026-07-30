Sensitive Data Exposure - htpasswd
====================================

URL vulnérable : http://192.168.56.101/whatever/htpasswd

Le fichier htpasswd contenant les credentials de l'administrateur
est accessible publiquement sans aucune authentification.

Contenu exposé :
  root:437394baff5aa33daa618be47b75cb49 (hash MD5) -> qwerty123@

Exploitation :
  1. Accéder à http://192.168.56.101/whatever/htpasswd
  2. Récupérer le hash MD5 du mot de passe
  3. Cracker le hash via crackstation.net ou hashcat
  4. Utiliser les credentials sur /admin/index.php

Impact :
  - Accès complet à l'interface d'administration
  - Compromission totale du site

Correction :
  - Ne jamais exposer les fichiers htpasswd publiquement
  - Placer les fichiers sensibles hors de la racine web
  - Utiliser des algorithmes de hashage sécurisés (bcrypt, argon2)
    et non MD5 qui est cracké en quelques secondes

OWASP : A02 - Cryptographic Failures / Sensitive Data Exposure

Admin Panel Access
===================

URL vulnérable : http://192.168.56.101/admin/index.php

Accès obtenu grâce aux credentials récupérés dans /whatever/htpasswd.
Le panneau d'administration n'a pas de protection supplémentaire
(2FA, IP whitelist, rate limiting).

OWASP : A07 - Identification and Authentication Failures