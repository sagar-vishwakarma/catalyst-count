
from django.urls import path
from .views import home,upload,query,user_add,logout,login,user_form
urlpatterns = [
    path('login/',login),
    path('home/',home),
    path('upload/',upload),
    path('query/',query),
    path('user-add/',user_add),
    path('logout/',logout),
    path('user_form/',user_form)
]