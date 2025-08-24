from .models import Category


def all_u_categories(request):
    category_u_list = Category.objects.all().order_by('sl')
    return {
        'category_u_list': category_u_list
    }






