import os

from django.shortcuts import render
from django.contrib import messages

from userdata.models import *



def view_all_profiles(request):
    if 'username' in request.session:
        #vu=profile.objects.filter(user_flage=1)
        vu = profile.objects.all()
        context={
            'users':vu
        }
        return render(request,'admindashboard/control_panel/view_all_profiles.html',context)
    return render(request,'index.html')

def add_new_user_details(request):
    return render(request,'admindashboard/control_panel/add_new_user_details.html')

def add_new_user_details_regi(request):
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




    #uc.user_flage = chk
    uc.save()

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

        img = request.FILES['image']





        uc = profile.objects.get(id=id)

        prod = profile.objects.get(id=id)
        if len(prod.profile_image)>0:
            os.remove(prod.profile_image.path)

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