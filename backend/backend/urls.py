from django.contrib import admin
from django.urls import path, include, re_path
#from rest_framework.routers import DefaultRouter
"""
from user.views import UserView
from bio.views import BioView
from social.views import SocialView
from main.views import MainView
"""
from django.views.decorators.cache import cache_page
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
   openapi.Info(
      title="FindMe API",
      default_version='v1',
      description="Findme",
      terms_of_service="https://moriire.github.io/mo",
      contact=openapi.Contact(email="ibmabdulsalam@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
"""
d_router = DefaultRouter()
d_router.register("user", UserView)
d_router.register("bio", BioView)
d_router.register("social", SocialView)
d_router.register("main", MainView)
"""
from .schema import schema
urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    #path("api/", include(d_router.urls))
]+[
   #path('documentation<format>/',  cache_page(60 * 15)(schema_view.without_ui(cache_timeout=0)), name='schema-json'),
   #path('documentation/',  cache_page(60 * 15)(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
   path('docs/',  cache_page(60 * 15)(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
  
]
