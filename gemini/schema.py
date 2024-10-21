import graphene

class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    author = graphene.String()
    publication_year = graphene.Int()

class Author(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class Query(graphene.ObjectType):
    all_books = graphene.List(Book)
    book_by_id = graphene.Field(Book, id=graphene.ID())
    author_by_name = graphene.Field(Author, name=graphene.String())

class Mutation(graphene.ObjectType):
    create_book = graphene.Field(Book, title=graphene.String(), author=graphene.String())

schema = graphene.Schema(query=Query, mutation=Mutation)