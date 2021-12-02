from flask import Flask, request
from flask_restful import Api, Resource
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


#PESSOAS
class Api_Pessoa(Resource):

     def get(self, nome):

          try:
               pessoa = Pessoas.query.filter_by(nome=nome).first()
               response = {
                    'id':pessoa.id,
                    'nome':pessoa.nome,
                    'idade':pessoa.idade
               }
          except AttributeError:
               response = {
                    'status':'Error',
                    'mensagem':f" '{nome}' não existe nos registros"
               }

          return response
     
     def put(self, nome):

          try:
               pessoa = Pessoas.query.filter_by(nome=nome).first()
               dados = request.json

               if 'nome' in dados:
                    pessoa.nome = dados['nome']
               
               if 'idade' in dados:
                    pessoa.idade = dados['idade']
               pessoa.save()

               response = {
                    'id':pessoa.id,
                    'nome':pessoa.nome,
                    'idade':pessoa.idade
               }

          except TypeError:
               response = {
                    'status':'Error',
                    'mensagem':"Null"
               }

          return response

     def delete(self, nome):
          
          try:
               pessoa = Pessoas.query.filter_by(nome=nome).first()
               pessoa.delete()
               response = {
                    'status':'Ok',
                    'mensagem':f'{nome} foi deletado dos registros com sucesso'
               }
          except AttributeError:
               response = {
                    'status':'Error',
                    'mensagem':'Por favor informe uma pessoa existente nos registros'
               }
          
          return response

class Api_Pessoa_home(Resource):

     def get(self):
          pessoas = Pessoas.query.all()
          response = [{
                    'id':dados.id,
                    'nome':dados.nome,
                     'idade':dados.idade         
          } for dados in pessoas]
          
          return response
     
     def post(self):
          
          try:
               dados = request.json
               pessoa = Pessoas(nome = dados['nome'], idade = dados['idade'])
               pessoa.save()

               response = {
                    'id':pessoa.id,
                    'nome':pessoa.nome,
                    'idade':pessoa.idade
               }

          except KeyError:
               response = {
                    'status':'Error',
                    'mensagem':'Falta informação no registro'
               }
          
          except TypeError:
               response = {
                    'status':'Error',
                    'mensagem':'Null'
               }

          return response


#ATIVIDADES
class Api_Atividade(Resource):

     def get(self):
          
          ativades = Atividades.query.all()
          response = [{
                    'id':dados.id,
                    'nome':dados.nome,
                    'pessoa':dados.tb_pessoa.nome         
          } for dados in ativades]
          
          return response

     def post(self):
          dados = request.json
          pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()

          atividade = Atividades(nome = dados['nome'], tb_pessoa = pessoa) 
          atividade.save()

          response = {
              'id':atividade.id,
              'nome':atividade.nome,
              'pessoa':atividade.tb_pessoa.nome
      
          }

          return response



#rotas
api.add_resource(Api_Pessoa, '/pessoa/<string:nome>' )
api.add_resource(Api_Pessoa_home, '/pessoa')
api.add_resource(Api_Atividade, '/atividade')


if __name__ == '__main__':
     app.run(debug=True)