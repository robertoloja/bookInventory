"""bookInv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inventory import views
from inventory.views import UpdateBook

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^modify/', views.modifyBook, name='modifyBook'),
    url(r'^modLocations/', views.modifyLocations, name='modifyLocations'),
    url(r'^savemod/(?P<pk>[\w-]+)/$', UpdateBook.as_view(), name='update_book'),
    url(r'^admin/', admin.site.urls),
]
