from django.urls import path
from WorldOfSpeedApp.web.views import index

urlpatterns =(
    path("", index, name="index"),
)