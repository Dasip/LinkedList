
# Класс узла связного списка
class Node:

    # ссылки по умолчанию указывают на NULL (None в случае Python)
    def __init__(self, data, link_next=None, link_prev=None):
        self.data = data    # данные
        self.link_next = link_next  # ссылка на следующий элемент
        self.link_prev = link_prev  # ссылка на предыдущий элемент

    # Установка данных в узел
    def set_data(self, d):
        self.data = d

    # Получение данных из узла
    def get_data(self):
        return self.data

    # Получение следующего узла по ссылке
    def next(self):
        return self.link_next

    # Получение предыдущего узла по ссылке
    def prev(self):
        return self.link_prev

    # Создание ссылки на следующий узел
    def set_next(self, n):
        self.link_next = n

    # Создание ссылки на предыдущий узел
    def set_prev(self, p):
        self.link_prev = p

    # Функция отображения узла при попытке его вывести
    def __repr__(self):
        # Выводим просто данные узла
        return str(self.data)


# Класс двусвязного линейного списка
class LinkedList:

    # В списке всегда храним ссылки на первый и последний узлы, а также длину списка
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    # Функция проверки списка на содержание узла с конкретными данными
    def __contains__(self, data):
        current_box = self.head
        # Цикл прохода по узлам списка
        while current_box:
            if current_box.get_data() == data:
                return True
            current_box = current_box.next()
        return False

    # Добавление элемента в начало списка
    def add_first(self, data):
        box = Node(data)
        # Если в списке нет узлов - первый узел автоматически задается как первый и последний узел
        if not self.tail:
            self.head = box
            box.set_prev(None)
            box.set_next(None)
            self.tail = box

        # Иначе - соединяем новый элемент ссылками с первым элементом, который был до этого
        else:
            self.head.set_prev(box)
            box.set_next(self.head)
            self.head = box
        # не забываем увеличить хранящуюся длину списка на 1
        self.len += 1

    # Добавление элемента на конкретную позицию в списке
    def insert_on_position(self, data, pos):
        # Если вставляем узел в пустой список или в начало списка
        if pos == 0 or self.count() == 0:
            self.add_first(data)
        # Если вставляем узел в конец списка
        elif pos == self.count():
            self.add_last(data)
        # Если вставляем узел в середину списка
        elif pos < self.count():
            current_box = self.head
            current_pos = 0
            # Ищем узел, лежащий сейчас на заданной позиции
            while current_pos != pos:
                current_box = current_box.next()
                current_pos += 1
            new_box = Node(data)
            # Соединяем новый узел ссылками с узлами на позициях pos-1 и pos
            new_box.set_next(current_box)
            new_box.set_prev(current_box.prev())
            # Соединяем узел на pos-1 с новым узлом
            current_box.prev().set_next(new_box)
            # Передвигаем узел, который был на pos, на pos+1
            current_box.set_prev(new_box)
            # не забываем увеличить хранящуюся длину списка на 1
            self.len += 1
        else:        # Если позиция находится вне списка
            print("Position out of range")

    # Добавление узла в конец списка
    def add_last(self, data):
        box = Node(data)
        # Если добавляем в пустой список, узел автоматически становится и первым и последним
        if not self.head:
            self.head = box
            box.set_prev(None)
            box.set_next(None)
            self.tail = box
        # иначе просто добавляем в конец
        else:
            self.tail.set_next(box)
            box.set_prev(self.tail)
            self.tail = box
        # не забываем увеличить хранящуюся длину списка на 1
        self.len += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

    # Удаляем узел с начала списка
    def remove_first(self):
        # Удаление из списка с одним узлом
        if self.len > 1:
            self.head = self.head.next()
            self.head.set_prev(None)
        # Удаление из списка с более чем 1 узлом
        else:
            self.head = None
            self.tail = None
        # не забываем уменьшить хранящуюся длину списка на 1
        self.len -= 1

    # Удаляем узел с конца списка
    def remove_last(self):
        # Удаление из списка с одним узлом
        if self.len > 1:
            self.tail = self.tail.prev()
            self.tail.set_next(None)
        # Удаление из списка с более чем 1 узлом
        else:
            self.head = None
            self.tail = None
        # не забываем уменьшить хранящуюся длину списка на 1
        self.len -= 1

    # Удаление узла с определенными данными
    def remove(self, data):
        current_box = self.head
        # поиск нужного узла
        while current_box:
            # Узел найден
            if current_box.get_data() == data:
                # Если узел - единственный в списке - очистить список
                if self.len == 1:
                    self.head = None
                    self.tail = None
                # Если узел - первый в списке - заменяем первый узел вторым
                elif current_box == self.head:
                    self.head = current_box.next()
                    self.head.set_prev(None)
                # Если узел - последний - заменяем его предпоследним
                elif current_box == self.tail:
                    self.tail = current_box.prev()
                    self.tail.set_next(None)
                # Узел в середине списка
                else:
                    current_box.prev().set_next(current_box.next())
                    current_box.next().set_prev(current_box.prev())
                # Не забываем уменьшить хранящуюся длину списка
                self.len -= 1
                return True
            current_box = current_box.next()
        # Если элемент не был найден, сказать об этом
        print("Element not found")
        return False

    # Функция для отображения списка при принте
    def __repr__(self):
        line = "[\t"
        current_box = self.head
        while current_box:
            line += f"Node({current_box.get_data()})\t"
            current_box = current_box.next()
        line += "]"
        return line

    # Получение длины списка
    def count(self):
        return self.len

    # Получение итерируемого массива из узлов списка
    def get_iterable(self):
        arr = []
        current_box = self.head
        while current_box:
            arr.append(current_box)
            current_box = current_box.next()
            print(current_box)
        return arr[:]

    def invert(self):
        if self.len > 1:
            movable = self.head
            current_box = movable.next()

            while current_box:
                movable.set_next(current_box.next())
                current_box.set_next(self.head)
                self.head = current_box
                current_box = movable.next()


a = LinkedList()
a.add_last(111)
a.add_last(123)
a.add_last(333)
a.insert_on_position(999, 2)
print(a)
a.invert()
print(a)
a.invert()
print(a)