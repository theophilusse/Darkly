Brute Force Login
=================

URL vulnérable :

http://IP_DARKLY/index.php?page=signin

Description :

La page de connexion autorise des tentatives répétées contre un compte
connu, ici le compte "admin". Le mot de passe utilisé par ce compte est
également présent dans les listes de mots de passe très courants.

Une attaque par brute force consiste à essayer automatiquement plusieurs
mots de passe jusqu'à ce que la réponse du serveur indique une connexion
réussie.

Exploitation :

Le fichier passwords.txt contient une courte liste de mots de passe
courants. Le script bruteforce.sh lit cette liste ligne par ligne.

Pour chaque mot de passe, il envoie avec curl une requête HTTP GET vers :

/index.php?page=signin

avec les paramètres suivants :

username=admin
password=mot_de_passe_testé
Login=Login

Le script analyse ensuite la réponse et recherche la chaîne :

The flag is

Lorsque cette chaîne apparaît, l'authentification a réussi. Le mot de
passe découvert est :

admin:shadow

Commande de reproduction :

./Resources/bruteforce.sh http://IP_DARKLY

Impact :

- Compromission d'un compte utilisateur ou administrateur ;
- accès à des fonctionnalités et données privées ;
- modification ou suppression de données ;
- réutilisation possible du même mot de passe sur d'autres services.

Correction :

- Utiliser un mot de passe long, unique et non présent dans les listes
  de mots de passe courants ;
- limiter le nombre de tentatives par compte et par adresse IP ;
- ajouter un délai progressif après les échecs ;
- bloquer temporairement le compte après plusieurs tentatives ;
- journaliser et détecter les essais répétés ;
- utiliser une authentification multifacteur.

OWASP :

A07 - Identification and Authentication Failures

À retenir :

La vulnérabilité ne vient pas du script lui-même. Elle vient de la
combinaison d'un mot de passe faible et d'une protection insuffisante
contre les tentatives répétées.
