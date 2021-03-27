
from django.urls import include, path

from . import views

app_name='accounts'

urlpatterns = [
    path('home',views.home , name='home'),
    path('start',views.start , name='start'),
    path('go_to',views.go_to , name='go_to'),

]