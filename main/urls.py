from django.urls import path

from main import views

urlpatterns =[
    path('random/', views.dariha),
    path('', views.BlogListView.as_view()),
    path('<int:pk>/', views.BlogDetailView.as_view()),
    path('create/', views.BlogCreateView.as_view()),
    path('<int:pk>/change/', views.BlogChange.as_view()),

]