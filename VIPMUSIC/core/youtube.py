import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZASLTIVeVu6ryqIdGvbIa8ciJYsuIbEAaB1fqPgclhFWOkv1uxhFTR5Pk5BguwVECpOjdOEkrT8ctvmefHzSIPEUoAMZqgLOPc9OdEy1xVkXQM3tnwJga6eRjqAQ2eptKfd3_kxIZHh-NZF7LAhfbLAY_V9P-KsEWxTQ4CIPs3wjEztaCgYKAcUSARESFQHGX2MiLyobH0DGn18u18q2yaHZpg0187",
    "expires": 1729976018.907575,
    "refresh_token": "1//05AEnUA8gnn6nCgYIARAAGAUSNwF-L9Ir3759d17CZH48CJpeAd7Aw-BSYUz6LcbKvKXZJ3F8cmgTX3QvkZ3Uf4pR7-nCDeRNWPg",
    "token_type": "Bearer",
}


def vipboy():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
