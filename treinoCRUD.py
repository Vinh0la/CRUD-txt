def main():
    lista_meds = []
    resp = 1

    while(resp != 0):
        print("1 - Inserir médico")
        print("2 - Alterar médico")
        print("3- Remove médico")
        print("4 - Gerar lista dos médicos cadastrados")
        print("5 - Gravar lista em arquivo .txt")

        opc = int(input("Escolha uma opção(1 - 5): "))

        if (opc == 1):
            insere_med(lista_meds)
        elif(opc == 2):
            ra = int(input("Insira o RA do médico que será alterado: "))
            altera_med(lista_meds,ra)
        elif(opc == 3):
            ra = int(input("Insira o RA do médico que será alterado: "))
            remove_med(lista_meds,ra)
        elif(opc == 4):
            relatorio(lista_meds)
        else:
            gravar_texto(lista_meds)

        resp = int(input("Deseja continuar? (1-Sim/0-Não): "))

    

def insere_med(lista_meds):
    try:
        ra = int(input("Insira o RA do médico a ser inserido: "))
        nome = input("Insira o nome do médico: ")
        idade = int(input("Insira a idade do médico: "))
    except ValueError:
        print("Insira apenas valores numéricos!")
    else:
        med = {'RA':ra, 'Nome':nome, 'Idade':idade}
        lista_meds.append(med)

def busca_med(lista_med,ra):
    pos = -1
    for i in range(len(lista_med)):
        if(lista_med[i]['RA'] == ra):
            pos = i
    return(pos)

def altera_med(lista_med,ra):
    pos = busca_med(lista_med,ra)

    if(pos != -1):
        try:
            print(f"Médico que será alterado: {lista_med[pos]['Nome']}")
            nome = input("Insira o novo nome do médico: ")
            print(f"Idade do médico: {lista_med[pos]['Idade']}")
            idade = int(input("Insira a nova idade do médico: "))
        except ValueError:
            print("Insira um valor numérico!")
        else:
            lista_med[pos]['Nome'] = nome
            lista_med[pos]['Idade'] = idade
    else:
        print("RA não encontrado!")
    
def remove_med(lista_med,ra):
    pos = busca_med(lista_med,ra)

    if(pos != -1):
        lista_med.pop(pos)
        print("Médico removido!")
    else:
        print("RA não encontrado!")
        
def relatorio(lista_med):
    for i in range(len(lista_med)):
        print(lista_med[i])

def gravar_texto(lista_med):
     for i in range(len(lista_med)):
        texto = str(lista_med[i]['RA']) + " " + lista_med[i]['Nome'] + " " + str(lista_med[i]['Idade'])
        with open("Lista_de_Medicos.txt","a",encoding="UTF8") as arq:
            arq.write(texto)
            arq.close
     print("Arquivo criado!")
    
if (__name__ == "__main__"):
    main()
