from django.contrib import admin

from apps.models import User, VacancyModel, DistrictModel


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(VacancyModel)
class VacancyModelAdmin(admin.ModelAdmin):
    pass


@admin.register(DistrictModel)
class DistrictModelAdmin(admin.ModelAdmin):
    pass
