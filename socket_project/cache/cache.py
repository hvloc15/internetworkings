import settings
import threading


def get(key):
    obj = settings.cache.get(key)
    return obj


def set(key, object):
    lock = threading.Lock()
    lock.acquire()
    settings.cache[key] = object
    lock.release()


def delete(key):
    lock = threading.Lock()
    lock.acquire()
    try:
        del settings.cache[key]
    except:
        pass
    lock.release()
