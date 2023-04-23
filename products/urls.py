from django.urls import path
from .views import (
    ListProduct,
    ListCategory,
    RetriveProduct,
    RetriveCategory,

    CreateProduct,
    UpdateProduct,
    DestroyProduct
)

urlpatterns = [
    path('list-product/', ListProduct.as_view()),
    path('list-category/', ListCategory.as_view()),
    path('retrieve-product/<str:slug>/', RetriveProduct.as_view()),
    path('retrieve-category/<str:slug>/', RetriveCategory.as_view()),

    path('create-product/', CreateProduct.as_view()),
    path('update-product/<int:pk>/', UpdateProduct.as_view()),
    path('delete-product/<int:pk>/', DestroyProduct.as_view()),

]
