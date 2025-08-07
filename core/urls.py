from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import index

schema_view = get_schema_view(
    openapi.Info(
        title="Content Moderation API",
        default_version='v1',
        description="API for automated classification of user-generated content using AI models.",
        contact=openapi.Contact(email="framonmar7@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
