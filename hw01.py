# Потрібно розробити програму, яка імітує приймання й обробку заявок: 
# програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), 
# додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.

from queue import Queue

# Заявка на обслуговування
class Request:
    _next_id = 1

    def __init__(self, description: str):
        self.id = Request._next_id
        self.description = description
        Request._next_id += 1

# Сервісний центр обробки заявок
class ServiceCenter:
    def __init__(self):
        self.queue = Queue()

    # Генерація нової заявки
    def generate_request(self, description: str):
        request = Request(description)
        self.queue.put(request)

        print(f"Створено заявку №{request.id}: {request.description}")

    # Обробка заявки
    def process_request(self):
        if self.queue.empty():
            print("Черга заявок порожня")
            return

        request = self.queue.get()
        print(f"Оброблено заявку №{request.id}: {request.description}")


def main():
    service_center = ServiceCenter()

    while True:
        description = input("Введіть опис нової заявки (Enter - вихід): ")

        if not description:
            break

        service_center.generate_request(description)
        service_center.process_request()

    print("Роботу сервісного центру завершено")


if __name__ == "__main__":
    main()
