from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    
    
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('admin/logout', views.logout, name='logout'),
    path('generate-blog', views.generate_blog, name='generate-blog'),
    path('history', views.blog_list, name='history'),
    path('details/<int:pk>/', views.blog_details, name='details'),
]