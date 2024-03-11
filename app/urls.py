from django.urls import path
from .views import List, Create, Detail, Update, Delete

urlpatterns = [
    path('', List.as_view(), name='home'),
    path('create/', Create.as_view(), name='create'),
    path('<int:pk>/', Detail.as_view(), name='detail'),
    path('<int:pk>/update/', Update.as_view(), name='update'),
    path('<int:pk>/delete/', Delete.as_view(), name='delete'),
]