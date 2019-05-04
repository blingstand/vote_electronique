import tkinter
from tkinter import messagebox

#message guide sur entries, s'effaçant au clic

#à remplir plus tard
def valider() :
  pseudo  = str(entry_pseudo.get())
  mdp = str(entry_mdp.get())
  messagebox.showinfo("Valider", "Confirmez-vous ceci ?\n\n pseudo = {},\nmot de passe = {}. ".format(pseudo,mdp))
  fenetre.destroy()

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
entry_pseudo.pack(padx = 1, pady = 2)

#2e entry
entry_mdp = tkinter.Entry(frame_principal, width = 25, font = entry_font )
entry_mdp.insert(0, "Entrez votre mot de passe ...")
entry_mdp.pack(padx = 2, pady = 2)

#bouton
button_valider = tkinter.Button(frame_principal, cursor = "dotbox", text = "Valider", command=valider, width = 30, font = button_font)
button_valider.pack(padx = 1, pady = 3)

fenetre.mainloop()
