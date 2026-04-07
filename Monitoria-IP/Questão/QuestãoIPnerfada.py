# O código da Lobotomy CinCorporation!
def malkuth (energianecessaria):
    # A Malkuth é a sefirá da organização, ela dará um teste para o aluno ter que receber um input com vários nomes e ter que ordenar pelo tamanho dos nomes.
    print ("Hoje é o dia da Malkuth!")
    print ("Malkuth: Ah, onde estão meus modos! Malkuth se apresentando, gerente!")
    print ("Malkuth: Estamos responsáveis hoje por organizar alfabeticamente nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos, gerente!")
    print ("")
    # Um exemplo de input e saída: Roland Angela Netzach Yesod Hod = Hod Yesod Roland Angela Neztach
    listanomes = input().split()
    # Se caso nenhum funcionário estiver no time:
    if len(listanomes) == 0:
        print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!")
        print ("")
        return 0
    # Bubblesort
    trocas = 0
    for i in range (len(listanomes)):
        for j in range (len(listanomes) - 1 - i):
            if (len(listanomes[j]) > len(listanomes[j + 1])):
                listanomes[j], listanomes[j + 1] = listanomes[j+1], listanomes[j]

                # Cada troca adicionará 1 na variável trocas para ser usado no manejo da energia.
                trocas += 1
    print(*listanomes)

    energia = max(0, 300 - trocas * 20)
    print(f"Energia Coletada: {energia} / {energianecessaria}")
    if energia >= energianecessaria:
        print ("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!")
        print ("")
        return 1
    else:
        print ("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!")
        print ("")
        return 0
def yesod(energianecessaria):
    print ("Hoje é dia do Yesod!")
    print ("Yesod: Gerente, você é a cabeça dessa corporação, você deve agir como um exemplo para os outros e fazer certeza que esse dia passe coordialmente seguindo as regras.")
    print ("Yesod: Hoje estamos com um problema a resolver, Gerente. Você é um progamador, não é? Hoje recebemos notas de funcionários que vão de a-z, e você terá de as comprimir para facilitar as informações.")
    print ()
    # Um exemplo de notas e uma saída: AAAABBBBCCC = 4A4B3C
    notasdescomprimidas = input()
    notascomprimidas = ''
    i = 0
    char = ''
    while i < len(notasdescomprimidas) and char != "&":
        char = notasdescomprimidas[i]
        if char != "&":
            contagem = 1
            while i + contagem < len(notasdescomprimidas) and notasdescomprimidas[i + contagem] == char:
                contagem += 1
            if contagem > 1:
                notascomprimidas += str(contagem) + char
            else:
                notascomprimidas += char
            i += contagem

    if char == "&":
        print ("Yesod: As notas de hoje estavam corrompidas, gerente.. devemos encerrar o dia mais cedo e investigar.")
        print (f"Yesod: Pelo menos, essas informações ainda estão conosco: '{notascomprimidas}'")
        print ()
        return 0
    else:
        print (f"Yesod: Gerente, aqui está as notas comprimidas: '{notascomprimidas}'")
        print (f"Energia Coletada: {energianecessaria} / {energianecessaria}")
        print ()
        return 1

def dias(energianecessaria):
    sefirot = input()

    if sefirot == 'Malkuth':
        diaconcluido = malkuth(energianecessaria)
        conclusaodias.append(diaconcluido)
    elif sefirot == "Yesod":
        diaconcluido = yesod(energianecessaria)
        conclusaodias.append(diaconcluido)
    else:
        print("Angela: Essa sefirot não está disponível hoje, gerente.")
        conclusaodias.append(0)

# Inicialização de Variáveis
dia = 1
conclusaodias = []
energianecessaria = 100
quantidade_de_dias = int(input())

print ("Hoje é o dia da Lobotomy CinCorporation!")
while (dia <= quantidade_de_dias):

    print (f"Angela: Hoje é o dia {dia} de {quantidade_de_dias}. Espero mais um expediente concluído com excelência, gerente.")
    dias(energianecessaria)

    energianecessaria += 40
    dia += 1

print ("Angela: O relatório dessa semana está pronto, gerente.")
for i in range(len(conclusaodias)):
    if conclusaodias[i]:
        print (f"Dia {i + 1} | Status: Energia necessária adquirida.")
    else:   
        print (f"Dia {i + 1} | Status: Energia necessária não adquirida.")
