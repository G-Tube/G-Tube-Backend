import os
from datetime import timedelta

SIMPLE_JWT = {
    "TOKEN_OBTAIN_SERIALIZER": "src.auth_manager.serializers.CustomObtainPairSerializer",
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "ISSUER": "gTube",
}


def get_jwk_from_env():
    config = {}
    rsa_priv_key_file = os.getenv("JWT_PRIVATE_KEY")
    algorithm = os.getenv("JWT_ALGORITHM", "RS256")
    if rsa_priv_key_file:
        with open(rsa_priv_key_file) as file:
            config["SIGNING_KEY"] = file.read().strip()

        rsa_pub_key_file = rsa_priv_key_file + ".pub"
        if algorithm == "RS256":
            with open(rsa_pub_key_file) as file:  # type: ignore
                config["VERIFYING_KEY"] = file.read().strip()

        config["VERIFYING_KEY"] = None
        config["ALGORITHM"] = algorithm
        config["JWK_URL"] = "/.well-known/jwks.json"
    return config


SIMPLE_JWT.update(get_jwk_from_env())
