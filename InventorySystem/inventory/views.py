from django.shortcuts import render,redirect
from .forms import productdetailform
from .models import *

def myfun(request):
    prod = Product.objects.all()
    form=productdetailform()
    if request.method=='POST':
        form=productdetailform(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['Name']
            ds=form.cleaned_data['Description']
            qu=form.cleaned_data['Quantity']
            pr=form.cleaned_data['Price']
            reg=Product(Name=nm,Description=ds,Quantity=qu,Price=pr)

            form .save()
            return redirect('myfun')
        else:
            form=productdetailform()
    return render(request,'base.html',{'form':form, 'prod':prod})

# Create your views here.

def detail(request):
    det=Product.objects.all()
    print(type(det))
    return render(request,'detail.html',{'info':det})

def delete(request,id):
    if request.method=='POST':
        pi=Product.objects.get(pk=id)
        pi.delete()
        return redirect('productpage')
    
def update(request, id):
    if request.method == 'POST':
        pi = Product.objects.get(pk=id)
        fm = productdetailform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('productpage')
    else:
        pi = Product.objects.get(pk=id)
        fm = productdetailform(instance=pi)
    
    return render(request, 'update.html', {'form': fm})

