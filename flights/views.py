import datetime

from rest_framework import generics

from flights import serializers
from flights.models import Booking, Flight
from django.shortcuts import render, redirect
from .forms import UserRegister,UserLogin
from django.contrib.auth import login, authenticate,logout


class FlightsList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer


class BookingsList(generics.ListAPIView):
    serializer_class = serializers.BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(date__gte=datetime.date.today())


class BookingDetails(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingDetailsSerializer
    lookup_url_kwarg = "booking_id"


class UpdateBooking(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.UpdateBookingSerializer
    lookup_url_kwarg = "booking_id"


class CancelBooking(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_url_kwarg = "booking_id"

    
def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("successful-signup")
    context = {
        "form" : form,
    }

    return render(request, "register.html", context)


def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("successful-login")
    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("success-page")


