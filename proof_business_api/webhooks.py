from .client import Client
from .types import JsonObj
import hmac
from hashlib import sha256


class WebhooksClient(Client):
    resource = "webhooks"
    api_version = "v2"

    def all(self, **params) -> JsonObj:
        return self._get("", params=params)

    def create(self, **payload) -> JsonObj:
        return self._post("", json=payload)

    def retrieve(self, id: str, **params) -> JsonObj:
        return self._get(id, params=params)

    def update(self, id: str, **payload) -> JsonObj:
        return self._put(id, json=payload)

    def delete(self, id: str) -> JsonObj:
        return self._delete(id)

    def events_for(self, id: str, **params) -> JsonObj:
        return self._get(id, params=params)

    def subscriptions(self) -> JsonObj:
        return self._get("")

    def validate_hmac(self, body: bytes, signature: str):
        hmac_signature = hmac.new(self.api_key.encode(), body, sha256).hexdigest()
        return hmac_signature == signature