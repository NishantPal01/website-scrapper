from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.


def scrap(request):
    if request.method == 'POST':
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
   
        for link in soup.find_all('a'):
            link_content = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_content, name=link_text)

        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all() 
    
    return render(request,'myapp/result.html',{'data':data}) 


def clear(request):
    Link.objects.all().delete()
    return render(request,'myapp/result.html')