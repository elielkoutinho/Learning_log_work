from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
	path('', views.index, name='index'),

	path('topics/', views.topics, name='topics'),

	path('topics/<topic_id>/', views.topic, name='topic'),

	# Página para adicionar um novo assunto 
	path('new_topic/', views.new_topic, name='new_topic'),

	]

