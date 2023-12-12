from tkinter import *
import requests
import sys
from PIL import Image, ImageTk
import sqlite3


def get_exchange_rate(from_currency, to_currency):
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    data = response.json()
    return data['rates'][to_currency]

def update_result_label(text):
    result_label.config(text=text)

def convert_currency():
    try:
        amount = int(entry_amount.get())
        from_currency = entry_from_currency.get().upper()
        to_currency = entry_to_currency.get().upper()
        
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        result = amount * exchange_rate
        
        # Enregistrer l'opération dans la base de données
        cursor.execute(f"INSERT INTO operations (amount, from_currency, to_currency, result) VALUES ({amount}, '{from_currency}', '{to_currency}', {result})")
        conn.commit()
        

        # Affiche le résultat dans la fenêtre tkinter
        update_result_label(f"{amount} {from_currency} = {result} {to_currency}")
    
    except ValueError:
        # Affiche le message d'erreur dans la fenêtre tkinter
        update_result_label("Erreur! Montant non valide; Veuillez entrer un nombre correcte.")

def get_last_operation():
    try:
        cursor.execute("SELECT * FROM operations ORDER BY id DESC LIMIT 1")
        last_operation = cursor.fetchone()

        if last_operation:
            entry_amount.delete(0, END)
            entry_amount.insert(0, last_operation[1])

            entry_from_currency.delete(0, END)
            entry_from_currency.insert(0, last_operation[2])

            entry_to_currency.delete(0, END)
            entry_to_currency.insert(0, last_operation[3])

            update_result_label(f"{last_operation[1]} {last_operation[2]} = {last_operation[4]} {last_operation[3]}")
        else:
            update_result_label("Erreur! Aucune opération précédente n'a été effectuée.")
    
    except sqlite3.Error:
        update_result_label("Erreur! Aucune opération précédente n'a été effectuée.")
def reset_fields():
    entry_amount.delete(0, END) 
    entry_from_currency.delete(0, END)
    entry_to_currency.delete(0, END)
    update_result_label("")

# Connexion à la database
conn = sqlite3.connect('convertisseur.db')
cursor = conn.cursor()

# Création de la table operations" 
cursor.execute("""
CREATE TABLE if not exists operations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    from_currency TEXT,
    to_currency TEXT,
    result REAL
)
""")


app = Tk()
app.configure(bg="Lightslategray")
app.geometry("700x220")
app.title("Smart_convert")


# Restreindre la taille de la fenêtre
app.resizable(False, False)

# Ajout et Configuration de l'image
image = Image.open("C:\\Users\\admin\\Documents\\Cours Python3\\pythonProject convertisseur\\plume.jpg")
image = image.resize((int(image.width / 13), int(image.height / 13)))
photo = ImageTk.PhotoImage(image)

# Créez un nouveau label pour afficher l'image
image_label = Label(app, image=photo, bg="light blue")
image_label.grid(row=0, column=2, rowspan=3, padx=5, pady=5)

# Créer un label pour entrer le montant
entry_amount = Entry(app, width=20)
entry_amount.grid(row=0, column=1)

# Créer un label pour le texte "Entrez le montant que vous souhaitez convertir"
amount_label = Label(app, text="Entrez le montant que vous souhaitez convertir", bg="Lightslategray")
amount_label.grid(row=0, column=0, padx=10, pady=10)

# Créer un label pour entrer la devise actuelle
entry_from_currency = Entry(app, width=20)
entry_from_currency.grid(row=1, column=1,padx=10, pady=10)

# Créer un label texte "entrer la devise actuelle"
from_currency_label = Label(app, text="Entrez la devise connue", bg="Lightslategray")
from_currency_label.grid(row=1, column=0,padx=10, pady=10)

# Créer un label pour entrer la devise voulu
entry_to_currency = Entry(app, width=20)
entry_to_currency.grid(row=2, column=1)

# Créer un label texte "entrer la devise voulu"
to_currency_label = Label(app, text="Entrez la devise voulu", bg="Lightslategray")
to_currency_label.grid(row=2, column=0,padx=10, pady=10)

# Créer le bouton de conversion
convert_button = Button(app, text="Convertir", command=convert_currency, bg="green")
convert_button.grid(row=3, column=1, padx=10, pady=10)

# Création du bouton de réinitialisation de l'opération
reset_button = Button(app, text="Réinitialiser", command=reset_fields, bg="Indianred")
reset_button.grid(row=3, column=0,)

# message
amount_label = Label(app, text="Exemple code de devise: ",font=("arial", 10), fg="Navajowhite", bg="Lightslategray")
amount_label.grid(row=4, column=0)

amount_label = Label(app, text=" 'USD' 'EUR' 'GBP' 'CAD' 'XAF' ",font=("arial", 10), fg="Navajowhite", bg="Lightslategray")
amount_label.grid(row=4, column=1)

# Création du bouton pour revenir à la précédente opération
reset_button = Button(app, text="Précédent", command=get_last_operation, bg="Navajowhite")
reset_button.grid(row=4, column=2)

#Création du label d'affichage du résultat
result_label = Label(app, text="", bg="Lightslategray")
result_label.grid(row=3, column=2, padx=10)

app.mainloop()
conn.close()
