from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login

from django.template import loader
from .models import checkboxModel
from .forms import usernameForm
from .forms import toggleForm
from .project import getToken, getWLANData, updateWLANData

from django.contrib.auth.decorators import login_required

import logging
import logging.handlers



def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'




logger = logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)
logger.propagate = False


fileHandler = logging.handlers.RotatingFileHandler('logFile.log', maxBytes=2000, backupCount=5)
fileHandler.setLevel(logging.DEBUG)
fileFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(fileFormatter)

logger.addHandler(fileHandler)

# Create your views here.
def m(request):
    logger = logging.getLogger('myLogger')
    logger.addHandler(fileHandler)

    template = loader.get_template('first.html')
    
    form =usernameForm(request.POST)
    
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('home')  # Redirect to a success page.

            logger.debug(f'User: {username} logged in')
            return HttpResponseRedirect("/subwayStation/")
        else:
            # Return an 'invalid login' error message.
            form.add_error(None, 'Invalid username or password')
    else:
        form = usernameForm()
    
    


    
    return HttpResponse(template.render(request=request))   

def index(request):
    logger = logging.getLogger('myLogger')
    logger.addHandler(fileHandler)

    logger.debug('aaaa')



    token = getToken()
    u = request.user.profile
    wlanNames = []
    if u.subwayAccount:
        wlanNames += [i.wlanName for i in checkboxModel.objects.all() if i.isSubwayWlan ]
    if u.busAccount:
        wlanNames += [i.wlanName for i in checkboxModel.objects.all() if not i.isSubwayWlan ]
    
    print(wlanNames)
    for name in wlanNames:
         checkboxModel.objects.get_or_create(wlanName=name)

    if request.method == 'POST':
        for wlanName in wlanNames:
            checkboxInstance = checkboxModel.objects.get(wlanName=wlanName)
            name = checkboxInstance.stationName
            #ensures checkbox shows correct value
            try:
                checkboxInstance.isChecked = not getWLANData(wlanName+"_Open",token).json()['data'][0]['basic']['shutdown']
            except:
                print(name)
                
            checkboxInstance.save()
            form = toggleForm(request.POST, instance=checkboxInstance)
            if form.is_valid():
                form.save()
        return redirect('index')



    #ensures checkbox shows correct value
   # checkboxInstance, created = checkboxModel.objects.get_or_create(id=1)
    #checkboxInstance.isChecked = getWLANData("Emergency_Test",token).json()['data'][0]['basic']['shutdown']
    #checkboxInstance.save()

    #form = toggleForm(instance=checkboxInstance)
    forms = []
    for wlanName in wlanNames:
        checkboxInstance = checkboxModel.objects.get(wlanName=wlanName)
        name = checkboxInstance.stationName
        try :
            checkboxInstance.isChecked = not getWLANData(wlanName+"_Open",token).json()['data'][0]['basic']['shutdown']
        except:
                print(name)
                
        
        checkboxInstance.save()
        forms.append((wlanName,name, toggleForm(instance=checkboxInstance)))
    context = {
        'forms': forms,
    }

    
    return render(request, 'subwayStation.html', context)

def updateCheckbox(request):
    logger = logging.getLogger('myLogger')
    logger.addHandler(fileHandler)
    if request.method == 'POST' and is_ajax(request=request):
        token = getToken()
        checkboxID= request.POST.get('checkboxID')
        
        isChecked = request.POST.get('isChecked') == 'true'
        
        try:
            
            checkboxInstance =checkboxModel.objects.get(wlanName=checkboxID)
            
            checkboxInstance.isChecked = isChecked
            
            
            r = updateWLANData(checkboxID+"_Open",token)
            rr = updateWLANData(checkboxID+"_OWE",token)
            checkboxInstance.save()
            if isChecked:
                logger.debug(f"Wlan {checkboxID} succesfully toggled on ")
            else:
                logger.debug(f"Wlan {checkboxID} succesfully toggled off ")
            return JsonResponse({'success': True, 'is_checked': checkboxInstance.isChecked})
        except checkboxModel.DoesNotExist:
            
            return JsonResponse({'success': False, 'error': 'Checkbox not found'})
        except:
            print("aa")
        
    return JsonResponse({'success': False, 'error': 'Invalid request'})





        


