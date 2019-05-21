"""lance l'application"""
import modules.app as app
import modules.identification as identification
import argparse

def parse_arguments():
    """Permet à l'utilisateur de choisir ce qu'il veut faire avec un parser"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--choix", type=int, help="""1/ voter,\n2/ consulter.""")
    args = parser.parse_args()
    choix = args.choix
    return choix


def recup_data():
    """sert à afficher la base de donnée"""

    connection = identification.Connection()
    liste_data = connection.recup_data()

    if not liste_data[0] :
      print(liste_data[1])
    else :
      for i in liste_data[1] :
        print(i)

def main():
    """Lancement du programme

        1/ l'utilisateur vote
        2/ il consulte la table
    """

    args = parse_arguments()
    if args ==  1:
        application = app.App()
    elif args == 2 :
        recup_data()

if __name__ == "__main__":
  main()

