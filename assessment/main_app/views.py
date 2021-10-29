# from django.forms import fields
from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm


# Create your views here.
def home(request):
    widget = Widget.objects.all()
    print(widget, '<--- Widget')
    forms = WidgetForm()
    return render(request, 'home.html', {'widget': widget, 'forms': forms})

def add_widget(request):
    form = WidgetForm(request.POST)
    print(form, '<--------- This is a form')
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home.html')

def delete_widget(request, id):
    Widget.object.get(id=id).delete()
    return redirect('/')