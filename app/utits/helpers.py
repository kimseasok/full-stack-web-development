def sanitize_key(key):
    import re
    return re.sub(r"\W", "_", key).lower()