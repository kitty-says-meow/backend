from drf_spectacular.utils import extend_schema

images_create_schema = extend_schema(
    summary='Загрузить изображение',
    description='При загрузке осуществляется проверка на валидность изображения.'
)
