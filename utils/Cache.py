import time

class Cache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl=None):
        if ttl is not None:
            expiration_time = time.time() + ttl
        else:
            expiration_time = None

        self.cache[key] = {'value': value, 'expiration_time': expiration_time}

    def get(self, key):
        if key in self.cache:
            cache_item = self.cache[key]
            if cache_item['expiration_time'] is None or cache_item['expiration_time'] > time.time():
                return cache_item['value']
            else:
                del self.cache[key]  # Remove item expirado do cache
        return None

    def remove(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache = {}