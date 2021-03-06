"""meberpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from.import views
from signup.views import login_view
from .views import logout



app_name='index'


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^members/', include('members.urls'), name='meberpage'),
    url(r'^$',include('homepage.urls'),name='homepage'),
    url(r'^memberapi/',views.MemberList.as_view(),name='restapi'),
    url(r'^register/',include('signup.urls'),name='register'),
    url(r'^login/',views.login_view,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
]

urlpatterns=format_suffix_patterns(urlpatterns)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
