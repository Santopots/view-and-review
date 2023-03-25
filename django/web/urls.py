from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('film/<pk>', views.FilmView.as_view(), name='film'),
    # path('accounts/', include())
]