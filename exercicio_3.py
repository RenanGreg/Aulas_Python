def potencia (a ,b): 
    if b == 0: 
        return 1; 
    else: 
        return a * potencia (a , b -1)  
    

a = int(input("insira a base \n")) 
b = int(input("insira o exponete \n")) 
p = potencia(a , b) 

print(f"{a} elevado a {b} é {p}") 
