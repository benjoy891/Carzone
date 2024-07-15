from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact, Favorites, Payments
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def inquiry(request):
     if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)


        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            "You have a new inquiry for the car "+car_title+'. Please login to your admin panel for more info',
            "futuresync101@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly')
        return redirect('/cars/'+car_id)
        

def favorite(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            already_done = Favorites.objects.all().filter(car_id=car_id, user_id=user_id)
            if already_done:
                messages.error(request, "This car is already added to Favorites.")
                return redirect('/cars/'+car_id)
            
        favorite = Favorites(car_id=car_id, car_title=car_title, user_id=user_id)
        favorite.save()
        messages.success(request, 'Added to Favorites')
        return redirect('/cars/'+car_id)


@csrf_exempt
def payment(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        trial_date = request.POST['trial_date']
        state = request.POST['state']
        city = request.POST['city']
        pincode = request.POST['pincode']
        street = request.POST['street']
        phone = request.POST['phone']
        
        if len(phone) > 10:
            messages.error(request,"Please enter a valid number")
            return redirect('/cars/'+car_id)
            
        payment = Payments(user_id=user_id, car_id=car_id,car_title=car_title, firstname=firstname, lastname=lastname, trial_date=trial_date, state=state, city=city, pincode=pincode,street=street, phone=phone)
        payment.save()
        messages.success(request, 'Booking complete.')
        return redirect('/cars/'+car_id)
    
