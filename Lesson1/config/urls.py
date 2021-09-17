from django.contrib import admin
from django.urls import path

from app.views import hello_view, roll_die_view, random_between_view, age_view, good_burger


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/<name>/", hello_view),
    path("age-in/<int:end>/<int:birthyear>/", age_view),
    path("order-total/<int:burgers>/<int:fries>/<int:drinks>", good_burger),
    path("roll-die/<int:sides>/", roll_die_view),
    path("random-between/<int:lo>/<int:hi>/", random_between_view),
]
