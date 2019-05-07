import mysql.connector

#fonction envoie_vote()

class User(object):
  """docstring for user"""
  def __init__(self, pseudo, mdp):
    self.pseudo = pseudo
    self.mdp = mdp
    self.mydb = mysql.connector.connect(
      host = "localhost",
      user = "root",
      passwd = "123",
      database = "conn_python"
      )
    self.my_cursor = self.mydb.cursor()

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
