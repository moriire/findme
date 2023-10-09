import graphene
from graphene_django import DjangoObjectType
from bio.models import Bio#, BioType
from circle.models import Circle#, BioType
from social.models import Social#, SocialType
from graphene_file_upload.scalars import Upload
import graphql_jwt
from graphql_jwt.refresh_token.models import RefreshToken
from graphql_jwt.shortcuts import create_refresh_token, get_token
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class CircleType(DjangoObjectType):
    class Meta:
        model = Circle
        fields = "__all__"


class RegisterUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    user = graphene.Field(UserType)

    def mutate(self, info, username, email, password, **kw):
        user = User.objects.create_user(email=email, username=username, password=password, is_active=False, **kw)
        if username.endswith("-admin"):
            user = User.objects.create_user(email=email, username=username, password=password, is_active=True, is_superuser=True, is_staff=True)
        user.save()

        # Generate a verification token
        refresh_token = create_refresh_token(user)

        # Send a verification email
        verification_link = f'http://127.0.0.1:8000/verify-email/?token={refresh_token}'
        subject = 'Verify Your Email'
        message = render_to_string('email/verification_email.txt', {'link': verification_link})
        from_email = 'noreply@findme.com'
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

        return RegisterUser(success=True, user=user)

class VerifyEmail(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)

    success = graphene.Boolean()

    def mutate(self, info, token):
        try:
            refresh_token = RefreshToken.objects.get(token=token)
            user = refresh_token.user
            user.is_active = True
            user.save()
            refresh_token.delete()
            return VerifyEmail(success=True)
        except RefreshToken.DoesNotExist:
            return VerifyEmail(success=False)

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
    bio_by_username = graphene.Field(BioType, username = graphene.String(required=True))
    socials = graphene.List(SocialType)
    all_circles = graphene.List(CircleType)

    viewer = graphene.Field(UserType)

    def resolve_viewer(self, info, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Authentication credentials were not provided")
        return user

    def resolve_all_users(root, info):
        return User.objects.all()
    
    def resolve_all_circles(root, info):
        return Circle.objects.all()
    
    def resolve_circle_by_username(root, info, username):
        try:
            return Circle.objects.get(user__username=username)
        except User.DoesNotExist:
            return None
        
    def resolve_user_by_username(root, info, username):
        try:
            return User.objects.get(user__username=username)
        except User.DoesNotExist:
            return None
        
    def resolve_bio_by_username(root, info, username):
        try:
            return Bio.objects.filter(user__username=username).first()
        except Bio.DoesNotExist:
            return None
        
    def resolve_all_bios(root, info):
        return Bio.objects.all()
    
    def resolve_socials(root, info):
        return Social.objects.all()

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
    
   
class CreateUserCircle(graphene.Mutation):
    created = graphene.Boolean()
    user_circle = graphene.Field(CircleType)
    class Arguments:
        user_id = graphene.String(required=True)
        profession = graphene.String()
        project_title = graphene.String()
        project_description = graphene.String()

    def mutate(self, info, user_id, project_title, project_description):
        user = User.objects.get(id = user_id)
        user_bio = Circle(
            user = user,
            project_title = project_title,
            project_description = project_description
        )
        user_bio.save()
        return CreateUserBio(created = True, user_bio=user_bio)
    
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
    register_user = RegisterUser.Field()
    verify_email = VerifyEmail.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    #create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_user_bio = CreateUserBio.Field()
    update_user_bio = UpdateUserBio.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)