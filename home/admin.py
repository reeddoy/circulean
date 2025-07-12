from django.contrib import admin
from home.models import *       
from django.utils.html import format_html


# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('-created_at',)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_preview', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('-created_at',)
    exclude = ('slug',)
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 30px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview', 'created_at')
    search_fields = ('name', 'category', 'price')
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('-created_at',)
    exclude = ('slug',)
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 30px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('-created_at',)
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('-created_at',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 30px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


class WebsiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False  # disables "Add" button

    def has_delete_permission(self, request, obj=None):
        return False  # disables "Delete" option


class OfficeInformationAdmin(admin.ModelAdmin):
    list_display = ('name','phone', 'email', 'created_at')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('created_at',)
    list_per_page = 50
    ordering = ('created_at',)
    

class FooterImageAdmin(admin.ModelAdmin):
    list_display = ('id','image_preview', 'created_at')
    ordering = ('created_at',)
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 30px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Website_Setting, WebsiteSettingAdmin)
admin.site.register(Office_information, OfficeInformationAdmin)
admin.site.register(Footer_Image, FooterImageAdmin)