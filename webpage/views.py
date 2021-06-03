from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def store(request):
    return render(request,'store.html')
 
def contact(request):
    return render(request,'contact.html')
