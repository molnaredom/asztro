"""weboldal URL Configuration

The `urlpatterns` list routes URLs to views_module. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views_module
    1. Add an import:  from my_app import views_module
    2. Add a URL to urlpatterns:  path('', views_module.home, name='home')
Class-based views_module
    1. Add an import:  from other_app.views_module import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', include('home.urls')),
    path('', include('base.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
