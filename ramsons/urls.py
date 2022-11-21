from django.contrib import admin
from django.urls import path, include
from ramsons.router import router

admin.site.site_header = "Ramsons Administration"
admin.site.site_title = "Super Admin"

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
