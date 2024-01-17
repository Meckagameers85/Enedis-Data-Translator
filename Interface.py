
import tkinter as tk
from tkinter import ttk, filedialog
path_fichier, path_dossier = "", ""

def choisir_fichier():
    global fichier, path_fichier
    path_fichier = filedialog.askopenfilename(title="Choisir un fichier")
    fichier = path_fichier.split("/")[-1]
    mettre_a_jour_etat_bouton()

def choisir_dossier():
    global dossier, path_dossier
    path_dossier = filedialog.askdirectory(title="Choisir un dossier")
    dossier = path_dossier.split("/")[-1]
    mettre_a_jour_etat_bouton()

def afficher_fichier():
    fenetre.destroy()

def mettre_a_jour_etat_bouton():
    if path_fichier!="":
        label_fichier.config(text=f"Fichier: {fichier}")
    if path_dossier!="":
        label_dossier.config(text=f"Dossier: {dossier}")
    
    if path_fichier!="" and path_dossier!="":
        btn_afficher['state'] = 'normal'
    else:
        btn_afficher['state'] = 'disabled'

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Interface Python")

# Utilisation de styles pour un look plus moderne
style = ttk.Style()
style.configure('TButton', padding=(10, 5, 10, 5), font=('Helvetica', 12))
style.configure('TLabel', font=('Helvetica', 12))

# Bouton pour choisir un fichier
btn_fichier = ttk.Button(fenetre, text="Choisir un fichier", command=choisir_fichier)
btn_fichier.pack(pady=10)

# Bouton pour choisir un dossier
btn_dossier = ttk.Button(fenetre, text="Choisir un dossier", command=choisir_dossier)
btn_dossier.pack(pady=10)

# Label pour afficher le nom du fichier sélectionné
label_fichier = ttk.Label(fenetre, text="Fichier :")
label_fichier.pack(pady=10)

# Label pour afficher le nom du dossier sélectionné
label_dossier = ttk.Label(fenetre, text="Dossier :")
label_dossier.pack(pady=10)

# Bouton pour afficher les fichiers et dossiers sélectionnés
btn_afficher = ttk.Button(fenetre, text="Traduire", command=afficher_fichier, state='disabled')
btn_afficher.pack(pady=10)

# Lancer la boucle principale
fenetre.mainloop()
