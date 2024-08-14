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

        whatsapp = request.POST.get('what')
        whatsapp_endis = request.POST.get('what_endis')
        youtube = request.POST.get('youtube')
        youtube_endis = request.POST.get('youtube_endis')
        google = request.POST.get('google')
        google_endis = request.POST.get('google_endis')
        telegram = request.POST.get('telegram')
        telegram_endis = request.POST.get('telegram_endis')

        general_link_head_1 = request.POST.get('general_link_head_1')
        general_link = request.POST.get('general_link')
        general_link_endis = request.POST.get('general_link_endis')

        general_link_head_12 = request.POST.get('general_link_head_12')
        general_link2 = request.POST.get('general_link2')
        general_link_endis2 = request.POST.get('general_link_endis2')

        general_link_head_13 = request.POST.get('general_link_head_13')
        general_link3 = request.POST.get('general_link3')
        general_link_endis3 = request.POST.get('general_link_endis3')

        img = request.FILES['image']
        imgback = request.FILES['imagebackground']
        broch = request.FILES['broch']

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

        uc.whatsapp = whatsapp
        uc.whatsapp_endis = whatsapp_endis
        uc.youtube = youtube
        uc.youtube_endis = youtube_endis
        uc.google = google
        uc.google_endis = google_endis
        uc.telegram = telegram
        uc.telegram_endis = telegram_endis

        uc.genaral_link_name = general_link_head_1
        uc.genaral_link = general_link
        uc.genaral_link_endis = general_link_endis

        uc.genaral_link_name2 = general_link_head_12
        uc.genaral_link2 = general_link2
        uc.genaral_link_endis2 = general_link_endis2

        uc.genaral_link_name3 = general_link_head_13
        uc.genaral_link3 = general_link3
        uc.genaral_link_endis3 = general_link_endis3


        uc.profile_image = img
        uc.profile_image_back = imgback
        uc.brochure = broch

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



        whatsapp = request.POST.get('what')
        whatsapp_endis = request.POST.get('what_endis')
        youtube = request.POST.get('youtube')
        youtube_endis = request.POST.get('youtube_endis')
        google = request.POST.get('google')
        google_endis = request.POST.get('google_endis')
        telegram = request.POST.get('telegram')
        telegram_endis = request.POST.get('telegram_endis')

        general_link_head_1 = request.POST.get('general_link_head_1')
        general_link = request.POST.get('genaral_link')
        general_link_endis = request.POST.get('general_link_endis')

        general_link_head_12 = request.POST.get('general_link_head_12')
        general_link2 = request.POST.get('genaral_link2')
        general_link_endis2 = request.POST.get('general_link_endis2')

        general_link_head_13 = request.POST.get('general_link_head_13')
        general_link3 = request.POST.get('genaral_link3')
        general_link_endis3 = request.POST.get('general_link_endis3')

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



        uc.whatsapp = whatsapp
        uc.whatsapp_endis = whatsapp_endis
        uc.youtube = youtube
        uc.youtube_endis = youtube_endis
        uc.google = google
        uc.google_endis = google_endis
        uc.telegram = telegram
        uc.telegram_endis = telegram_endis

        uc.genaral_link_name = general_link_head_1
        uc.genaral_link = general_link
        uc.genaral_link_endis = general_link_endis

        uc.genaral_link_name2 = general_link_head_12
        uc.genaral_link2 = general_link2
        uc.genaral_link_endis2 = general_link_endis2

        uc.genaral_link_name3 = general_link_head_13
        uc.genaral_link3 = general_link3
        uc.genaral_link_endis3 = general_link_endis3

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


def update_pdf(request,id):
    if request.method == 'POST':
        img = request.FILES['uppdf']

        uc = profile.objects.get(id=id)

        prod = profile.objects.get(id=id)

        if len(prod.brochure) > 0:
            os.remove(prod.brochure.path)
            uc.brochure = img

        uc.save()

        messages.info(request, 'update pdf sucessfully')
        return view_all_profiles(request)

    context = {
        'sd' : profile.objects.all().get(id=id),
    }

    return render(request, 'admindashboard/control_panel/updatepdf.html',context)




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
    response['Content-Disposition'] = 'attachment; filename="ramu.vcf"'
    employees = profile.objects.all().filter(id=id)
    writer = csv.writer(response)
    a='BEGIN:VCARD\nVERSION:3.0\nN:;Adv . Latha . K;;;\nFN:Adv . Latha . K\nORG:\nTITLE:Advocate\nTEL;type=Work:+919447131783\nitem1.URL:https://nearfield.me/AdvLathak\nitem1.X-ABLabel:OTHER\nEND:VCARD'
    x=10
    for i in employees:
        writer.writerow([i.prof])
    return response




##############