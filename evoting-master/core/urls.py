from django.urls import path
from core import views

urlpatterns = [

    path('', views.show_base, name='home'),
    path('voting-page', views.show_voting_page, name='voting-page'),
    path('results-page', views.show_results, name='results-page'),

]
