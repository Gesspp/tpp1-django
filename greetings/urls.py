from django.urls import path
from . import views


urlpatterns = [
    path('hello/<str:name>', views.hello, name='hello'),
    path('stats/', views.stats, name='stats'),
    path('ststs/<str:name>', views.ststs, name='ststs'),
    # path('', views.index, name='index'),
]