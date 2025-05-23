from django.urls import path
from . import views
# Removed import of Ion OAuth views
# from .views import IonLoginView, IonLogoutView, IonCallbackView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    # Removed Ion OAuth URL patterns from here, they are now in ion_auth/urls.py
    # path('login/', IonLoginView.as_view(), name='login'),
    # path('logout/', IonLogoutView.as_view(), name='logout'),
    # path('oauth/redirect', IonCallbackView.as_view(), name='ion_callback'),
] 