from django.contrib import admin
from django.urls import path

from trackingAPI.views import ListCryptocurrencyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListCryptocurrencyView.as_view()),
]
