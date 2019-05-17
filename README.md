# vote_electronique(Python)

Bonjour à tous, 

Ce projet est une sorte de mise en pratique de technologies récemment apprises (avril 2019). Il a pour but d'utiliser mais aussi 
de combiner ces technologies dans une situation utra simplifiée. J'ai essayé d'utiliser la POO en python mon code essaye de décomposer chaque tâche en une fonction pour faciliter le testing.

Il y a 5 fichiers : 
1/ app.py : c'est mon interface graphique, elle contrôle l'identité de l'utilisateur et fournit une réaction adaptée à ce contrôle.
    Elle emploie le module messagebox pour donner des feedbacks sous forme de popups, le module tkinter pour l'aspect graphique, 
    le module identification pour l'interaction avec la bdd. 
2/ identification.py : c'est mon module qui interagit avec ma bdd. Il se compose de deux classes : 
    1/ connection (établit la connection avec la base)
    2/ user(connection) héritant de connection il fournit les fonctions de classes nécessaires à app.py
3/ db_vote_electro.sql : c'est le créateur de ma base de données. Celle-ci est très simple car elle se compose de 4 colonnes 
    (id, pseudo, mdp, vote). L'emploie de Mysql n'est pas ici la priorité. Il y a cependant une procédure pour éviter d'écrire 
    trop de code mysql dans identification.py. 
4/ recup_data.py : c'est un module qui permet à l'administrateur d'avoir accès aux résultats du vote. Je veux rajouter des options 
à ce fichier via argparse.
5/ test_identification.py : il test que les fonctions du module identification.py communiquent bien entre elles.

Le projet est actuellement inachevé car je dois finir recup_data et je veux rajouter une page de code pour le testing de app.py. 

blingstand(blingstand@hotmail.fr)
 
