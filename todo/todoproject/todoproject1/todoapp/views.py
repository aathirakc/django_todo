from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from django import forms
from .forms import task_form
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class list_view(ListView):
    model=task
    template_name = 'add.html'
    context_object_name = 'details'

class detail_view(DetailView):
    model=task
    template_name = 'detail_view.html'
    context_object_name = 'detail'

class update_view(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'detail'
    fields=('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class delete_view(DeleteView):
    model=task
    template_name = 'delete.html'
    context_object_name = 'detail'
    def get_success_url(self):
        return reverse_lazy('cbvdetail')
def home(request):
    return HttpResponse("hi")

def add(request):
    obj = task.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        p=request.POST.get('p')
        date=request.POST.get('date')
        obj=task(name=name,priority=p,date=date)

        obj.save()
        return redirect('/add')
    return render(request,"add.html",{'details':obj})
def delete(request,id):
    obj=task.objects.get(id=id)
    obj.delete()
    return redirect('/add')
def update(request,id):
    obj=task.objects.get(id=id)
    form = task_form(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/add')
    return render(request, "edit.html", {'form': form, 'task2': obj})

