def ola(): 
    nome = input("insira o nome \n")
    print(f"ola {nome}, Bem vindo ao curso \n")

def idade(): 
    ano_atual = int(input("insira o ano atual \n"))
    ano_nasc= int(input("insira o ano de seu nascimento \n")) 
    idade = ano_atual - ano_nasc 
    print(f"idade no ano {ano_atual} é {idade}") 

ola()
idade() 
