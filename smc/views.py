from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import os
from wsgiref.util import FileWrapper

def raise_grievance(request):
    print(request.user.id)
    form = GreivanceForm()
    if request.method == 'POST':
        form = GreivanceForm(request.POST)
        letter = request.POST.get('grievance_letter')
        name = Letter.objects.get(email_smc = request.user.email).name_smc
        grievance = Letter.objects.get(email_smc = request.user.email).grievance
        email = Letter.objects.filter(email_smc = request.user.email).first().email_smc
        school = Letter.objects.filter(email_smc = request.user.email).first().school_smc
        state = Letter.objects.filter(email_smc = request.user.email).first().state_smc
        city = Letter.objects.filter(email_smc = request.user.email).first().city_smc
        date_posted = Letter.objects.filter(email_smc = request.user.email).first().date_posted

        NewGrievance = GrievanceLetter.objects.create(grievance_letter = letter, name_smc = name, grievance = grievance, email_smc = email, school_smc = school, state_smc = state, city_smc = city, date_posted = date_posted)
        NewGrievance.save()
        messages.success(request, 'Grievance posted!')
        return redirect('project_home')
    return render(request, 'smc/raise_grievance_form.html', {'form': form})

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):
    	def get(self, request, *args, **kwargs):
            pdf = render_to_pdf('smc/new_grievance.html', {'form': Letter.objects.all().last()})
            return HttpResponse(pdf, content_type='application/pdf')

def grievance_form(request):
    form = LetterFieldsForm()
    context = {'form': form}  
    if request.method == 'POST':
        form = LetterFieldsForm(request.POST)
        if form.is_valid():
            user = form.save()  
            name_smc = form.cleaned_data.get('name_smc')
            let = Letter.objects.all().last()
            context = {'form': form, 'name_smc': name_smc}
        else:
            messages.success(request, 'Invalid Credentials') 
        return render(request, 'smc/view_letter.html')
    return render(request, 'smc/grievance_form.html', {'form': form})


def new_grievance(request):
    return render(request, 'smc/new_grievance.html')

def project_home(request):
    context = {
        'letters': GrievanceLetter.objects.all()
    }
    return render(request, "smc/project_home.html", context)

def project_about(request):
    return render(request, "smc/project_about.html")

def register_smc(request):
    form = SmcRegisterForm()
    context = {'form':form}
    if request.method == 'POST':
        form = SmcRegisterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Account has been created!')
            return redirect('smc_login')
        else:
            messages.success(request, 'Invalid Credentials')  
            
    return render(request, 'smc/smc_register.html', context)
