
from django.urls import path
from .views import create_generator_View, result_generator_View


urlpatterns = [
    path('add', create_generator_View, name="add_generate"),
    path("result", result_generator_View, name="result_generation"),
]
