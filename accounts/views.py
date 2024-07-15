from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact, Favorites, Payments
from django.contrib.auth.decorators import login_required
from cars.models import Car
from accounts.models import Refunds




# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')     

    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect ('dashboard')
                    # messages.success(request, 'You are registered successfully')
                    # return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=request.user.id)
    data = {
        'inquiries':user_inquiry
    }
    return render(request, 'accounts/dashboard.html',data)



@login_required(login_url='login')
def favorites(request):
    user_favorites = Favorites.objects.order_by('-created_date').filter(user_id=request.user.id)
    data = {
        'favorites':user_favorites
    }
    return render(request, 'accounts/favorites.html', data)

def remove_from_favorites(request, car_id):
    if request.user.is_authenticated:
        favorite = get_object_or_404(Favorites, user_id=request.user.id, car_id=car_id)
        favorite.delete()
        messages.success(request, 'The car has been removed from your favorites.')
    else:
        messages.error(request, 'You need to be logged in to remove a favorite.')
    
    return redirect('favorites')  # Redirect to the favorites page

@login_required(login_url='login')
def payments(request):
    user_payments = Payments.objects.order_by('-trial_date').filter(user_id=request.user.id)
    data = {
        'payments':user_payments
    }
    return render(request, 'accounts/bookings.html', data)

def remove_from_bookings(request, car_id):
    if request.method == 'POST' and request.user.is_authenticated:
        user_id = request.user.id
        bookings = Payments.objects.filter(car_id=car_id, user_id=user_id)

        if bookings.exists():
            # Delete all bookings for this car and user
            bookings.delete()

            # Extract refund details from the POST request
            user_refund_id = request.POST.get('user_id')
            car_refund_id = request.POST.get('car_id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            car_title = request.POST.get('car_title')

            # Create a new refund entry
            refund = Refunds(
                user_refund_id=user_refund_id, 
                car_refund_id=car_refund_id, 
                first_name=first_name, 
                last_name=last_name, 
                car_title=car_title,
            )
            refund.save()

            messages.success(request, 'Booking removed successfully. Your payment will be refunded within 2-3 working days.')
        else:
            messages.error(request, 'No booking found to remove.')
    else:
        messages.error(request, 'You need to be logged in to remove a booking.')

    return redirect('bookings')  # Replace with your actual redirect URL


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logged out')
        return redirect('home')
    return redirect('home')
