from types import SimpleNamespace
from typing import Any
import json


def __json_encode(o: object) -> Any:
    return { __beautify_key(k): v for k, v in o.__dict__.items() }


def __json_decode(json: Any) -> Any:
    return SimpleNamespace(**json)


def __beautify_key(key: str) -> str:
    return key.replace(r'^[_]*', '')


def encode(o: object) -> str:
    return json.dumps(o, default=__json_encode)


def decode(raw: str) -> Any:
    return json.loads(raw, object_hook=__json_decode)