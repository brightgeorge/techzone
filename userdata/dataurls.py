from django.urls import path
from . import data

urlpatterns = [

    path('add_new_user_details', data.add_new_user_details, name='add_new_user_details'),
    path('add_new_user_details_regi',data.add_new_user_details_regi,name='add_new_user_details_regi'),
    path('view_all_profiles',data.view_all_profiles,name='view_all_profiles'),
    path('update_profile/<id>',data.update_profile,name='update_profile'),

    path('upload_image/',data.upload_image,name='upload_image'),
    path('profile_image_regi/',data.profile_image_regi,name='profile_image_regi'),
    path('update_profile_image/<id>',data.update_profile_image,name='update_profile_image'),
    path('update_profile_image_background/<id>',data.update_profile_image_background,name='update_profile_image_background'),

    path('qrcode/<id>',data.qrcode,name='qrcode'),
    path('getfile/<id>',data.getfile,name='getfile'),


    ]