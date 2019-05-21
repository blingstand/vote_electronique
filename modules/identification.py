import mysql.connector

"""
Remarque(s) :
  1/ J'avais mis auparavant req1 en fonction privée car je trouvais ça logique, seule la fonction verif_idtf()
  y faisait appel. Cependant je l'ai mise ensuite publique quand j'ai fait mon module test_identification car je
  n'ai pas su comment tester une fonction privée et même si c'était logique.

"""


liste_euro = ("Abstention", "l'Union Populaire Républicaine", "la France Insoumise", "les Républicains", "Debout la France", "Le Rassemblement National", "Place Publique - Parti Socialiste", "Europe Ecologie les Verts", "La République en Marche", "Le Parti Communiste", "l'Union des Démocrates Indépendants", "Génération.s", "les Patriotes" )

def deco_recup_data(func):
  """ Il donne à la fonction recup data un texte présentatif avec des retours à la ligne  """
  def inner(*args, **kwargs):
    try :
      resultat =  func(*args, **kwargs)
      result_print = []
      for i in resultat :
        result_print.append("Vote pour {} -> {} votant(s).".format(liste_euro[i[0]], i[1]))
      return True, result_print
    except :
      return False, "Erreur dans la requête sql"
  return inner

class Connection() :

  def __init__(self):
    self.mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "123",
      database = "conn_python"
      )
    self.my_cursor = self.mydb.cursor()


  @deco_recup_data
  def recup_data(self):
    """
    Cette fonction récupère le nombre de votant pour chaque vote
    """
    try :
      sql = "CALL compteur_vote();"
      self.my_cursor.execute(sql)
      resultat = self.my_cursor.fetchall()
      return resultat
    except Error as error:
      pass


class User(Connection):
  """docstring for user"""
  def __init__(self, pseudo, mdp):
    super().__init__()
    self.pseudo = pseudo
    self.mdp = mdp


  def req1(self):
    try :
      sql = "SELECT mdp FROM vote_electro WHERE pseudo = '{}'".format(self.pseudo)
      self.my_cursor.execute(sql)
      resultat = self.my_cursor.fetchone()
      return resultat
    except Exception as e :
      raise e

  def req2(self):
    try :
      sql2 = "SELECT mdp FROM vote_electro WHERE pseudo = '{}'".format(self.pseudo)
      self.my_cursor.execute(sql2)
      resultat = self.my_cursor.fetchone()
      return resultat
    except Exception as e :
      raise e

  def verif_idtf(self):
    """
    vérifie la bdd pour vérifier la présence de cet utilisateur
    """
    resultat1 = self.req1()
    if resultat1 :
      resultat2 = self.req2()
      if str(resultat2[0]) == self.mdp :
        return True

  def envoie_vote(self, vote):

    try :
      sql = "UPDATE vote_electro SET vote = {} WHERE pseudo = '{}'".format(vote, self.pseudo)
      self.my_cursor.execute(sql)
      self.mydb.commit()
      print(self.my_cursor.rowcount, " ligne(s) ajoutée(s) avec succès ! ")
      return True

    except Exception as e :
      raise e
      return False



