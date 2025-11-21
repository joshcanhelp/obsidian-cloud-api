from django.urls import path

from . import views

urlpatterns = [
    path("", views.root, name="root"),
    path("register", views.userRegistration, name="userRegistration"),
    path("vaults", views.vaultList, name="vaultList"),
    path("keys", views.keyList, name="keyList"),
    path("actions", views.actionList, name="actionList"),
]
