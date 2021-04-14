from django.urls import include, path
from . import views

urlpatterns = [
  path('welcome', views.welcome),
  path('getapi/<slug:typee>', views.get_api),
  path('addapi/<slug:typee>', views.add_api),
  path('updateapi/<slug:typee>/<int:song_id>', views.update_api),
  path('deleteapi/<slug:typee>/<int:song_id>', views.delete_api)
]