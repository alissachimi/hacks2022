"""hacks2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('home.html', views.homepage),
    path('page2.html', views.page2),
    path('miles.html', views.miles),
    path('a2000.html', views.a2000),
    path('a2001.html', views.a2001),
    path('a2002.html', views.a2002),
    path('a2003.html', views.a2003),
    path('a2004.html', views.a2004),
    path('a2005.html', views.a2005),
    path('a2006.html', views.a2006),
    path('a2007.html', views.a2007),
    path('a2008.html', views.a2008),
    path('a2009.html', views.a2009),
    path('a2010.html', views.a2010),
    path('a2011.html', views.a2011),
    path('a2012.html', views.a2012),
    path('a2013.html', views.a2013),
    path('a2014.html', views.a2014),
    path('a2015.html', views.a2015),
    path('yay.html', views.yay),

]
