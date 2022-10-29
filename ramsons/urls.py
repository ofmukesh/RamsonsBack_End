from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from company.views import ComapnyView
from test.views import TestView
from manager.views import Permission_View, Register

admin.site.site_header = "Ramsons Administration"
admin.site.site_title = "Super Admin"

router = routers.DefaultRouter()
router.register(r"m", TestView, "test")
router.register(r"permission", Permission_View, "permission")
router.register(r"register", Register, "register")
router.register(r"company", ComapnyView, "company")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
