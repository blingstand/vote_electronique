# vote_electronique(Python)

Bonjour à tous, 

Ce projet est une sorte de mise en pratique de technologies récemment apprises (avril 2019). Il a pour but d'utiliser mais aussi 
de combiner ces technologies dans une situation utra simplifiée. J'ai essayé d'utiliser la POO en python.

Il y a 3 fichiers : 
- app.py : c'est mon interface graphique, elle contrôle l'identité de l'utilisateur et fournit une réaction adaptée à ce contrôle.
    Elle emploie le module messagebox pour donner des feedbacks sous forme de popups, le module tkinter pour l'aspect graphique, 
    le module identification pour l'interaction avec la bdd. 
- identification.py : c'est mon module qui interagit avec ma bdd. Il se compose de deux classes : 
    1/ connection (établit la connection avec la base)
    2/ user(connection) héritant de connection il fournit les fonctions de classes nécessaires à app.py
- db_vote_electro.sql : c'est le créateur de ma base de données. Celle-ci est très simple car elle se compose de 4 colonnes 
    (id, pseudo, mdp, vote). L'emploie de Mysql n'est pas ici la priorité. Il y a cependant une procédure pour éviter d'écrire 
    trop de code mysql dans identification.py. 
    
Le projet est actuellement inachevé car je veux rajouter une page de code pour le testing. 

blingstand(blingstand@hotmail.fr)
 
