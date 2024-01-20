def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.log_history = []

    def log(self, message):
        self.log_history.append(message)

    def get_log_history(self):
        return self.log_history

logger1 = Logger()
logger1.log("Request 1 handled")
logger1.log("Response 1 sent")
logger2 = Logger()
logger2.log("Request 2 handled")
logger2.log("Response 2 sent")
print(logger1.get_log_history())
print(logger2.get_log_history())