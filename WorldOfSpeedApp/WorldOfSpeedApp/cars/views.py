from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from WorldOfSpeedApp.cars.models import Car
from django.views import generic as views


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("car_type", "car_model", "year", "image_url", "price", "owner")
        labels = {
            'car_type': 'Type',
            'car_model': 'Model',
            'year': 'Year',
            'image_url': 'Image URL',
            'price': 'Price',
            'owner': 'Owner',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Set choices for the car_type field
            self.fields['car_type'].widget.choices = Car.CHOICES

        widgets = {
            "image_url": forms.URLInput(attrs={"placeholder":"https://..."}),
        }


def get_car():
    return Car.objects.all()


def create_car(request):
    form = CreateCarForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {'form': form,}

    return render(request,"cars/car-create.html", context)


def catalogue(request):

    context = {
        "cars": Car.objects.all()
    }
    return render(request,"cars/catalogue.html", context)


class DetailCarView(views.DetailView):
    model = Car
    template_name = "cars/car-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        return context


class EditCarView(views.UpdateView):
    model = Car
    template_name = "cars/car-edit.html"
    fields = ("car_type", "car_model", "year", "image_url", "price", "owner")
    success_url = reverse_lazy("catalogue")


class DeleteCarView(views.DeleteView):
    model = Car
    template_name = "cars/car-delete.html"
    success_url = reverse_lazy("catalogue")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        context['car_type'] = car.car_type
        context['car_model'] = car.car_model
        context['car_year'] = car.year
        context['car_image_url'] = car.image_url
        context['car_price'] = car.price
        return context

