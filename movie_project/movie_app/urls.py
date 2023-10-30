from django.urls import path
from . import views
app_name = 'movie_app'
urlpatterns = [
    path('', views.index, name="index"),
    path('movie/<int:movie_id>/', views.Details, name='Details'),
    path('add/', views.Add_Movie, name='Add_Movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')

]

