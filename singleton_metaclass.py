from threading import Lock

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kargs)
                cls._instances[cls] = instance
        return cls._instances[cls]