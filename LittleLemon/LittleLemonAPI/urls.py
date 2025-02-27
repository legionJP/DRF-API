from importlib.resources import path

from django import views 
from  LittleLemonAPI.views import User

urlpatterns = [
    path('Users/', views.User.as_view()),
]