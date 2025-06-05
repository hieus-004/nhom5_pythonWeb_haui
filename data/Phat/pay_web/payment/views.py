from django.shortcuts import render

# Create your views here.
def get_pay(request):
    return render(request,'payment.html')