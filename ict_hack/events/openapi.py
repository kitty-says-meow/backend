from drf_spectacular.utils import extend_schema

from events.serializers import EventSerializer

events_create_schema = extend_schema(summary='Создать мероприятие')
events_retrieve_schema = extend_schema(summary='Получить мероприятие по ID')
events_list_schema = extend_schema(summary='Получить список мероприятий')
events_my_schema = extend_schema(summary='Получить список мероприятий моих клубов/подразделений')
events_report_schema = extend_schema(summary='Загрузить отчет по мероприятию', responses={200: EventSerializer})
events_join_schema = extend_schema(summary='Записаться на мероприятие', responses={201: ''})
