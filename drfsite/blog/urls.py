from django.urls import path
from .views import *

urlpatterns = [
#     path('api/post/', views.PostListCreate.as_view({'get': 'list', 'post': 'create'})),
#     path('api/post/<int:pk>', views.PostListCreate.as_view({'delete': 'destroy'})),
    path('', post_lists),
    path('test/', checkName)
]
