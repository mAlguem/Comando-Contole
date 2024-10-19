import requests, json, time

def enviando():
    while True:
        url = "http://127.0.0.1:9910/"

        comando = input("Comando: ")

        payload = json.dumps({
            "comando": comando
        })

        header = {
            "Content-Type":"application/json"
        }

        request = requests.request("POST", url, headers=header, data=payload)

        if request.status_code == 200:
            print("\nComando enviado...")
        else:
            print("Erro")
        
        time.sleep(5)

        payload = ""
        header = {}
        enviar = requests.request("GET", url, headers=header, data=payload)
        if enviar.status_code == 200:
            print(enviar.text)
        else:
            print("Erro")

enviando()
