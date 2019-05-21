# vote_electronique(Python/MySQL)

Bonjour à tous, 

Ce projet est une sorte de mise en pratique de technologies récemment apprises (avril-mai 2019). Il a pour but d'utiliser mais aussi 
de combiner ces technologies dans une situation utra simplifiée. J'ai essayé d'utiliser la POO en python mon code essaye de décomposer chaque tâche en une fonction pour faciliter le testing.

Il y a 5 fichiers :
1/ main.py : il lance le programme en fonction du choix avec argparse fait par l'utilisateur.
2/ app.py : c'est mon interface graphique, elle contrôle l'identité de l'utilisateur et fournit une réaction adaptée à ce contrôle.
    Elle emploie le module messagebox pour donner des feedbacks sous forme de popups, le module tkinter pour l'aspect graphique, 
    le module identification pour l'interaction avec la bdd. 
3/ identification.py : c'est mon module qui interagit avec ma bdd. Il se compose de deux classes : 
    1/ connection (établit la connection avec la base)
    2/ user(connection) héritant de connection il fournit les fonctions de classes nécessaires à app.py
4/ db_vote_electro.sql : c'est le créateur de ma base de données. Celle-ci est très simple car elle se compose de 4 colonnes 
    (id, pseudo, mdp, vote). L'emploie de Mysql n'est pas ici la priorité. Il y a cependant une procédure pour éviter d'écrire 
    trop de code mysql dans identification.py. 
5/ test_identification.py : il test que les fonctions du module identification.py communiquent bien entre elles.

Le projet sera inachevé quand j'aurai régler les problèmes de test_identification.py. 

blingstand(blingstand@hotmail.fr)
 
