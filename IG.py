import tkinter
from tkinter import messagebox
#les 2 vars de l'alerte recup les résultats de entries


#à remplir plus tard
def valider() :
  nom  = str(entry_nom.get())
  mdp = str(entry_mdp.get())
  messagebox.showinfo("Valider", "Confirmez-vous ceci ?\n\n nom = {},\nmot de passe = {}. ".format(nom,mdp))
  fenetre.destroy()

#CSS
titel_font = "times 24 bold"
entry_font = "times 20 italic"
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
entry_nom = tkinter.Entry(frame_principal, textvariable = "", width = 15, font = entry_font )
entry_nom.pack(padx = 1, pady = 2)

#2e entry
entry_mdp = tkinter.Entry(frame_principal, textvariable = "", width = 15, font = entry_font, show = "*"  )
entry_mdp.pack(padx = 2, pady = 2)

#bouton
button_valider = tkinter.Button(frame_principal, cursor = "dotbox", text = "Valider", command=valider, width = 30, font = button_font)
button_valider.pack(padx = 1, pady = 3)

fenetre.mainloop()
