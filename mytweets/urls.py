"""mytweets URL Configuration

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
# from django.conf.urls import url
# from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from tweets.views import Index,Profile
import tweets

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'$', views.index, name = 'index')
#     url(r'^admin/', Index.as_view()),
# ]

urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view()),
    url(r'^user/(\w+)/$', Profile.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
