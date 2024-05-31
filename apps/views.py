from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.filters import VacancyModelFilterSet
from apps.models import VacancyModel, User
from apps.permissions import Auther
from apps.serializers import VacancyModelRetrieveSerializers, VacancyModelSerializer, VacancyModelCreateSerializers, \
    UserModelCreateSerializer
from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail


class LogInAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelCreateSerializer
    permission_classes = [AllowAny]


class VacancyModelCreateAPIView(ListCreateAPIView):
    queryset = VacancyModel.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyModelFilterSet

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VacancyModelSerializer
        return VacancyModelCreateSerializers


class VacancyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = VacancyModel.objects.all()
    serializer_class = VacancyModelRetrieveSerializers
    permission_classes = [Auther]


class SendEmailAPIView(APIView):

    def get(self, request, email):
        send_mail('Example', 'message', EMAIL_HOST_USER, [email])
        return {'message': f'Email sent message {email}'}
