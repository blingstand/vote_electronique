import mysql.connector

#fonction recup data

class Connection() :

  LISTE_EURO = ("l'Union Populaire Républicaine", "la France Insoumise", "les Républicains", "Debout la France", "Le Rassemblement National", "Place Publique - Parti Socialiste", "Europe Ecologie les Verts", "La République en Marche", "Le Parti Communiste", "l'Union des Démocrates Indépendants", "Génération.s", "les Patriotes" )

  def __init__(self):
    self.mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "123",
      database = "conn_python"
      )
    self.my_cursor = self.mydb.cursor()

  def recup_data(self, vote = "default"):
    """
    Cette fonction récupère le nombre de votant pour chaque vote
    """
    sql = "CALL compteur_vote();"
    self.my_cursor.execute(sql)
    my_result = self.my_cursor.fetchall()

    for i in my_result :
      print("Vote pour {} -> {} votant(s).".format(self.LISTE_EURO[i[0]-1], i[1]))


class User(Connection):
  """docstring for user"""
  def __init__(self, pseudo, mdp):
    super().__init__()
    self.pseudo = pseudo
    self.mdp = mdp


  def identification(self):
    """
    vérfifie la bdd pour vérifier la présence de cet utilisateur
    """

    sql = "SELECT mdp FROM vote_electro WHERE pseudo = '{}'".format(self.pseudo)
    self.my_cursor.execute(sql)
    my_result = self.my_cursor.fetchone()

    if my_result :
      sql2 = "SELECT mdp FROM vote_electro WHERE pseudo = '{}'".format(self.pseudo)
      self.my_cursor.execute(sql)
      my_result2 = self.my_cursor.fetchone()
      if str(my_result2[0]) == self.mdp :
        return True

  def envoie_vote(self, vote):
    sql = "UPDATE vote_electro SET vote = {} WHERE pseudo = '{}'".format(vote, self.pseudo)

    self.my_cursor.execute(sql)
    self.mydb.commit()
    print(self.my_cursor.rowcount, "record(s) affected")

    # except :
    #   print("Une erreur est survenue =(")


