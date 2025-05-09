def main():
    nomes = []
    idades = []
    rendas = []
    q_filhos = []

    
    n = int(input("Insira a quantidade de pessoas: \n"))

    for i in range(n):
        nome = input(f"Insira o nome da pessoa {i + 1}: \n")
        idade = int(input(f"Insira a idade de {nome}: \n"))
        renda = float(input(f"Insira a renda familiar de {nome}: \n"))
        filho = int(input(f"Insira a quantidade de filhos de {nome}: \n"))

        nomes.append(nome)
        idades.append(idade)
        rendas.append(renda)
        q_filhos.append(filho)


    indice_maior_idade = idades.index(max(idades))
    indice_menor_idade = idades.index(min(idades))


    indice_maior_renda = rendas.index(max(rendas))
    indice_menor_renda = rendas.index(min(rendas))


    indice_maior_filhos = q_filhos.index(max(q_filhos))
    indice_menor_filhos = q_filhos.index(min(q_filhos))


    print("\n===== RESULTADOS DA ANÁLISE =====")

    print("\n--- IDADE ---")
    print(f"Maior idade: {max(idades)} anos - Pessoa: {nomes[indice_maior_idade]}")
    print(f"Menor idade: {min(idades)} anos - Pessoa: {nomes[indice_menor_idade]}")

    print("\n--- RENDA FAMILIAR ---")
    print(f"Maior renda: R$ {max(rendas):.2f} - Pessoa: {nomes[indice_maior_renda]}")
    print(f"Menor renda: R$ {min(rendas):.2f} - Pessoa: {nomes[indice_menor_renda]}")

    print("\n--- QUANTIDADE DE FILHOS ---")
    print(f"Maior quantidade de filhos: {max(q_filhos)} - Pessoa: {nomes[indice_maior_filhos]}")
    print(f"Menor quantidade de filhos: {min(q_filhos)} - Pessoa: {nomes[indice_menor_filhos]}")

    # Exibição de estatísticas adicionais
    print("\n--- ESTATÍSTICAS GERAIS ---")
    print(f"Média de idade: {sum(idades) / len(idades):.1f} anos")
    print(f"Média de renda familiar: R$ {sum(rendas) / len(rendas):.2f}")
    print(f"Média de filhos: {sum(q_filhos) / len(q_filhos):.1f}")


if __name__ == "__main__":
    main()
