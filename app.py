import tkinter as tk
from tkinter import messagebox
from time import sleep

#valider_euro()


class App(tk.Tk) :
  #mes "CSS"
  COULEUR_CHAMP_ENTRY = "#fff0b3"
  TITEL_FONT = "times 20 bold"
  ENTRY_FONT = "times 15"
  BUTTON_FONT = "times 20 bold"
  #espace identifiants
  PSEUDO_ATTENDU = "root"
  MDP_ATTENDU = "123"
  #Question
  QUESTION = "Pour qui voulez-vous voter le 25 mai 2019 ? "
  #liste
  LISTE_EURO = ("l'Union Populaire Républicaine", "la France Insoumise", "les Républicains", "Debout la France", "Le Rassemblement National", "Place Publique - Parti Socialiste", "Europe Ecologie les Verts", "La République en Marche", "Le Parti Communiste", "l'Union des Démocrates Indépendants", "Génération.s", "les Patriotes" )

  def __init__(self):
    """
    initie la fen principale (self)
    """
    tk.Tk.__init__(self)
    self.geometry("600x300")
    self.title("Vote électronique")
    self.compoFen1()
    self.mainloop()

  def compoFen1(self):
    """
    Crée les composants de la première fenêtre
    """

    #text
    self.label_titel = tk.Label(self, text = "Identification", font = self.TITEL_FONT)
    self.label_titel.place(x = 220, y= 20 )

    #1ere entry
    self.entry_pseudo = tk.Entry(self, textvariable = "", width = 25, font = self.ENTRY_FONT, justify ="center")
    self.entry_pseudo.insert(0, "Entrez votre pseudo ...")
    self.entry_pseudo.bind("<Button-1>", self.clean_entry_pseudo)
    self.entry_pseudo.bind("<FocusOut>", self.focusout_pseudo)
    self.entry_pseudo.place(x = 180, y= 100 )

    #2e entry
    self.entry_mdp = tk.Entry(self, width = 25, font = self.ENTRY_FONT, justify ="center" )
    self.entry_mdp.insert(0, "Entrez votre mot de passe ...")
    self.entry_mdp.bind("<Button-1>", self.clean_entry_mdp)
    self.entry_mdp.bind("<Key>", self.clean_entry_mdp)
    self.entry_mdp.bind("<FocusOut>", self.focusout_mdp)
    self.entry_mdp.place(x = 180, y= 140 )

    #bouton
    self.button_valider = tk.Button(self, cursor = "dotbox", text = "Valider", command= self.valider, width = 30, font = self.BUTTON_FONT)
    self.button_valider.place(x = 55, y= 200 )

  def compoFen2(self):

    #text
    self.label_titel = tk.Label(self, text = self.QUESTION, font = self.TITEL_FONT, bg = "grey")
    self.label_titel.place(x = 35, y= 30 )

    #spinbox
    self.spinb_euro = tk.Spinbox(self, value=self.LISTE_EURO, justify = "center", wrap = True, width = 50, font = self.ENTRY_FONT)
    self.spinb_euro.place(x=40, y = 130)

    #bouton
    self.button_valider_euro = tk.Button(self, cursor = "dotbox", text = "Valider", command= self.valider_euro, width = 30, font = self.BUTTON_FONT)
    self.button_valider_euro.place(x=50, y = 200)


    # self.liste_partis.pack()

  def destComposants(self, liste):
    """
    détruit les composant de la deuxième fenêtre
    """
    for i in liste :
      i.destroy()

  def valider_euro(self):
    """
    valide le choix de la spinbox (spinb_euro), envoie au serveur les données, remercie et ferme
    """
    print(str(self.spinb_euro.get()))
    #rajouter ici l'écriture dans la bdd
    self.destComposants([self.spinb_euro, self.button_valider_euro])

    self.label_titel.config(text="Merci de votre participation")
    self.label_titel.place(x = 140, y = 130)
    self.update()
    sleep(2) #2 sec de merci et on ferme
    self.destroy()

  def valider(self) :
    """
    Vérifie les identifiants lorsque je clique sur le bouton Valider
    """
    messagebox.showinfo("Valider", "Je vérifie vos identifiants")
    if str(self.entry_pseudo.get()) == self.PSEUDO_ATTENDU and str(self.entry_mdp.get()) == self.MDP_ATTENDU :
      messagebox.showinfo("Info","Identification réussie ! ")
      self.destComposants([self.label_titel, self.entry_pseudo, self.entry_mdp, self.button_valider])
      self.compoFen2()
    else :
      rep = messagebox.askretrycancel("Erreur", "Recommencez ou quittez.")
      if not rep :
        self.destroy()
      else :
        self.entry_pseudo.delete(0, "end")
        self.entry_pseudo.insert(0, "Entrez votre pseudo ...")
        self.entry_mdp.delete(0, "end")
        self.entry_mdp.insert(0, "Entrez votre mot de passe ...")
        self.entry_mdp.config(show = "")

  def clean_entry_pseudo(self, event):
    """
    Efface le texte de entry_pseudo pour simuler un placeholder, change le bg
    """
    if str(self.entry_pseudo.get()) == "Entrez votre pseudo ..." :
      self.entry_pseudo.delete(0, "end")
      self.entry_pseudo.insert(0, "")
    self.entry_pseudo.config(bg = self.COULEUR_CHAMP_ENTRY)

  def clean_entry_mdp(self, event):
    """
    Efface le texte de entry_mdp pour simuler un placeholder, change le bg
    """
    if str(self.entry_mdp.get()) == "Entrez votre mot de passe ..." :
      self.entry_mdp.delete(0, "end")
      self.entry_mdp.insert(0, "")
      self.entry_mdp.config(show = "*") #cache ce qui est marqué
    self.entry_mdp.config(bg = self.COULEUR_CHAMP_ENTRY)

  def focusout_mdp(self, event):
    """
    Remet le texte de entry_mdp pour simuler un placeholder, change le bg
    """
    self.entry_mdp.config(bg = "white")
    if str(self.entry_mdp.get()) == "" :
      self.entry_mdp.insert(0, "Entrez votre mot de passe ...")
      self.entry_mdp.config(show = "")

  def focusout_pseudo(self, event):
    """
    Remet le texte de entry_pseudo pour simuler un placeholder, change le bg
    """
    self.entry_pseudo.config(bg = "white")
    if str(self.entry_pseudo.get()) == "" :
      self.entry_pseudo.insert(0, "Entrez votre pseudo ...")

def main():

  a = App()

if __name__ == "__main__":
  main()
