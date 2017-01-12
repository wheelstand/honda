import hashlib
import uuid


def random_string():
    salt = uuid.uuid4().hex
    return hashlib.md5(salt.encode()).hexdigest()