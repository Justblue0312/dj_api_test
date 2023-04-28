from django.urls import path
from .views import ListUser, RetriveUser, CreateUser, UpdateUser, DeleteUser

urlpatterns = [
    path("list-user/", ListUser.as_view()),
    path("retrieve-user/<str:pk>/", RetriveUser.as_view()),
    path("create-user/", CreateUser.as_view()),
    path("update-user/<str:pk>/", UpdateUser.as_view()),
    path("delete-user/<str:pk>/", DeleteUser.as_view()),
]
