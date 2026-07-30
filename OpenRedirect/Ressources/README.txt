URL vulnérable : http://192.168.56.101/index.php?page=redirect&site=xxx

Le paramètre "site" est utilisé pour rediriger l'utilisateur vers des sites
externes (Facebook, Twitter, Instagram) depuis les icônes du footer.

Le serveur ne valide pas la valeur du paramètre "site" et redirige vers
n'importe quelle URL fournie, y compris des sites malveillants.

Exploitation :
  ?page=redirect&site=https://evil.com
  → redirige la victime vers un site contrôlé par l'attaquant

Impact :
  - Phishing : l'URL de départ est légitime (192.168.56.101), la victime
    fait confiance au lien avant d'être redirigée
  - Contournement de filtres basés sur le domaine source

Correction :
  - Utiliser une whitelist des redirections autorisées
  - Ou remplacer le paramètre par un identifiant (ex: site=1 → facebook.com)

OWASP : Unvalidated Redirects and Forwards