from django.urls import path

from WorldOfSpeedApp.profiles.views import create_profile, ProfileDetailsView, \
    EditProfileView, DeleteProfileView

urlpatterns =(
    path("create/", create_profile, name="create_profile"),
    path("details/", ProfileDetailsView.as_view(), name="details_profile"),
    path("edit/", EditProfileView.as_view(), name="edit_profile"),
    path("delete/", DeleteProfileView.as_view(), name="delete_profile"),

)