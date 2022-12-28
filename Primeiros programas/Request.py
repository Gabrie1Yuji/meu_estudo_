import requests

url = "g1.globo.com"
file = open('lista.txt')
lista = file


for linha in lista:
    linha = linha.strip()

    #Monta url
    sub_to_check = f"https://{url}.{linha}"

    try:
        r = requests.get(sub_to_check) 
        print("sucesso")
        print(sub_to_check)  
        print("##########")
    except:
        print(f"nao consegui {sub_to_check}")
        continue

