import graphene
from graphene_django import DjangoObjectType,DjangoListField
from .models import Category,Quizzes,Question,Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        field = ('id','name')
        

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        field = ('id','title','category','quiz')



class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        field = ('title','quiz')
        
        

class AnswerType(DjangoObjectType):
    class Meta:
        model = Category
        field = ('question','answer_text')
        
        
        
        
class Query(graphene.ObjectType):
    
    all_questions = graphene.Field(QuestionType,id=graphene.Int())
    all_answers = graphene.List(AnswerType,id = graphene.Int())
    # all_questions = graphene.List(QuestionType)
    
    def resolve_all_questions(root,info,id):
        return Question.objects.get(pk=id)
    
    
    def resolve_all_answers(root,info,id):
        return Answer.objects.filter(question=id)
    
    
    
    
class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required = True)
    category = graphene.Field(CategoryType) # defing the expected and return data type
    
    @classmethod
    def mutate(cls,root,info,name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)
        



class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
    
    
    
    
    
    
    
    
    
    
    
schema = graphene.Schema(query=Query,mutation=Mutation)
