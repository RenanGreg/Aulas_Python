def val(): 
    op = int(input("insira a opção \n")) 

    if (op == 1 or op == 2 or op == 3): 
        return op 
    
    else: 
        print("opcão errada \n")
        return val() 
    

def soma (a , b): 
    return a + b 

def sub (a , b): 
    return a - b 

def mult (a , b): 
    return a * b 

print("Menu: \n1 - Soma \ n2 - Subtração \n3 - Multiplicação") 

escolha = val() 

a = int(input("insira o primeira valor \n ")) 
b = int(input("insira o segundo valor \n")) 

if escolha == 1: 
    s = soma(a, b)  
    print(f"soma = {s}") 

elif escolha == 2: 
    sb = sub (a , b)
    print(f"subtração {sb}") 

else: 
    m = mult(a , b) 
    print(f"multiplicação {m}") 
