from django.conf import settings
from django.utils import timezone
from drf_spectacular.contrib.django_oauth_toolkit import DjangoOAuthToolkitScheme
from mozilla_django_oidc.auth import OIDCAuthenticationBackend


class KeycloakOIDCAuthenticationBackend(OIDCAuthenticationBackend):
    def get_username(self, claims):
        username = super().get_username(claims)
        preferred_username = claims.get('preferred_username', username)
        return preferred_username

    def get_userinfo(self, access_token, id_token, payload):
        return self.verify_token(access_token)

    def create_user(self, claims):
        user = super().create_user(claims)

        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user

    def update_user(self, user, claims):
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.last_login = timezone.now()
        user.save()

        return user


class KeycloakAuthScheme(DjangoOAuthToolkitScheme):
    target_class = 'mozilla_django_oidc.contrib.drf.OIDCAuthentication'
    name = 'keycloak'

    def get_security_requirement(self, auto_schema):
        return {self.name: ['profile']}

    def get_security_definition(self, auto_schema):
        return {
            'type':             'openIdConnect',
            'openIdConnectUrl': f'{settings.KEYCLOAK_SERVER}/auth/realms/{settings.KEYCLOAK_REALM}/.well-known/openid-configuration'
        }
