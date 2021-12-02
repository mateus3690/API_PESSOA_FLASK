from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///baseLocal.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):

     __tablename__ = 'tb_pessoa'
     id = Column(Integer, primary_key=True)
     nome = Column(String(50), index=True)
     idade = Column(Integer)

     def __repr__(self):
         return f'<Pessoa {self.nome}>'
     
     def save(self):
          db_session.add(self)
          db_session.commit()
     
     def delete(self):
          db_session.delete(self)
          db_session.commit()


class Atividades(Base):

     __tablename__ = 'tb_atividades'
     id = Column(Integer, primary_key=True)
     nome = Column(String(80))
     id_pessoa = Column(Integer, ForeignKey('tb_pessoa.id'))
     tb_pessoa = relationship('Pessoas')

     def __repr__(self):
         #return f'<Pessoa {self.nome}>'
         return f'<Ativiade {self.nome}>'
     
     def save(self):
          db_session.add(self)
          db_session.commit()
     
     def delete(self):
          db_session.delete(self)
          db_session.commit()


def init_db():
     Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
     init_db()