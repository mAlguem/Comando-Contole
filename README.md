# Comando-Contole

Fiz meu primeiro projeto em python que consiste em uma api que roda um banco de dados que armazena "id e comandos" atraves de metodos como "GET e POST", como funciona:

-> O servidor fica rodando e armazenando os comandos

-> O atacante envia um comando para o servidor atraves do método POST

-> A vitima realiza o metodo GET no ultimo comando armazenado no banco de dados, depois extrai esse comando e utiliza a biblioteca subprocess para executar o comando localmente onde a saida é enviada para o banco de dados atraves do metodo POST

-> O atacante vai ter um tempo de espera de 5 segundos para fazer um GET no banco de dados onde vai visualizar a saida do comando que foi executado na vitima.

-> Isso vai ocorrer em loop tanto no atacante quanto na vitima

"""
Caso queira testar o codigo, dividi os terminais em tres no mesmo terminal (podendo utilizar o vscode ou terminator, tmux) , recomendo iniciar o servidor, depois a vitima e o atacante e testar.
"""

"""
Aceito sugestões de melhora para deixar esse projeto mais robusto
"""

"""
Para o codigo funcionar perfeitamente, edite a linha 8 e coloque o diretorio que deseja criar o banco de dados informando o caminho completo.
Caso esteja no Sistema Operacional linux apenas mude o caminho

-> Caso esteja no Windows: 
("sqlite:///C:\\Users\\teste\\seu\\diretorio\\atual\\teste.db")
''''
