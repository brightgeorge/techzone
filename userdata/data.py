import os

from io import BytesIO
import base64
from PIL import Image
import qrcode
from django.http import HttpResponse

from django.shortcuts import render
from django.contrib import messages


from userdata.models import *



def view_all_profiles(request):
    if 'username' in request.session:
        #vu=profile.objects.filter(user_flage=1)
        context={
            'users':profile.objects.all()
        }
        return render(request,'admindashboard/control_panel/view_all_profiles.html',context)
    return render(request,'index.html')

def add_new_user_details(request):
    return render(request,'admindashboard/control_panel/add_new_user_details.html')

def add_new_user_details_regi(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        location = request.POST.get('location')

        udes = request.POST.get('description')
        profile_details = request.POST.get('profiledetails')

        facebook = request.POST.get('facebook')
        faceendis = request.POST.get('fbendis')

        instagram = request.POST.get('instagram')
        instaendis = request.POST.get('insta_endis')

        linkedin = request.POST.get('linkedin')
        linkendis = request.POST.get('linkedin_endis')

        twitter = request.POST.get('twitter')
        twittendis = request.POST.get('twitter_endis')

        img = request.FILES['image']
        imgback = request.FILES['imagebackground']

        uc = profile()
        uc.name = name

        uc.mob = mob
        uc.email = email
        uc.location = location
        uc.prof = udes
        uc.prof_details = profile_details

        uc.facebook = facebook
        uc.facebook_endis = faceendis

        uc.instagram = instagram
        uc.instagram_endis = instaendis

        uc.linkedin = linkedin
        uc.linkedin_endis = linkendis

        uc.twitter = twitter
        uc.twitter_endis = twittendis

        uc.profile_image = img
        uc.profile_image_back = imgback

        #uc.user_flage = chk
        uc.save()
        return view_all_profiles(request)

    return render(request, 'admindashboard/control_panel/add_new_user_details.html')



def update_profile(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        mob = request.POST.get('mob')
        email = request.POST.get('email')
        location = request.POST.get('location')
        udes = request.POST.get('description')

        profile_details = request.POST.get('profiledetails')

        facebook = request.POST.get('facebook')
        faceendis = request.POST.get('fbendis')

        instagram = request.POST.get('instagram')
        instaendis = request.POST.get('insta_endis')

        linkedin = request.POST.get('linkedin')
        linkendis = request.POST.get('linkedin_endis')

        twitter = request.POST.get('twitter')
        twittendis = request.POST.get('twitter_endis')

        #img = request.FILES['image']





        uc = profile.objects.get(id=id)

        #prod = profile.objects.get(id=id)
        #if len(prod.profile_image)>0:
            #os.remove(prod.profile_image.path)

        uc.name = name

        uc.mob = mob
        uc.email = email
        uc.location = location
        uc.prof = udes
        uc.prof_details = profile_details

        uc.facebook = facebook
        uc.facebook_endis = faceendis

        # uc.emp_branch=empbranch


        uc.instagram = instagram
        uc.instagram_endis = instaendis

        uc.linkedin = linkedin
        uc.linkedin_endis = linkendis

        uc.twitter = twitter
        uc.twitter_endis = twittendis

        #print('this is my image',img)

        #if img != '':
            #uc.profile_image = img


        #uc.user_flage = chk
        uc.save()
        messages.info(request, 'Profile updated sucessfully')
        return view_all_profiles(request)

    context = {
        'sd' : profile.objects.all().get(id=id),
    }

    return render(request, 'admindashboard/control_panel/update_profile.html',context)









def update_profile_image(request,id):
    if request.method == 'POST':
        img = request.FILES['image']

        uc = profile.objects.get(id=id)

        prod = profile.objects.get(id=id)
        if len(prod.profile_image)>0:
            os.remove(prod.profile_image.path)
            uc.profile_image = img
        uc.save()

        messages.info(request, 'Profile updated sucessfully')
        return view_all_profiles(request)

    context = {
        'sd' : profile.objects.all().get(id=id),
    }

    return render(request, 'admindashboard/control_panel/update_profile_image.html',context)







def update_profile_image_background(request,id):
    if request.method == 'POST':
        img = request.FILES['image']

        uc = profile.objects.get(id=id)

        prod = profile.objects.get(id=id)
        if len(prod.profile_image_back)>0:
            os.remove(prod.profile_image_back.path)
            uc.profile_image_back = img
        uc.save()

        messages.info(request, 'Profile updated sucessfully')
        return view_all_profiles(request)

    context = {
        'sd' : profile.objects.all().get(id=id),
    }

    return render(request, 'admindashboard/control_panel/update_profile_image_background.html',context)





#############OUR SERVICES START HERE #################


def view_all_services(request):
    if 'username' in request.session:
        #vu=profile.objects.filter(user_flage=1)
        vu = profile.objects.all()
        context={
            'users':vu
        }
        return render(request,'admindashboard/control_panel/view_all_services.html',context)
    return render(request,'index.html')

def add_new_services(request):
    return render(request,'admindashboard/control_panel/add_new_services.html')



#############OUR SERVICES END HERE #################

#############OUR IMAGES START HERE #################

def upload_image(request):
    return render(request,'admindashboard/control_panel/images/background/upload_image.html')

def profile_image_regi(request):
    if request.method == 'POST':
        img = request.FILES['image']
        print('my image',img)

        ic = images_profile()
        ic.profile_image = img
        ic.save()

    return render(request,'admindashboard/control_panel/images/background/upload_image.html')




#############OUR IMAGES END HERE #################


def qrcode(request,id):
    context = {}
    if request.method == "POST":
        import qrcode
        qr_text = request.POST.get("qr_text", "")
        #qr_image = qrcode.make(qr_text,box_size=15)
        data = 'QR Code using make() function'
        m='http://54.252.251.143:8000/user_dashboard_old/'
        n=id
        x=m+n


        import qrcode
        qr_image = qrcode.make(x)
        qr_image_pil = qr_image.get_image()
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
        context['msg'] = x
    return render(request, 'admindashboard/control_panel/qrcode.html', context=context)



import csv
def getfile(request,id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.vcf"'
    employees = profile.objects.all().filter(id=id)
    writer = csv.writer(response)
    for employee in employees:
        writer.writerow([employee.name,employee.mob,employee.email])
    return response




##############