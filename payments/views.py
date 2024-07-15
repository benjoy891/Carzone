from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
from django.contrib.auth.decorators import login_required



# Create your views here.


    

def index(request):
    if request.method == 'POST':
        amount = 200000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4","WIWYANkTTLg7iGbFgEbwj4BM")
        )
        payment = client.order.create({'amount':amount, 'currency':order_currency, 'payment_capture':'1'})

    return render(request, 'payments/index.html')


@csrf_exempt
def success(request):
    return render(request, "payments/success.html")