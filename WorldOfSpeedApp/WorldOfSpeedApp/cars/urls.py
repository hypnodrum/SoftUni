from django.urls import path

from WorldOfSpeedApp.cars.views import catalogue, create_car, DetailCarView, EditCarView, DeleteCarView

urlpatterns =(
    path("catalogue/", catalogue, name="catalogue"),
    path("create/", create_car, name="create_car"),
    path("<int:pk>/details/", DetailCarView.as_view(), name="details_car"),
    path("<int:pk>/edit/", EditCarView.as_view(), name="edit_car"),
    path("<int:pk>/delete/", DeleteCarView.as_view(), name="delete_car"),

)