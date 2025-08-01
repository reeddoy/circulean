from django.shortcuts import render, redirect
from home.models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
import threading
from datetime import datetime
from django.conf import settings


# Create your views here.
def home(request):
    website, created = Website_Setting.objects.get_or_create(id=1)
    products = Product.objects.order_by('-id')[:6]
    blogs = Blog.objects.order_by('-id')[:3]
    return render(request, 'home.html', {'website': website, 'products': products, 'blogs': blogs})



# Async Email Sender
def send_contact_email(subject, message, recipient_list):
    threading.Thread(
        target=send_mail,
        args=(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list),
        kwargs={'fail_silently': False}
    ).start()

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name') or ''
        email = request.POST.get('email') or ''
        phone = request.POST.get('phone') or ''
        subject = request.POST.get('subject') or ''
        message = request.POST.get('message') or ''
        try:
            temp = Contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
            temp.save()
            website = Website_Setting.objects.first()
            if website.contact_email_notification:
                try:
                    send_contact_email(
                        subject=f'New Contact Form Submission at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
                        message=f'Submitted Form Credentials are- \n\nName: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}',
                        recipient_list=[website.contact_email],)
                except:
                    pass
            messages.success(request, 'Successfully Submitted.')
            return redirect(request.get_full_path())
        except:
            messages.error(request, 'Something went wrong.')
            return redirect(request.get_full_path())
        
    headoffice = Office_information.objects.first()
    office_info = Office_information.objects.all().exclude(id=headoffice.id)
    return render(request, 'contact.html', {'headoffice': headoffice, 'office_info': office_info})


def about(request):
    return render(request,'about.html')

def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})



def blog_details(request, id):
    try:
        blog = Blog.objects.get(id=id)
        last_post = Blog.objects.order_by('-id')[:3]
        return render(request,'blog-details.html', {'blog': blog, 'last_post': last_post})
    except:
        messages.error(request, 'Blog not found.')
        return redirect('/blog/')


def product(request, slug):
    try:
        if slug == 'all':
            products = Product.objects.all().order_by('-id')
            category_name = 'All'
        else:
            category = Category.objects.get(slug=slug)
            products = Product.objects.filter(category=category).order_by('-id')
            category_name = category.name
        
        # Add pagination
        paginator = Paginator(products, 9)  # Show 9 products per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, 'product.html', {
            'products': page_obj,
            'category': category_name
        })
    except:
        messages.error(request, 'Category not found.')
        return redirect('/')




def submit_newsletter(request):
    if request.method == 'POST':
        n_email = request.POST.get('newsletter_name')
        try:
            temp = Newsletter.objects.create(email = n_email)
            temp.save()
            messages.success(request, 'Successfully Submitted.')
            return redirect(request.get_full_path())
        except:
            messages.error(request, 'Something went wrong.')
            return redirect(request.get_full_path())
    else:
        return redirect('/')



def internal_partners(request):
    return render(request, 'internal-partners.html')

def services(request):
    return render(request, 'services.html')

def merchandise_sourcing(request):
    return render(request, 'merchandise-sourcing.html')

def product_quality_audit(request):
    return render(request, 'product-quality-audit.html')