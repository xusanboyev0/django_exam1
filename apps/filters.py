from django_filters import FilterSet, ChoiceFilter

from apps.models import VacancyModel


class VacancyModelFilterSet(FilterSet):
    time = ChoiceFilter(choices=VacancyModel.Time.choices)

    class Meta:
        model = VacancyModel
        fields = {
            'title': ['exact'],
            'practice': ['exact']
        }
