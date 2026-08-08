Improper Input Validation - Survey
===================================

URL vulnérable : http://192.168.56.101/index.php?page=survey

Le formulaire de sondage propose des choix avec des valeurs numériques
contraintes côté client (ex: valeurs entre 1 et 10).

Ces contraintes ne sont pas vérifiées côté serveur.
En modifiant les valeurs du POST (valeurs négatives ou très grandes),
le serveur accepte et traite des données invalides, révélant le flag.

Exploitation :
  - Intercepter la requête POST avec Burp Suite ou DevTools
  - Modifier les valeurs numériques (ex: -1, 99999)
  - Soumettre la requête modifiée

Impact :
  - Corruption de données en base
  - Contournement de logique métier
  - Dans ce cas : accès au flag

Correction :
  - Toujours valider et sanitiser les entrées côté serveur
  - Ne jamais faire confiance aux données envoyées par le client

OWASP : A03 - Injection / Improper Input Validation