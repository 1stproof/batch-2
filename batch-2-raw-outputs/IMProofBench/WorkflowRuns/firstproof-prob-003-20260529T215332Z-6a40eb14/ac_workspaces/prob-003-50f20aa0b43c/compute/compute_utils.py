import json
from pathlib import Path


def safe_json_default(obj):
    try:
        import numpy as np

        if isinstance(obj, np.generic):
            return obj.item()
        if isinstance(obj, np.ndarray):
            return obj.tolist()
    except Exception:
        pass
    if isinstance(obj, complex):
        return {"real": obj.real, "imag": obj.imag}
    if isinstance(obj, (set, frozenset)):
        return sorted(obj)
    if isinstance(obj, Path):
        return str(obj)
    if hasattr(obj, "tolist"):
        return obj.tolist()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def safe_json_dumps(obj, **kwargs):
    return json.dumps(obj, default=safe_json_default, **kwargs)


def safe_json_dump(obj, path, **kwargs):
    Path(path).write_text(safe_json_dumps(obj, **kwargs), encoding="utf-8")
