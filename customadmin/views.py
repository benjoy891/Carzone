from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from cars.models import Car
from pages.models import Team
from contacts.models import Contact, Favorites, Payments
import os 
from accounts.models import Refunds
import razorpay
from django.views.decorators.csrf import csrf_exempt






def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('admin_dashboard')
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect('admin_dashboard')
            
            messages.info(request, 'Invalid Password')
            return redirect('/')
        
        return render(request, 'admin_login.html')
    
    except Exception as e:
        print(e)
        


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_cars(request):
    cars = Car.objects.order_by('-created_at')
    data = {
        'cars':cars,
    }
    return render(request, 'admin_car.html',data)



def update_car(request, pk):
    car = Car.objects.get(id=pk)
    if request.method == 'POST':
        car.car_title = request.POST.get('car_title')
        car.state = request.POST.get('state')
        car.city = request.POST.get('city')
        car.color = request.POST.get('color')
        car.year = request.POST.get('year')
        car.condition = request.POST.get('condition')
        car.price = request.POST.get('price')
        car.description = request.POST.get('description')
        # Handle file uploads
        photo_fields = ['car_photo', 'car_photo_1', 'car_photo_2', 'car_photo_3', 'car_photo_4']
        for field in photo_fields:
            if field in request.FILES:
                file_field = getattr(car, field)
                if file_field and hasattr(file_field, 'path') and os.path.exists(file_field.path):
                    os.remove(file_field.path)
                setattr(car, field, request.FILES[field])

        car.features = request.POST.getlist('features')
        car.body_style = request.POST.get('body_style')
        car.engine = request.POST.get('engine')
        car.transmission = request.POST.get('transmission')
        car.interior = request.POST.get('interior')
        car.miles = request.POST.get('miles')
        car.door = request.POST.get('door')
        car.passengers = request.POST.get('passengers')
        car.vin_no = request.POST.get('vin_no')
        car.mileage = request.POST.get('mileage')
        car.fuel_type = request.POST.get('fuel_type')
        car.no_of_owners = request.POST.get('no_of_owners')
        car.is_featured = 'is_featured' in request.POST

        car.save()
        messages.success(request, "Car updated successfully!")
        return redirect('admin_cars')
    context = {'car':car}
    return render(request, 'update_detail.html', context)

def delete_car(request, pk):
    # Retrieve the car object or return a 404 error if not found
    car = get_object_or_404(Car, id=pk)
    
    if request.method == 'POST':
        # Delete the car object
        car.delete()
        messages.success(request, 'Car deleted successfully.')
    return redirect('admin_cars')  # Redirect to a success page or another view
    


def add_car(request):
    if request.method == 'POST':
        car_title = request.POST.get('car_title')
        state = request.POST.get('state')
        city = request.POST.get('city')
        color = request.POST.get('color')
        year = request.POST.get('year')
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        description = request.POST.get('description')
        body_style = request.POST.get('body_style')
        engine = request.POST.get('engine')
        transmission = request.POST.get('transmission')
        interior = request.POST.get('interior')
        miles = request.POST.get('miles')
        door = request.POST.get('door')
        passengers = request.POST.get('passengers')
        vin_no = request.POST.get('vin_no')
        mileage = request.POST.get('mileage')
        fuel_type = request.POST.get('fuel_type')
        no_of_owners = request.POST.get('no_of_owners')
        is_featured = 'is_featured' in request.POST

        car = Car(
            car_title=car_title,
            state=state,
            city=city,
            color=color,
            year=year,
            condition=condition,
            price=price,
            description=description,
            body_style=body_style,
            engine=engine,
            transmission=transmission,
            interior=interior,
            miles=miles,
            door=door,
            passengers=passengers,
            vin_no=vin_no,
            mileage=mileage,
            fuel_type=fuel_type,
            no_of_owners=no_of_owners,
            is_featured=is_featured,
        )

        if 'car_photo' in request.FILES:
            car.car_photo = request.FILES['car_photo']
        if 'car_photo_1' in request.FILES:
            car.car_photo_1 = request.FILES['car_photo_1']
        if 'car_photo_2' in request.FILES:
            car.car_photo_2 = request.FILES['car_photo_2']
        if 'car_photo_3' in request.FILES:
            car.car_photo_3 = request.FILES['car_photo_3']
        if 'car_photo_4' in request.FILES:
            car.car_photo_4 = request.FILES['car_photo_4']

        car.save()
        messages.success(request, "Car added successfully!")
        return redirect('admin_cars')

    return render(request, 'add_car.html')




def admin_teams(request):
    teams = Team.objects.order_by('-created_date')
    data = {
        'teams':teams,
    }
    return render(request, 'admin_teams.html',data)

def delete_team(request, pk):
    team = get_object_or_404(Team, id=pk)
    
    if request.method == 'POST':
        team.delete()
        messages.success(request, 'Team Member deleted successfully.')
    return redirect('admin_teams')  


def team_updation(request, pk):
    team = Team.objects.get(id=pk)
    if request.method == 'POST':
        team.first_name = request.POST.get('first_name')
        team.last_name = request.POST.get('last_name')
        team.designation = request.POST.get('designation')
        team.facebook_link = request.POST.get('facebook_link')
        team.twitter_link = request.POST.get('twitter_link')
        team.google_plus_link = request.POST.get('google_plus_link')
        if len(request.FILES) != 0:
            if len(team.photo) > 0:
                os.remove(team.photo.path)
            team.photo = request.FILES['photo']
        
        team.save()
        messages.success(request, "Team details updated successfully")
        return redirect('admin_teams')
    context = {'team':team}
    return render(request, 'update_team.html', context)

def add_team(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        facebook_link = request.POST.get('facebook_link')
        twitter_link = request.POST.get('twitter_link')
        google_plus_link = request.POST.get('google_plus_link')

        team = Team(first_name=first_name,
                    last_name=last_name,
                    designation=designation,
                    facebook_link=facebook_link,
                    twitter_link=twitter_link,
                    google_plus_link=google_plus_link,
                    )
        
        if 'photo' in request.FILES:
            team.photo = request.FILES['photo']

        team.save()
        messages.success(request, "Team member registered succesfully")
        return redirect('admin_teams')        

    return render(request, 'add_team.html')



def admin_contact(request):
    user_inquiry = Contact.objects.all()
    data = {
        'inquiries':user_inquiry
    }
    return render(request, 'admin_contact.html',data)

def contact_details(request, id):
    single_contact = get_object_or_404(Contact, pk=id)
    data = {
        'single_contact':single_contact,

    }
    return render(request, 'contact_details.html', data)



@csrf_exempt
def admin_refunds(request):
    user_refunds = Refunds.objects.all()
    
    if request.method == 'POST':
        car_refund_id = request.POST.get('car_refund_id')
        refunds = Refunds.objects.filter(car_refund_id=car_refund_id)
        
        if refunds.exists():
            refunds.delete()
            messages.success(request, "Refund is successful")
        else:
            messages.error(request, "No refunds found for this car ID")
    
    data = {
        'user_refunds': user_refunds
    }
    return render(request, 'admin_refunds.html', data)


def razor(request):
    if request.method == 'POST':
        amount = 200000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM")
        )
        razor = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
        return redirect('admin_refunds')



def admin_payments(request):
    user_payments = Payments.objects.all()
    data = {
        'payments':user_payments
    }
    return render(request, 'admin_payments.html',data)

def payment_details(request, id):
    single_payment = get_object_or_404(Payments, pk=id)
    data = {
        'single_payment':single_payment,

    }
    return render(request, 'payment_details.html', data)

