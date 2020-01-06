from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .forms import LinkForm
# Create your views here.
from .models import Link

class Home(TemplateView):
    def get(self, request, *args, **kwargs):
        form = LinkForm()
        return render(request, 'cutter/home.html', {'form':form})

    def post(self, request, *args, **kwargs):
            form = LinkForm(request.POST)
            if form.is_valid():
                new_url = form.cleaned_data.get("url")
                print(new_url)
                obj, created = Link.objects.get_or_create(url=new_url)
                print(obj)
                return render(request, 'cutter/success.html' ,{'object':obj})
            else:
                return render(request, 'cutter/home.html', {'form':form})
                    
        
            
        
class SuccessDeatil(DetailView):
    def get(self, request, key=None, *args, **kwargs):
        link = Link.objects.get(key=key)
        return redirect(link.url)