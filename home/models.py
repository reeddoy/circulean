from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
        
    def __str__(self):
        return self.name


    
class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    
    
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Blog(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = CKEditor5Field('Text', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    

    
class Newsletter(models.Model):
    email = models.EmailField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email



class Website_Setting(models.Model):
    new_arrival_feature_display = models.BooleanField(default=False)
    contact_email_notification = models.BooleanField(default=False)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return "Website Setting"
    
    



