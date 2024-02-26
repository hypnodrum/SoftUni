from django import forms
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from WorldOfSpeedApp.profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")

        widgets = {
            "username": forms.TextInput(attrs={"placeholder":"Username"}),
            "email": forms.EmailInput(attrs={"placeholder":"Email"}),
            "age": forms.NumberInput(attrs={"placeholder":"Age"}),
            "password": forms.PasswordInput(attrs={"placeholder":"Password"}),
        }


def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("catalogue")
    context = {'form': form,}

    return render(request,"profiles/profile-create.html", context)


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = "profiles/profile-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()

        total_car_price = profile.profile.aggregate(total_sum=Sum('price'))['total_sum']
        total_car_price = total_car_price if total_car_price is not None else 0
        context['total_car_price'] = total_car_price
        context['profiles'] = Profile.objects.all()

        return context

    def get_object(self, queryset=None):
        return get_profile()


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = "profiles/profile-edit.html"
    fields = ("username", "email", "age", "password", "first_name", "last_name", "profile_picture")
    success_url = reverse_lazy("details_profile")

    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return get_profile()
