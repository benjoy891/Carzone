from django.shortcuts import render, redirect, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.decorators.csrf import csrf_exempt
import razorpay
from contacts.models import Payments


# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_at')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    title_search = Car.objects.values_list('car_title',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'cars':paged_cars,
        'title_search':title_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request, 'cars/cars.html', data)



def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    user_id = request.user.id
    already_done = Payments.objects.filter(user_id=user_id, car_id=id).exists()

    data = {
        'single_car': single_car,
        'already_done': already_done,
    }
    return render(request, 'cars/car_detail.html', data)


def razor(request):
        if request.method == 'POST':
            amount = 200000
            order_currency = 'INR'
            client = razorpay.Client(
                auth=("rzp_test_SROSnyInFv81S4","WIWYANkTTLg7iGbFgEbwj4BM")
            )
            razor = client.order.create({'amount':amount, 'currency':order_currency, 'payment_capture':'1'})
        return redirect('cars')



@csrf_exempt
def payment_success(request):
    return render(request, "cars/payment_success.html")


def search(request):
    cars = Car.objects.order_by('-created_at')
    title_search = Car.objects.values_list('car_title',flat=True).distinct()
    city_search = Car.objects.values_list('city',flat=True).distinct()
    year_search = Car.objects.values_list('year',flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat=True).distinct()


    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'car_title' in request.GET:
        car_title = request.GET['car_title']
        if car_title:
            cars = cars.filter(car_title__iexact=car_title)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)
    

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)   



    data = {
        'cars':cars,
        'title_search':title_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search,
    }
    return render(request, 'cars/search.html', data)

