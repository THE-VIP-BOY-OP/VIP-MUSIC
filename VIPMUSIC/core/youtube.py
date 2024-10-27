import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZCF9VQ_t37HaJoqexLY961mvpqTM1rqdvDbLvMEmOnFAUKtQ_4GModmKm4bLHL5vJj5Wuv3WfGXC1GPsrA9K-f0biQszZTy7a3JbwMgaWRF9Cepk8YcfgVB9Ase0gQHArF267CrKZwcDiXX2IInJSYMM5sNp5wUP1JI3XWcM-DZBMnRaCgYKAbYSARISFQHGX2MihJR7K7A7JLDmzn4yRmtwDQ0187",
    "expires": 1730115155.251452,
    "refresh_token": "1//056BOYS8QzxrYCgYIARAAGAUSNwF-L9Irwl_Edq4pOz6ylq9vxSqXAyaPMSc9k4IV4sKOy66xHLbuG--4Hx3rp9r29voH71M7eFk",
    "token_type": "Bearer",
}


def vipboy():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
