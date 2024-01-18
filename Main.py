import csv
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


path_fichier, path_dossier = "", ""
fichier, dossier = "", ""

def get_data(path):
    global path_fichier,fichier
    data = ""
    header = ""
    dico_Header = {"CONS": "Consommation","BRUT":"Comptage Brut"}
    with open(path, "r") as file:
        data = file.read()
    header,data = data.split('"points":')
    
    #data: "mesures":[{...},{...},{...}]}
    header = header.split('"mesures":[{')[1]
    header = header.split(",")
    Exit_Data = [["Identifiant PRM", "Date de debut","Date de fin","Grandeur metier","Etape metier","Unite"]]
    Exit_Data.append([header[0].split('"idPrm":"')[1][:-1],
                      header[2].split('"dateDebut":"')[1][:-10],
                      header[3].split('"dateFin":"')[1][:-11],
                      dico_Header[header[5].split('"grandeur":[{"grandeurMetier":"')[1][:-1]],
                      dico_Header[header[1].split('"etapeMetier":"')[1][:-1]],
                      header[7].split('"unite":"')[1][:-1]
                      ])
    
    #data: "points":[{...},{...},{...}]header
    Exit_Data.append(["Horodate", "Valeur","","","",""])
    data = data.replace("]}]}]}", "]")
    data = data.replace("}, {", "},{")
    data = data.replace("} ,{", "},{")
    datas = data.split("},{")
    for i in range(len(datas)):
        ligne = []
        ligne = datas[i].split(",")
        ligne = ligne[:2]
        Exit_Data.append([ligne[1].split('"')[3], ligne[0].split('"')[3],"","","",""])
    return Exit_Data

def translate_CSV():
    global path_fichier, path_dossier, fichier, dossier
    if path_fichier !="" and path_dossier != "":
        data = get_data(path_fichier)
        path = path_dossier + "/" + fichier[:-4] + "_traduit.csv"
        with open(path, 'w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=';')
            writer.writerows(data)
        messagebox.showinfo("Traduction", "Traduction terminée !")
        fenetre.destroy()

def choisir_fichier():
    global fichier, path_fichier
    data = ""
    path_fichier = filedialog.askopenfilename(title="Choisir un fichier")
    fichier = path_fichier.split("/")[-1]
    if fichier[-5:] != ".json":
        messagebox.showerror("Erreur", "Le fichier doit être au format .json")
        path_fichier = ""
        fichier = ""
        
    else :
        with open(path_fichier, "r") as file:
            data = file.read()
        if '"points":' not in data:
            messagebox.showerror("Erreur", "Le fichier ne contient pas de données")
            path_fichier = ""
            fichier = ""
    mettre_a_jour_etat_bouton()

def choisir_dossier():
    global dossier, path_dossier
    path_dossier = filedialog.askdirectory(title="Choisir un dossier")
    dossier = path_dossier.split("/")[-1]
    mettre_a_jour_etat_bouton()

def mettre_a_jour_etat_bouton():
    if path_fichier != "":
        label_fichier.config(text=f"Fichier: {fichier}")
    if path_dossier != "":
        label_dossier.config(text=f"Dossier: {dossier}")

    if path_fichier != "" and path_dossier != "":
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
btn_afficher = ttk.Button(fenetre, text="Traduire", command=translate_CSV, state='disabled')
btn_afficher.pack(pady=10)

# Lancer la boucle principale
fenetre.mainloop()
