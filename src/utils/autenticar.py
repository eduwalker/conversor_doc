from flask import Request
from src.config import API_TOKEN


def autenticar(req: Request) -> bool:
    auth = req.headers.get("Authorization", "")
    return auth == f"Bearer {API_TOKEN}"
