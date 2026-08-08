Stored XSS - Page Feedback
==========================

URL vulnérable :

http://IP_DARKLY/index.php?page=feedback

Description :

La page Feedback permet à un utilisateur d'envoyer un nom et un message.
Ces données sont enregistrées dans une base de données puis relues afin
d'être affichées sur la page.

Une XSS stockée apparaît lorsqu'une entrée dangereuse est enregistrée par
le serveur puis réinjectée dans une page HTML sans encodage ou filtrage
correct. Elle peut alors affecter plusieurs visiteurs lors de consultations
ultérieures.

Exploitation du challenge :

Les valeurs suivantes sont envoyées :

Name: test
Message: script

Commande de reproduction :

./Resources/exploit.sh http://IP_DARKLY

Dans cette version pédagogique de Darkly, la présence du mot "script" ou
"alert" dans un feedback stocké déclenche le flag.

Point important :

Le simple mot "script" n'exécute pas du JavaScript. Il sert ici de marqueur
spécifique au challenge. La vulnérabilité représentée est le traitement
insuffisant de données utilisateur persistantes susceptibles d'être
réinjectées dans une page.

Différence avec la XSS de la page Media :

- Media : le payload est fourni dans l'URL et traité dans la requête
  courante ;
- Feedback : la donnée est enregistrée puis réaffichée plus tard.

Impact d'une véritable XSS stockée :

- Exécution persistante de JavaScript chez les visiteurs ;
- vol potentiel de sessions lorsque les cookies sont mal protégés ;
- actions exécutées avec les droits d'une victime ;
- modification de la page ou affichage d'un faux formulaire ;
- phishing et redirection vers un site malveillant ;
- attaque possible d'un administrateur consultant les feedbacks.

Correction :

- Encoder les données avant de les afficher, par exemple avec
  htmlspecialchars en PHP ;
- traiter les feedbacks comme du texte et non comme du HTML ;
- effectuer les validations côté serveur ;
- ne pas se reposer sur une blacklist de mots comme "script" ;
- utiliser une bibliothèque de sanitisation reconnue si du HTML doit être
  autorisé ;
- ajouter une Content Security Policy ;
- protéger les cookies avec HttpOnly, Secure et SameSite.

Exemple PHP :

echo htmlspecialchars($feedback, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');

OWASP :

Cross-Site Scripting - Stored XSS

À retenir :

Une donnée contrôlée par l'utilisateur est stockée puis réutilisée. La
protection correcte consiste principalement à encoder la sortie selon son
contexte, et non à essayer de bloquer quelques mots particuliers.
