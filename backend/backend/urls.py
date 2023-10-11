from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from .schema import schema
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
def index(request):
    return redirect("/graphql")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path("graphql", csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
]