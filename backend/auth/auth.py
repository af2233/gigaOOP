from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

from core.config import Settings



cookie_transport = CookieTransport(cookie_name='auth', cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=Settings.SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)