import graphene
from graph_types import *

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
