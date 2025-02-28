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

    label5 = tk.Label(root, text= "Lista de convidados", font=("Arial", 15))
    label5.grid(row= 5 , column= 1)

    for i, item in enumerate(lista_nomes):
        label6 = tk.Label(root, text=item)
        label6.grid(row= i + 6, column=0)

    for i, item in enumerate(lista_idades):
        label7 = tk.Label(root, text=item)
        label7.grid(row= i + 6, column=2)

    for i, item in enumerate(lista_emails):
        label8 = tk.Label(root, text=item)
        label8.grid(row=i + 6, column=1)

root = tk.Tk()
root.title("Convite")
root.geometry("500x500")

label1 = tk.Label(root, text="Convidados", font=("Arial", 15))
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Nome:", font=("Arial", 15))
label2.grid(row=1, column=0)

entrada1 = tk.Entry(root, font=("Arial", 15))
entrada1.grid(row=1, column=1)

label3 = tk.Label(root, text="Idade:", font=("Arial", 15))
label3 .grid(row=2, column=0)

entrada2 = tk.Entry(root, font=("Arial", 15))
entrada2.grid(row=2, column=1)

label4 = tk.Label(root, text="Email:", font=("Arial", 15))
label4.grid(row=3, column=0)

entrada3 = tk.Entry(root, font=("Arial", 15))
entrada3.grid(row=3, column=1)

b_ad = tk.Button(root, text="Adicionar", font=("Arial", 15),command=ad)
b_ad.grid(row=4, column=0)
b_exibir = tk.Button(root, text="Exibir", font=("Arial", 15),command=exibir)
b_exibir.grid(row=4, column=1)

root.mainloop()
