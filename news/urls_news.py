
from django.urls import path


# Импортируем созданное нами представление
from .views import PostsList, PostsListSearch, PostDetail, ArtDetail
# , ProductDetail
# from .views import ProductsList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
from .views import PostCreate, PostUpdate, PostDelete, ArtCreate, ArtUpdate, ArtList, ArtDelete, ArtListSearch

# from django.urls import path
# from .views import (
#     PostsList, PostsListSearch, PostDetail,
#     PostCreatePermission, PostUpdate, PostDelete,
#     ArtCreate, ArtUpdate, ArtList, ArtDetail, ArtDelete, ArtListSearch
# )

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   # path('', PostsList.as_view()),

   # ПОСЛЕДУЮЩЕЕ БУДЕТ ПОЗЖЕ
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения

   # path('news/', PostsList.as_view(), name='post_list'),
   # path('news/search/', PostsListSearch.as_view()),
   # path('news/<int:pk>', PostDetail.as_view(), name='post_list_uno'),
   # # path('create/', create_product, name='product_create'),
   # path('news/create/', PostCreate.as_view(), name='post_create'),
   # path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   # path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

# ссылается на способы создания из программы news/views
   path('', PostsList.as_view(), name='post_list'),
   path('search/', PostsListSearch.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='post_list_uno'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]

