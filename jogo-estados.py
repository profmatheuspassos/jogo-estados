import random
import os

estados = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

def imprimeFinal(pontuacao, rodadas):
    print(f"Pontuação final: {pontuacao}")
    print("Porcentagem de acertos: {:.2f}%".format((pontuacao / rodadas) * 100))
    print("Até a próxima!")

estadoComp = ""
rodadas = 0
pontuacao = 0

while True:
    os.system("cls" if os.name == "nt" else "clear")
    estadoComp = random.choice(list(estados.keys()))
    escolhaUsuario = input(f"Qual a capital de {estadoComp}? => ").strip()
    if escolhaUsuario == estados[estadoComp]:
        pontuacao += 1
        rodadas += 1
        print("Você acertou!")
        print(f"Pontuação atual: {pontuacao}")
    else:
        rodadas += 1
        print("Você errou!")
        print(f"Pontuação atual: {pontuacao}")
    del estados[estadoComp]
    if not estados:
        print("Você chegou ao final do jogo, já que foram perguntadas as capitais de todos os estados brasileiros.")
        imprimeFinal(pontuacao, rodadas)
        break
    while True:
        continuar = input("Deseja jogar novamente? (S/N) => ").strip().upper()
        if continuar in ["S", "N"]:
            break  # Sai do loop interno se a entrada for válida
        else:
            print("Por favor, digite \"S\" para continuar ou \"N\" para sair.\n")
    if continuar == "S":
        continue
    else:
        imprimeFinal(pontuacao, rodadas)
        break