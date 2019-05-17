import identification
import argparse


connection = identification.Connection()
liste_data = connection.recup_data()


if not liste_data[0] :
  print(liste_data[1])
else :
  for i in liste_data[1] :
    print(i)

