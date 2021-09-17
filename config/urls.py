from django.contrib import admin
from django.urls import path

from app.views import near_hundred, string_splosion, cat_dog, lone_sum

urlpatterns = [
    path('admin/', admin.site.urls),
    path("lone-sum/<a>/<b>/<c>", lone_sum),
    path("cat-dog/<word>", cat_dog),
    path("string-splosion/<str>", string_splosion),
    path("near-hundred/<int:n>", near_hundred),
]
