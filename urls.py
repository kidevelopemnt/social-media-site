from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
  path('myprofile/', views.my_profile_view, name='my-profile-view'),
  path('my-invites/', views.invites_received_view, name='my-invites-view'),
  path('all-profiles/', views.ProfileListView.as_view(), name='all-profiles-view'),
  path('to-invite/', views.invite_profile_list_view, name='invite-profiles-view'),
  path('send-invite/', views.send_invitation, name='send-invite-view'),
  path('remove-friend/', views.remove_from_friends, name='remove-friend-view'),
  path('my-invites/accept/', views.accept_invitation, name='accept-invite-view'),
  path('my-invites/decline/', views.decline_invitation, name='decline-invite-view'),

]