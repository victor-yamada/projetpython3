###from tkinter import *
###fen1 = Tk()
###fen1.title("Smart_convert")
###tex1 = Label(fen1, text='************************! Bienvenue dans Smart_convert !******************************', fg= 'green')
###tex1.grid()
###tex2 = Label(fen1, text="Quelle opération désirez-vous effectué aujourd'hui? ", fg= 'red')
###tex2.grid()###



###txt3 = Label(fen1, text = 'Entrez un montant :')
###txt4 = Label(fen1, text = 'Entrez une devise:')
###txt5 = Label(fen1, text = 'Entrez la Devise voulu:')
###entrer1 = Entry(fen1)
###entrer2 = Entry(fen1)
###entrer3 = Entry(fen1)
###txt3.grid(row = 0)
###txt4.grid(row = 1)
###txt5.grid(row = 2)
###entrer1.grid(row = 0, column= 1)
###entrer2.grid(row = 1, column= 1)
###entrer3.grid(row = 1, column= 2)







###resultat = Label(fen1, text="L'équivalent de " entrer1 + entrer2 "est égal à" operation entrer3)

###bou1 = Button(fen1, text='Réinitialiser', command = fen1.update)


###bou1.grid(side = BOTTOM)
###fen1.mainloop()

#from tkinter import *
#import requests

#def get_exchange_rate(from_currency, to_currency):
 #   response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
  ## return data['rates'][to_currency]

#def convert_currency(amount, from_currency, to_currency):
 #   exchange_rate = get_exchange_rate(from_currency, to_currency)
  #  return amount * exchange_rate

#amount = float(input("Entrez le montant que vous souhaitez convertir: "))
#from_currency = input("Entrez la devise actuelle: ").upper()
#to_currency = input("Entrez la devise voulu: ").upper()

#result = convert_currency(amount, from_currency, to_currency)
#print(f"{amount} {from_currency} is equal to {result} {to_currency}")



from tkinter import *
import requests

def get_exchange_rate(from_currency, to_currency):
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{from_currency}')
    data = response.json()
    return data['rates'][to_currency]

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()

    result = convert_currency(amount, from_currency, to_currency)
    result_label.config(text=f"{amount} {from_currency} is equal to {result} {to_currency}")

