from django.contrib import admin
from django.urls import path, include
from .import views
app_name = 'predict'
urlpatterns = [
    path('',views.predict,name = 'predict'),
    path('predict_iris', views.predict_iris, name='predict_iris'),
    path('results/', views.view_results, name='results'),
]
