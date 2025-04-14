import tkinter as tk

janela = tk.Tk

lista_nomes = []
lista_idades = []
lista_emails = []

def ad():
    valor1 = entrada1.get()
    lista_nomes.append(valor1)

    valor2 = entrada2.get()
    lista_idades.append(valor2)

    valor3 = entrada3.get()
    lista_emails.append(valor3)

    alert = tk.Toplevel(root)

    label9 = tk.Label(alert, text= "Convidado inserido na lista")
    label9.pack()

    def ok():
        alert.destroy()
    b_ok = tk.Button(alert, text="Ok", command=ok)
    b_ok.pack()
    entrada1.delete(0, "end")
    entrada2.delete(0, "end")
    entrada3.delete(0, "end")


def exibir():

    lista1.delete(0, tk.END)
    lista2.delete(0, tk.END)
    lista3.delete(0, tk.END)

    for item1 in lista_nomes:
        lista1.insert(tk.END, item1)

    for item2 in lista_idades:
        lista2.insert(tk.END, item2)

    for item3 in lista_emails:
        lista3.insert(tk.END, item3)


def limp():
    lista_nomes.clear()
    lista_idades.clear()
    lista_emails.clear()

def loc():
    alert1 = tk.Toplevel(root)
    alert1.title("Localizar Convidado")
    valor = entrada4.get()
    
    if lista_nomes.count(valor) >= 1: 
        label_alert = tk.Label(alert1, text="Covidado Localizado", font=("Arial", 15)) 
        
    else:
        label_alert1 = tk.Label(alert1, text="Convidado Não Localizado", font=("Arial", 15))  
        label_alert1.pack() 
        
    def ok():
        alert1.destroy()
        b_alert = tk.Button(alert1, text="OK", font=("Arial", 15), command=ok)
        b_alert.pack
        
root = tk.Tk()
root.title("Convite")
root.geometry("675x500")

# LABELS
label1 = tk.Label(root, text="Convidados", font=("Arial", 15))
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Nome:", font=("Arial", 15))
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Idade:", font=("Arial", 15))
label3 .grid(row=2, column=0)

label4 = tk.Label(root, text="Email:", font=("Arial", 15))
label4.grid(row=3, column=0)

label3 = tk.Label(root, text="Idade:", font=("Arial", 15))
label3 .grid(row=2, column=0)

label4 = tk.Label(root, text="Email:", font=("Arial", 15))
label4.grid(row=3, column=0)

label5 = tk.Label(root, text= "Lista de convidados", font=("Arial", 15))
label5.grid(row= 5, column= 1)

label6 = tk.Label(root, text="Nome", font=("Arial", 15))
label6.grid(row=8, column=0)

label7 = tk.Label(root, text="Idade", font=("Arial", 15))
label7.grid(row=8, column=1)

label8 = tk.Label(root, text="Email", font=("Arial", 15))
label8.grid(row=8, column=2)

#ENTRADAS
entrada1 = tk.Entry(root, font=("Arial", 15))
entrada1.grid(row=1, column=1)

entrada2 = tk.Entry(root, font=("Arial", 15))
entrada2.grid(row=2, column=1)

entrada3 = tk.Entry(root, font=("Arial", 15))
entrada3.grid(row=3, column=1)

entrada4 = tk.Entry(root, font=("Arial", 15))
entrada4.grid(row=6, column=1)

#LISTAS
lista1 = tk.Listbox(root, font=("Arial", 15))
lista1.grid(row=6, column=0)

lista2 = tk.Listbox(root, font=("Arial", 15))
lista2.grid(row=6, column=1)

lista3 = tk.Listbox(root, font=("Arial", 15))
lista3.grid(row=6, column=2)

#BOTOES

#Botao adicionar
b_ad = tk.Button(root, text="Adicionar", font=("Arial", 15),command=ad)
b_ad.grid(row=4, column=0)

#Botao Exibir
b_exibir = tk.Button(root, text="Exibir", font=("Arial", 15),command=exibir)
b_exibir.grid(row=4, column=1)

#Botao Limpar
b_limpar = tk.Button(root, text="Limpar", font=("Arial", 15), command=limp)
b_limpar.grid(row=4, column=2)

#Botao Localizar
label_loc = tk.Label(root, text="Localizar convidado:", font=("Arial", 15))
label_loc.grid(row=5, column=0)

b_loc = tk.Button(root, text="Localizar", font=("Arial", 15), command=loc)
b_loc.grid(row=5, column=2)

root.mainloop()
