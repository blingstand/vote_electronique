import tkinter
from tkinter import messagebox

#1er messbox explication


def valider() :
  pseudo = str(entry_pseudo.get())
  mdp = str(entry_mdp.get())
  messagebox.askokcancel("Valider", "Je vérifie vos identifiants")
  fenetre.destroy()

couleur_champ_entry = "#fff0b3"
def clean_entry_pseudo(event):
  if str(entry_pseudo.get()) == "Entrez votre pseudo ..." :
    entry_pseudo.delete(0, "end")
    entry_pseudo.insert(0, "")
  entry_pseudo.config(bg = couleur_champ_entry)

def clean_entry_mdp(event):
  if str(entry_mdp.get()) == "Entrez votre mot de passe ..." :
    entry_mdp.delete(0, "end")
    entry_mdp.insert(0, "")
    entry_mdp.config(show = "*")
  entry_mdp.config(bg = couleur_champ_entry)

def focusout_mdp(event):
  entry_mdp.config(bg = "white")
  if str(entry_mdp.get()) == "" :
    entry_mdp.insert(0, "Entrez votre mot de passe ...")
    entry_mdp.config(show = "")

def focusout_pseudo(event):
  entry_pseudo.config(bg = "white")
  if str(entry_pseudo.get()) == "" :
    entry_pseudo.insert(0, "Entrez votre mot de passe ...")

#CSS
titel_font = "times 24 bold"
entry_font = "times 15 italic"
button_font = "times 20 bold"


fenetre = tkinter.Tk()
fenetre.geometry("800x400")
fenetre.title("Vote électronique")

frame_principal = tkinter.Frame(fenetre, width=780, height=380, borderwidth=10, background='grey')
frame_principal.pack()

#text
label_titel = tkinter.Label(frame_principal, text = "Identification", font = titel_font)
label_titel.pack(padx = 1, pady = 1 )

#1ere entry
entry_pseudo = tkinter.Entry(frame_principal, textvariable = "", width = 25, font = entry_font )
entry_pseudo.insert(0, "Entrez votre pseudo ...")
entry_pseudo.focus_set()
entry_pseudo.bind("<Key>", clean_entry_pseudo)
entry_pseudo.bind("<FocusOut>", focusout_pseudo)
entry_pseudo.pack(padx = 1, pady = 2)

#2e entry
entry_mdp = tkinter.Entry(frame_principal, width = 25, font = entry_font )
entry_mdp.insert(0, "Entrez votre mot de passe ...")
entry_mdp.focus_set()
entry_mdp.bind("<Key>", clean_entry_mdp)
entry_mdp.bind("<FocusOut>", focusout_mdp)
entry_mdp.pack(padx = 2, pady = 2)

#bouton
button_valider = tkinter.Button(frame_principal, cursor = "dotbox", text = "Valider", command=valider, width = 30, font = button_font)
button_valider.pack(padx = 1, pady = 3)

fenetre.mainloop()
