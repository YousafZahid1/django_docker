"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# Import your Ion OAuth views from the blog app - REMOVED
# from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Explicitly handle the root URL by including blog.urls
    path('', include('blog.urls')),
    # Include the URLs from the new ion_auth app at the root level
    path("oauth/", include("ion_auth.urls")),
    # Removed Ion OAuth URLs defined directly
    # path("oauth/", blog_views.IonLoginView.as_view(), name="oauth2"),
    # path("oauth/redirect", blog_views.IonCallbackView.as_view(), name="redirect"),
    # path("oauth/logout", blog_views.IonLogoutView.as_view(), name="logout"),
]
