from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
import os

#import test
# Create your views here.
 
 
def image_view(request):
    
    
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            #os.system('cmd/c "python conda.py"')
            import test
            return render(request, 'result.html',{'output': test.result})
          #  return HttpResponse('successfully uploaded')
            # return redirect('success')
    else:
        form = Form()
    return render(request, 'index.html', {'form': form})


def delete_image(request):
    # Delete the image here
    return HttpResponseRedirect('/')
 
def success(request):
    return HttpResponse('successfully uploaded')


# Create your views here.