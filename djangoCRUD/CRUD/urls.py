from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
	# READ
	path('', views.Index.as_view(), name='read'),
	# CREATE
	path('new/', views.new, name='new'),
	path('create/', views.create, name='create'),
	# UPDATE
	path('edit/<int:pk>/', views.Edit.as_view(), name='edit'),
	path('update/<int:contact_id>/', views.update, name='update'),
	# DELETE
	path('remove/<int:pk>/', views.Remove.as_view(), name='remove'),
	path('delete/<int:contact_id>/', views.delete, name='delete'),
]