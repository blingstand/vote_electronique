import tkinter

#à remplir plus tard
def valider() :
  pass

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
val_nom = tkinter.StringVar()
entry_nom = tkinter.Entry(frame_principal, textvariable = "", width = 15, font = entry_font )
entry_nom.pack(padx = 1, pady = 2)

#2e entry
val_mdp= tkinter.StringVar()
entry_mdp = tkinter.Entry(frame_principal, textvariable = "", width = 15, font = entry_font  )
entry_mdp.pack(padx = 2, pady = 2)

#bouton
button_valider = tkinter.Button(frame_principal, text = "valider", command=valider, width = 30, font = button_font)
button_valider.pack(padx = 1, pady = 3)

fenetre.mainloop()
