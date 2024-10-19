from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sqlalchemy as db

engine = db.create_engine("sqlite:////home/skopeo/Desktop/PYTHON/CP - BOT/storage.db")
conexao = engine.connect()
metadado = db.MetaData()
metadado.bind = engine
metadado.reflect(bind=engine)

try:
    tabela_comando = db.Table("tabela_comando", metadado,
                            db.Column("ID", db.Integer, primary_key=True, autoincrement=True),
                            db.Column("CMD", db.Text, nullable=True) , extend_existing=True
                            )
    metadado.create_all(engine)
except Exception as e:
    print(f"Erro ao criar a tabela {e}")

app = Flask(__name__)
api = Api(app)

class Comandos(Resource):
    def get(self):
        query_get = conexao.execute(db.select(tabela_comando))
        resultado = [dict(row) for row in query_get.mappings()]
        return jsonify(resultado)

    def post(self):
        dados = request.get_json()
        cmd = dados.get("comando")
        if cmd:
            query_post = tabela_comando.insert().values(CMD=cmd)
            conexao.execute(query_post)
            conexao.commit()
            return {"message":"Comando adicionado"}
        else:
            return {"message": "Erro no comando"}
        
api.add_resource(Comandos, "/")

if __name__ == "__main__":
    app.run(debug=True, port=9910)
