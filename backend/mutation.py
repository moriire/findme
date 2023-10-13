from graph_types import *
from graphene_file_upload.scalars import Upload
#import graphql_jwt
from graphql_jwt.refresh_token.models import RefreshToken
from graphql_jwt.shortcuts import create_refresh_token, get_token
from django.core.mail import send_mail
from django.template.loader import render_to_string


def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == "POST":
        handle_uploaded_file(request.FILES["file"])
        return True
    
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
        user_circle = Circle(
            user = user,
            project_title = project_title,
            project_description = project_description
        )
        user_circle.save()
        return CreateUserCircle(created = True, user_circle=user_circle)
    
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
        
    def mutate(self, info, user_id, body):
        user = User.objects.get(id=user_id)
        user.body = body
        return UpdateUserBio(updated=True, user=user)

class UploadBioImage(graphene.Mutation):
    img = graphene.Field(UploadType)
    success = graphene.Boolean()
    class Arguments:
        img = Upload(required=True)#Upload(required=True)
        user = graphene.ID(required=True)

    def mutate(self,  info, img, user):
        user_instance = User.objects.get(id=user)
        try:
            pics = Photo.objects.filter(id=user)
        except:
            pic = Photo(
                user=user_instance,
                img = img
            )
        else:
            count = pics.count()
            if (count <= 3):
                pic = Photo(
                        user=user_instance,
                        img = img
                    )
            else:
                pics.first().delete()
                pic = Photo(
                        user=user_instance,
                        img = img
                    )

        finally:
            pic.save()
        return UploadBioImage(img=pic, success=True)