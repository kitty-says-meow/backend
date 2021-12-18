from django.db import models


class EventCategory(models.IntegerChoices):
    EDUCATION = 1, 'Учебная деятельность'
    SCIENCE = 2, 'Научно-исследовательская деятельность'
    SOCIAL = 3, 'Общественная деятельность'
    CULTURE = 4, 'Культурно-творческая деятельность'
    SPORT = 5, 'Спортивная деятельность'


class EventStatus(models.IntegerChoices):
    PENDING = 1, 'На рассмотрении'
    ACCEPTED = 2, 'Мероприятие одобрено'
    REJECTED = 3, 'Мероприятие отклонено'
    PENDING_REPORT = 4, 'Ожидается отправка отчёта'
    PENDING_REPORT_CONFIRMATION = 5, 'Ожидается утверждение отчёта'
    REPORT_ACCEPTED = 6, 'Отчёт утверждён'
    REPORT_REJECTED = 7, 'Отчёт отлконён'
