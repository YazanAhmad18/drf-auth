from django.urls import path
from .views import AirplanesList, AirplanesDetail

urlpatterns = [
    path('', AirplanesList.as_view(), name='airplane_list'),
    path('<int:pk>/', AirplanesDetail.as_view(), name='airplane_detail'),
]