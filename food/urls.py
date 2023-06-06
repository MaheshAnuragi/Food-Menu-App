from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # /food
    # path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    # /food/1
    # path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.DetailClassView.as_view(),name='detail'),
    # add food item
    path('add/',views.create_item,name='create_item'),
    # path('add/',views.CreateItemClassView.as_view(),name='create_item'),
    # edit food item
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    # delete an food item
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
]
