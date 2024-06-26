from django.urls import path
from . import data

urlpatterns = [

    path('add_new_user_details', data.add_new_user_details, name='add_new_user_details'),
    path('add_new_user_details_regi',data.add_new_user_details_regi,name='add_new_user_details_regi'),
    path('view_all_profiles',data.view_all_profiles,name='view_all_profiles'),
    path('update_profile/<id>',data.update_profile,name='update_profile'),

    path('upload_image/',data.upload_image,name='upload_image'),
    path('profile_image_regi/',data.profile_image_regi,name='profile_image_regi'),


    ]