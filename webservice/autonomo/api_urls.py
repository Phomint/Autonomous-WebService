from django.urls import path, include

from autonomo.views import AutonomoList, AutonomoView

urlpatterns = [
    path('autonomos/', AutonomoList.as_view()),
    path('autonomos/<int:pk>/', AutonomoView.as_view()),
]

