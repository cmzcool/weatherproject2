from django.urls import path

from . import views

app_name = 'weatherapp'
urlpatterns = [
    path('', views.weather, name='weather'),
    path('home.html', views.home, name='home'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('thefuture.html', views.future, name='future'),
    path('feedback.html', views.feedback, name='feedback'),

    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]