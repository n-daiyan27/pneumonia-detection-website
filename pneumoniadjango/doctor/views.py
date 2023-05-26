from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import os 
def docHome(request): 
    return render(request, 'doctorPage.html')