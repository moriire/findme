from graphene_file_upload.scalars import Upload
import graphql_jwt
from graphql_jwt.refresh_token.models import RefreshToken
from graphql_jwt.shortcuts import create_refresh_token, get_token
from django.core.mail import send_mail
from query import *
from mutation import (
                      RefreshToken, 
                      RegisterUser, 
                      VerifyEmail, 
                      UpdateUserBio, 
                      UpdateUser, 
                      UploadBioImage,
                      CreateUserBio, 
                      CreateUserCircle,
                      DeleteUser
                      )

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    verify_email = VerifyEmail.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    #create_user = CreateUser.Field()
    upload_image = UploadBioImage.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_user_bio = CreateUserBio.Field()
    update_user_bio = UpdateUserBio.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)