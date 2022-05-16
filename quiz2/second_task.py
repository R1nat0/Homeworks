"""
create_topic(topic_name: str):  создание топика
subscribe(user_id: int, topic: str): подписка пользователя на топик
post_feed(topic: str, feed_id: int): публикация новости в топик
"""
class NewsObserver:
    """
    Система наблюдения за новостями
    """
    def __init__(self):
        self.__observers = set()
    def attach(self, observer):
        """
        Подключение
        """
        self.__observers.add(observer)
    def detach(self, observer):
        """
        Отключение
        """
        self.__observers.remove(observer)
    def notify_subscribe(self):
        """
        Уведомление о подписке
        """
        for observer in self.__observers:
            observer.subscribe()
    def notify_post_feed(self):
        """
        Уведомление о публикации
        """
        for observer in self.__observers:
            observer.post_feed()

class News:
    """Наблюдение за новостями."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.topic = None
        self.feed_id = None
    def create_topic(self, topic: str, feed_id: int):
        """
        Создание топика
        """
        self.topic = topic
        self.feed_id = feed_id
    def subscribe(self):
        """
        Подписка пользователя на топик
        """
        if self.verification():
            print(f'Пользователь {self.user_id} подписался на новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не подписался ни на одну новость')
    def post_feed(self):
        """
        Публикация новости в топик
        """
        if self.verification():
            print(f'Пользователь {self.user_id} получил новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не получил ни одну новость')
    def verification(self):
        """
        Верификация
        """
        if self.topic == self.feed_id is None:
            return False
        else:
            return True
