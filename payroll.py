from django.db import models

class Payroll(models.Model):
    name = models.CharField(max_length=100)
    rate_of_pay = models.DecimalField(max_digits=6, decimal_places=2)
    hours_worked = models.DecimalField(max_digits=6, decimal_places=2)

    def calculate_pay(self):
        return self.rate_of_pay * self.hours_worked

    def __str__(self):
        return self.name

#Create a form:
from django import forms
from .models import Payroll

class PayrollForm(forms.ModelForm):
    class Meta:
        model = Payroll
        fields = ['name', 'rate_of_pay', 'hours_worked']

    #Create views:
    from django.shortcuts import render
from .forms import PayrollForm

def payroll_calculator(request):
    if request.method == 'POST':
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll = form.save(commit=False)
            payroll.save()
            context = {
                'payroll': payroll,
                'total_pay': payroll.calculate_pay()
            }
            return render(request, 'payroll/result.html', context)
    else:
        form = PayrollForm()
    return render(request, 'payroll/form.html', {'form': form})

    #Create templates:
    <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Calculate Pay</button>
</form>

#result.html
<h1>Payroll Calculation Result</h1>
<p>Name: {{ payroll.name }}</p>
<p>Total Pay: {{ total_pay }}</p>

#Update URLs:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_calculator, name='payroll_calculator'),
]
#Include app URLs in the project:
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payroll/', include('payroll.urls')),
]

