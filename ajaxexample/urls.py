
from django.contrib import admin
from django.urls import path
import chart.views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cv.Viewer.as_view(),name="index"),
]
