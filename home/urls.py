from django.urls import path
from home import views




urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/<int:id>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('internal-partners/', views.internal_partners, name='internal_partners'),
    path('services/', views.services, name='services'),
    path('merchandise-sourcing/', views.merchandise_sourcing, name='merchandise_sourcing'),
    path('product-quality-audit/', views.product_quality_audit, name='product_quality_audit'),
    
    
    
    
    path('submit_newsletter/', views.submit_newsletter, name='submit_newsletter'),
]