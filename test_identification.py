#module qui test identification
import identification
import mysql.connector

class TestZone() :

  """j'initialise une instance connection et une autre user"""
  user = identification.User("adri", "123")
  connection = identification.Connection()

  def test_recup_data(self):
    """Je vérifie que recup data fournit bien un tuple composé d'un bool et d'un nombre positif (car qtt) """
    liste = self.connection.recup_data()
    assert isinstance(liste[0], bool) and len(liste[1]) > 0

  def test_req1(self) :
    """ Je vérifie que req1 ne retourne pas false """
    assert self.user.req1 != False

  def test_req2(self) :
    """ Je vérifie que req2 ne retourne pas false """
    assert self.user.req2 != False

  def test_verif_idtf(self):
    """ Je vérifie que verif_idtf renvoie bien un bool """
    resultat = self.user.verif_idtf()
    assert isinstance(resultat, bool)

  def test_envoie_vote(self):
    """ Je vérifie que verif_idtf fonctionne bien en renvoyant un True """
    resultat = self.user.envoie_vote(4)
    assert resultat == True
# test = TestZone()
# test.test_verif_idtf()
