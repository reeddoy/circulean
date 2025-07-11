from django.urls import path
from home import views




urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/<int:id>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    
    
    
    
    path('submit_newsletter/', views.submit_newsletter, name='submit_newsletter'),
]