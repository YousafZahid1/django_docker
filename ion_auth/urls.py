from django.urls import path
from . import views

urlpatterns = [
    path("", views.IonLoginView.as_view(), name="oauth2"),
    path("redirect", views.IonCallbackView.as_view(), name="redirect"),
    path("logout", views.IonLogoutView.as_view(), name="logout"),
] 