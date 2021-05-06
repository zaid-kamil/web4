from django.shortcuts import render,redirect
from .forms import ContactForm, PublisherForm
from .models import Publisher

# Create your views here.

def homeview(request):
    return render(request,'index.html')


def contactview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)       
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm() # khali form
    context = {'c_form':form}
    return render(request,'contact.html',context)

def add_publisher_view(request):
    if request.method =='POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewpub')
    else:
        form = PublisherForm()
    context = {'pub_form':form}
    return render(request, 'add_publisher.html',context)

def show_publishers(request):
    pubs = Publisher.objects.all() # all the records
    context= {'publishers':pubs}
    return render(request, 'show_publishers.html',context)

def search_publishers(request):
    query = request.GET.get('q','')
    if len(query) >0:
        data = Publisher.objects.filter(name__contains=query)
        context = {'query':query,'results':data}
    else:
        context = {'message':"no query given"}
    return render(request,'search_publishers.html',context)