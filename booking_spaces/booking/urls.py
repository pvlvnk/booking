from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.index, name='index'),
    path('reserving/<slug:slug>/', views.space_reserving, name='space_reserving'),
    path('reserving/<slug:slug>/<str:username>', views.reserve_edit, name='reserve_edit'),
    path('schedule/', views.CreateSchedule, name='create_schedule'),
    path('info/', views.InfoView.as_view(), name='info'),
]