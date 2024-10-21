from flask import Flask
from flask_graphql import GraphQLView
import graphene
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()

engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="world"))
    books = graphene.List(Book)

    def resolve_books(self, info):
        session = Session()
        return session.query(Book).all()

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema))

if __name__ == '__main__':
    app.run()