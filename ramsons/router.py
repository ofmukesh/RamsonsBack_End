from rest_framework.routers import DefaultRouter
from company.views import ComapnyView
from company.views import ComapnyView
from test.views import TestView
from manager.views import Permission_View, Register

router = DefaultRouter()
router.register("m", TestView, "test")
router.register("register", Register, "register")
router.register("permission", Permission_View)
router.register('company', ComapnyView)
