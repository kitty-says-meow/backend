from django.db import models


class EventCategory(models.IntegerChoices):
    EDUCATION = 1, 'Учебная деятельность'
    SCIENCE = 2, 'Научно-исследовательская деятельность'
    SOCIAL = 3, 'Общественная деятельность'
    CULTURE = 4, 'Культурно-творческая деятельность'
    SPORT = 5, 'Спортивная деятельность'


class EventStatus(models.IntegerChoices):
    pass
