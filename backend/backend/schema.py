import graphene
from graphene_django import DjangoObjectType
from bio.models import Bio#, BioType
from user.models import User#, UserType
from social.models import Social#, SocialType
from graphene_file_upload.scalars import Upload
import graphql_jwt
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
class BioType(DjangoObjectType):
    class Meta:
        model = Bio
        fields = (
            "user",
            "body",
            "img"
        )

class SocialType(DjangoObjectType):
    class Meta:
        model = Social
        fields = "__all__"  

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_username = graphene.Field(UserType, username = graphene.String(required=True))
    all_bios = graphene.List(BioType)
    bio_by_id = graphene.Field(BioType, id = graphene.Int(required=True))
    socials = graphene.List(SocialType)

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_user_by_username(root, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
    def resolve_bio_by_id(root, info, id):
        try:
            return Bio.objects.get(id=id)
        except Bio.DoesNotExist:
            return None
        
    def resolve_all_bios(root, info):
        return Bio.objects.all()
    
    def resolve_socials(root, info):
        return Social.objects.all()
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    created = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, **kw):
        user = User(**kw)
        user.save()
        return CreateUser(created=True, user = user)

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    updated = graphene.Boolean()
    class Arguments:
        id = graphene.ID()
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, id, username, first_name, last_name):
        user = User.objects.get(id=id)
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        return UpdateUser(user=user, updated=True)

class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)
    deleted = graphene.Boolean()
    class Arguments:
        id = graphene.Int()
    
    def mutate(self, info, id):
        user = User.objects.get(id=id)
        user.delete()
        return DeleteUser(deleted = True, user=user)
class CreateUserBio(graphene.Mutation):
    created = graphene.Boolean()
    user_bio = graphene.Field(BioType)
    class Arguments:
        body  =  graphene.String()
        user_id = graphene.Int()
        img = Upload()

    def mutate(self, info, user_id, body):
        user = User.objects.get(id = user_id)
        user_bio = Bio(
            user = user,
            body=body
        )
        user_bio.save()
        return CreateUserBio(created = True, user_bio=user_bio)
    
class UpdateUserBio(graphene.Mutation):
    updated = graphene.Boolean()
    bio = graphene.Field(BioType)
    class Arguments:
        id = graphene.Int()
        body = graphene.String()
        user_id = graphene.Int()
        img = Upload()
        
    def mutate(self, info, user_id, body, img=None):
        user = User.objects.get(id=user_id)
        user.body = body
        match img:
            case None: pass
            case _:
                if user.img:
                    user.img.delete()
                user.img = img
        user.save()
        return UpdateUserBio(updated=True, user=user)
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_user_bio = CreateUserBio.Field()
    update_user_bio = UpdateUserBio.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)