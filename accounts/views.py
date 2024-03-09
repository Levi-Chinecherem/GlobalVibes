# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .models import CustomUser
User = CustomUser

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'  # your template for entering the email

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')  # Assuming your form has an 'email' field
        user = User.objects.filter(email=email).first()

        if user:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = reverse_lazy('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})
            reset_link = f"{request.scheme}://{request.get_host()}{reset_url}"

            # Send the reset link to the user via email
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_link}',
                'info@globalvibes.net',
                [email],
                fail_silently=False,
            )

        # Redirect to a confirmation page
        return render(request, 'accounts/password_reset_sent.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_image = request.FILES.get('profile_image')  # Retrieve the uploaded file

        try:
            user = CustomUser.objects.create_user(
                email=email,
                username=username,
                password=password,
            )

            if profile_image:
                user.profile_image = profile_image
                user.save()

            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')  # Replace 'home' with your home page URL

        except Exception as e:
            # Handle any errors (e.g., duplicate email, username) and provide appropriate feedback
            messages.error(request, f'Error creating account: {e}')

    return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Replace 'home' with your home page URL
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'accounts/signin.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('home')  # Replace 'home' with your home page URL
        else:
            messages.error(request, 'Please correct the error below.')

    form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')  # Replace 'home' with your home page URL

