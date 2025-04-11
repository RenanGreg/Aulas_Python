from array import array

array = [9, 0, 6, 2, 9, 1, 9]
local = []
alvo = 9

for i in range(len(array)):
    if array [i] == alvo:
        posicao = i
        local.append(posicao)

    else:
        posicao = -1

if len(local) <=0 :
    print("Valor não encontrado")

else:
    print(f"Posiçoes do valor {alvo}")
    print(local)
    print(f"A quantidade de ocorrencias é: {len(local)}")
