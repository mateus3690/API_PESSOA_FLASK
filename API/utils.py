from models import Pessoas

def consulta():
     select = Pessoas.query.all()
     #select = Pessoas.query.filter_by(nome='gabriel').first()
     return select

def inserir():

     insert_into = Pessoas(nome='gabriel', idade=14)
     insert_into.save()

     print(insert_into)

def alterar():
     update = Pessoas.query.filter_by(nome='gabriel').first()
     update.idade = 20
     update.save()
     print('atualizando ok..')

def excluir():
     delet = Pessoas.query.filter_by(nome='gabriel').first()
     delet.delete()

if __name__ == '__main__':
     #inserir()
     #alterar()
     print(consulta())
     #excluir()
    # print(consulta())
