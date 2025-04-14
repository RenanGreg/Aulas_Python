import tkinter as tk

#Janela principal
root = tk.Tk()
root.title("Janela de Trabalho")

#tamanho da janela
root.geometry("600x600")

label1 = tk.Label(root, text = "Bem Vindo")
label1.pack(padx=50 , pady=50)

def ola():
    label2 = tk.Label(root, text= "botao funcionando")
    label2.pack(padx=25 , pady=25)

botao= tk.Button(root, text="ok", command=ola)
botao.pack(padx=30 , pady=30)

t = tk.Entry(root)
t.pack(pady=35 , padx=35)

#Caixa de texto
def texto():
    valor = t.get()
    label1.config(text= "Bem Vindo \n" + valor)

botao2 = tk.Button(root, text="Atualizar", command=texto)
botao2.pack(pady=25, padx=25)

#Abrindo uma nova opção de janela
def janela():
    frame1 = tk.Toplevel(root)
    frame1.title("Nova Janela")
    frame1.geometry("300x300")

    label3 = tk.Label(frame1, text="Janela do Usuario")
    label3.pack(padx=20 , pady=20)

#Botao de sair
    def sair():
        frame1.destroy()
    botao3 = tk.Button(frame1, text="Sair" , command=sair)
    botao3.pack(padx=20, pady=20)
    frame1.pack()

botao4 = tk.Button(root, text="Nova Janela", command=janela)
botao4.pack(pady=20 , padx=20)

#Iniciando loop principal
root.mainloop()
