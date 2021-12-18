from drf_spectacular.openapi import AutoSchema as DefaultAutoSchema


# DRF-spectacular custom schema inspector
class AutoSchema(DefaultAutoSchema):
    def get_paginated_name(self, serializer_name):
        return f'Paginated{serializer_name}s'
