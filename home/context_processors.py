from .models import Category, Footer_Image


def all_u_categories(request):
    category_u_list = Category.objects.all()
    return {
        'category_u_list': category_u_list
    }



def footer_images(request):
    images = Footer_Image.objects.all()
    return {
        'footer_image_list': images
    }


