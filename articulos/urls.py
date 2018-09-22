"""BlogPersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path
from .views import *

app_name = "articulos"

urlpatterns = [
    path('', ArticlesList.as_view(), name='list_articles'),
    path('filter/', ArticlesListFilter, name='list_filter_articles'),
    path('verArticulo/<slug:slug>/', ArticlesVer.as_view(), name='ver_articles'),
    path('nuevoArticulo/', ArticlesCreate.as_view(), name='crear_articles'),
    path('EditArticulo/<int:pk>/', ArticlesUpdate.as_view(), name='edit_articles'),
    path('borrarArticulo/<int:pk>/', ArticlesDelete.as_view(), name='borrar_articles'),

]
