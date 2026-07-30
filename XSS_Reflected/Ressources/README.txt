XSS Reflected - Media Page
============================

URL vulnérable : http://192.168.56.101/index.php?page=media&src=PAYLOAD

Le paramètre "src" est injecté directement dans l'attribut data
d'une balise <object> sans sanitisation :
  <object data="VALEUR_SRC"></object>

Exploitation :
  ?page=media&src=data:text/html,<script>alert(1)</script>

Impact :
  - Vol de cookies de session via lien piégé envoyé à une victime
  - Exécution de code JS dans le contexte du site

Correction :
  - Échapper les caractères spéciaux avec htmlspecialchars()
  - Valider que src est une URL/chemin image valide

OWASP : A03 - Cross-Site Scripting (XSS) Reflected