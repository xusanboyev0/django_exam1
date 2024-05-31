from django.urls import path, include

from apps.views import VacancyModelCreateAPIView, VacancyRetrieveUpdateDestroyAPIView, LogInAPIView

urlpatterns = [
    path('vacancy/', VacancyModelCreateAPIView.as_view()),
    path('vacancy/<int:pk>', VacancyRetrieveUpdateDestroyAPIView.as_view()),
    path('login/', LogInAPIView.as_view())
]
