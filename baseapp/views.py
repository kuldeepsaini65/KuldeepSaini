from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


def home(request):
    work = Experience.objects.filter(type='work').order_by('joining_date')[::-1]
    education = Experience.objects.filter(type='education').order_by('joining_date')[::-1]
    context = {
        'workexp' : work,
        'educationexp' : education  
    }
    
    if request.method == "POST":
        fname = request.POST.get('conName')
        lname = request.POST.get('conLName')
        email = request.POST.get('conEmail')
        phone = request.POST.get('conPhone')
        service = request.POST.get('conService')
        message = request.POST.get('conMessage')
        try:
            data = ContactForm(fname = fname, lname = lname, email = email, phone = phone, services = service, message = message)
            data.save()
            messages.success(request, "Message Sent Successfuly !")
            return redirect('home')
            # return JsonResponse({'success': True})
        
            

            
        except Exception as e:
            messages.error(request, e)
            return redirect('home')
            # return redirect('/home?success=False')
            # return JsonResponse({'success': False})

    return render(request, 'index.html', context=context)

def about(request):
    work = Experience.objects.filter(type='work').order_by('joining_date')[::-1]
    education = Experience.objects.filter(type='education').order_by('joining_date')[::-1]
    context = {
        'work' : work,
        'education' : education  
    }
        
    return render(request, 'about.html', context=context)

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def blogs(request):
    return render(request, 'blog.html')

def blogsDetails(request):
    return render(request, 'blog-details.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('conName')
        lname = request.POST.get('conLName')
        email = request.POST.get('conEmail')
        phone = request.POST.get('conPhone')
        service = request.POST.get('conService')
        message = request.POST.get('conMessage')
        try:
            data = ContactForm(fname = fname, lname = lname, email = email, phone = phone, services = service, message = message)
            data.save()
            messages.success(request, "woowwow")
            # return redirect('home')
            return redirect('/contact?success=True')
            
            
        except Exception as e:
            messages.error(request, e)
            return redirect('home')

    return render(request, 'contact.html')


def privacy_policy(request):
    return render(request,'basic_pages/privacy_policy.html')


def termsconditions(request):
    return render(request, 'basic_pages/terms_and_conditions.html')
def refund(request):
    return render(request, 'basic_pages/refund.html')
def shipping(request):
    return render(request, 'basic_pages/shipping.html')