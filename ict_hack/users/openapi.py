from drf_spectacular.utils import extend_schema

profile_get_schema = extend_schema(summary='Получить информацию о текущем пользователе')
profile_delete_schema = extend_schema(summary='Деактивировать аккаунт')
users_search_get_schema = extend_schema(summary='Поиск пользователей (мин. 3 символа, макс. 10 результатов)')
