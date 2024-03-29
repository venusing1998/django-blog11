"""djangoblog URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from index import views as index_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("index.urls", namespace="index", app_name="index")),
    url(r"^account/", include("account.urls",
                              namespace="account", app_name="account")),
    url(r"^blog/", include("blog.urls", namespace="blog", app_name="blog")),
    url(r"^article/", include("article.urls",
                              namespace="article", app_name="article")),
    url(r'^home/', TemplateView.as_view(template_name="home.html"), name="home"),
]
