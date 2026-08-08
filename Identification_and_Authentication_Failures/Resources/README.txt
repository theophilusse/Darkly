Hidden Page - User-Agent & Referer Spoofing
============================================

URL vulnérable : http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

Cette page est accessible via le lien "© BornToSec" dans le footer.
Elle contient des indices cachés dans des commentaires HTML :

  <!-- You must come from : "https://www.nsa.gov/". -->
  <!-- Let's use this browser : "ft_bornToSec". It will help you a lot. -->

Le serveur vérifie les headers HTTP Referer et User-Agent pour
autoriser l'accès au flag. Ces headers sont entièrement contrôlés
par le client et ne constituent pas une mesure de sécurité fiable.

Exploitation :
  curl -s "http://192.168.56.101/?page=b7e44c7a..." \
       -H "Referer: https://www.nsa.gov/" \
       -H "User-Agent: ft_bornToSec"

Impact :
  - N'importe qui peut spoofer ces headers trivialement
  - Les indices étaient visibles en clair dans le HTML source

Correction :
  - Ne jamais baser une autorisation sur des headers client
  - Les headers Referer et User-Agent sont modifiables par n'importe qui
  - Utiliser une authentification côté serveur (session, token)

OWASP : A07 - Identification and Authentication Failures