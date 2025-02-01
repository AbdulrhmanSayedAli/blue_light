from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from common.rest_framework.permissions import IsSuperuser
from rest_framework.authentication import SessionAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Blue Light Apis",
        default_version="v1",
    ),
    public=True,
    permission_classes=(IsSuperuser,),
    authentication_classes=[SessionAuthentication],
)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/users/", include("users.urls")),
        path("api/auth/", include("myauth.urls")),
        path("api/courses/", include("courses.urls")),
        path("api/home/", include("home.urls")),
        path("api/uploader/", include("uploader.urls")),
        path("api/enums/", include("enums.urls")),
        path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    ]
    + staticfiles_urlpatterns()
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
