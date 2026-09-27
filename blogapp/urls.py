from django.urls import path
from .views import home,about,post_detail,user_posts

app_name = 'blogapp'

urlpatterns = [
    path('', home),
    path('about/', about),
    path('post/<int:post_id>/', post_detail),
    path('user/<str:username>/',user_posts),
]
