from django.urls import path

from booking import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('reserving/<slug:slug>/', views.space_reserving, name='space_reserving'),
    path('reserving/<slug:slug>/<str:username>/', views.reserve_edit, name='reserve_edit'),
    path('create_schedule/', views.CreateSchedule, name='create_schedule'),
    path('delete_schedule/', views.DeleteSchedule, name='delete_schedule'),
    path('create_space/', views.CreateSpace, name='create_space'),
    path('delete_space/', views.DeleteSpace, name='delete_space'),
    path('info/', views.InfoView.as_view(), name='info'),
]
