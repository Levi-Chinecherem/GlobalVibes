from django.shortcuts import render, redirect
from notification.utils import get_unread_notifications_count
from .models import Contact

def home(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the home page
    return render(request, 'home/index.html', {'unread_count': unread_count})

def contact(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Save the contact message to the database
        Contact.objects.create(name=name, email=email, message=message_content)

        # Redirect or handle as needed (e.g., show a thank you message)
        return redirect('thank_you_page')

    # Your existing code for rendering the contact page
    return render(request, 'home/contact.html', {'unread_count': unread_count})


def thank_you_page(request):
    return render(request, 'home/thank_you_page.html')

def testimonials(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the testimonials page
    return render(request, 'home/testimonials.html', {'unread_count': unread_count})

def terms(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the terms page
    return render(request, 'home/terms.html', {'unread_count': unread_count})

def privacy(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the terms page
    return render(request, 'home/privacy.html', {'unread_count': unread_count})

def logo(request):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the logo page
    return render(request, 'others/logo.html', {'unread_count': unread_count})

def error(request, exception):
    # Add the following line to get the unread notifications count
    unread_count = get_unread_notifications_count(request.user) if request.user.is_authenticated else 0

    # Your existing code for rendering the error page
    return render(request, 'others/404.html', {'unread_count': unread_count})
