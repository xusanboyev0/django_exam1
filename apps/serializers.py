from rest_framework.serializers import ModelSerializer, CharField

from apps.models import VacancyModel, User


class UserModelCreateSerializer(ModelSerializer):
    password = CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'password')

    def create(self, validated_data):
        users = super(UserModelCreateSerializer, self).create(validated_data)
        users.set_password(validated_data['password'])
        users.save()
        return users


class VacancyModelSerializer(ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = 'title', 'salary', 'district', 'practice', 'company'


class VacancyModelCreateSerializers(ModelSerializer):
    class Meta:
        model = VacancyModel
        exclude = 'user',


class VacancyModelRetrieveSerializers(ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = 'title', 'salary', 'district', 'description', 'company', 'practice'
