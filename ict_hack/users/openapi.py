from drf_spectacular.utils import extend_schema

users_retrieve_schema = extend_schema(summary='Получить информацию о пользователе по ISU ID')
users_search_schema = extend_schema(summary='Поиск пользователей (мин. 3 символа, макс. 10 результатов)')
users_profile_schema = extend_schema(summary='Получить информацию о текущем пользователе')
users_rating_schema = extend_schema(summary='Получить рейтинг ПГАС')
users_score_convert_schema = extend_schema(summary='Конвертировать ПГАС баллы в личные баллы', responses={200: ''})
users_score_send_schema = extend_schema(summary='Отправить личные баллы пользователю по ISU ID')
