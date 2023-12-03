from tkinter import *
import requests
import sys
from PIL import Image, ImageTk


def get_exchange_rate(from_currency, to_currency):
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    data = response.json()
    return data['rates'][to_currency]

def update_result_label(text):
    result_label.config(text=text)

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = entry_from_currency.get().upper()
        to_currency = entry_to_currency.get().upper()
        
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        result = amount * exchange_rate
        
        # Affiche le résultat dans la fenêtre tkinter
        update_result_label(f"{amount} {from_currency} =  {result} {to_currency}")
    
    except ValueError:
        # Affiche le message d'erreur dans la fenêtre tkinter
        update_result_label("Erreur! Montant non valide; Veuillez entrer un nombre correcte.")

def reset_fields():
    entry_amount.delete(0, END)
    entry_from_currency.delete(0, END)
    entry_to_currency.delete(0, END)
    update_result_label("")




app = Tk()
app.configure(bg="Lightslategray")
app.title("Smart_convert")

# Restreindre la taille de la fenêtre
app.resizable(False, False)

image = Image.open("C:\\Users\\admin\\Documents\\Cours Python3\\pythonProject convertisseur\\plume.jpg")
image = image.resize((int(image.width / 13), int(image.height / 13)))
photo = ImageTk.PhotoImage(image)

# Créez un nouveau label pour afficher l'image
image_label = Label(app, image=photo, bg="light blue")
image_label.grid(row=0, column=2, rowspan=3, padx=5, pady=5)


entry_amount = Entry(app, width=20)
entry_amount.grid(row=0, column=1)

amount_label = Label(app, text="Entrez le montant que vous souhaitez convertir")
amount_label.grid(row=0, column=0, padx=10, pady=10)

entry_from_currency = Entry(app, width=20)
entry_from_currency.grid(row=1, column=1,padx=10, pady=10)


from_currency_label = Label(app, text="Entrez la devise actuelle")
from_currency_label.grid(row=1, column=0,padx=10, pady=10)


entry_to_currency = Entry(app, width=20)
entry_to_currency.grid(row=2, column=1)

to_currency_label = Label(app, text="Entrez la devise voulu")
to_currency_label.grid(row=2, column=0,padx=10, pady=10)

convert_button = Button(app, text="Convertir", command=convert_currency, bg="green")
convert_button.grid(row=3, column=1, padx=10, pady=10)

reset_button = Button(app, text="Réinitialiser", command=reset_fields, bg="Crimson")
reset_button.grid(row=3, column=0,)

result_label = Label(app, text="")
result_label.grid(row=3, column=2, padx=10)

app.mainloop()