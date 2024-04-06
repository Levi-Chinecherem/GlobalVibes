
from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('logo/', v.logo, name='logo'),
    path('contact/', v.contact, name='contact'),
    path('testimonials/', v.testimonials, name='testimonials'),
    path('404/', v.error, name='error'),
    path('terms/', v.terms, name='terms'),
    path('privacy/', v.privacy, name='privacy'),
    path('thank-you/', v.thank_you_page, name='thank_you_page'),
]
