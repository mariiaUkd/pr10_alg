class Node:
    """Вузол двобічно зв'язного списку."""

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Двобічно зв'язний список."""

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # ---------- службові методи ----------
    def _check_index(self, index, allow_end=False):
        limit = self._size if allow_end else self._size - 1
        if not isinstance(index, int) or index < 0 or index > limit:
            raise IndexError(f"Індекс {index} поза межами списку (розмір {self._size})")

    def _node_at(self, index):
        """Повертає вузол за індексом, рухаючись з найближчого краю."""
        if index < self._size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev
        return current

    # ---------- додавання ----------
    def add_first(self, value):
        """Додати елемент на початок списку."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._size += 1

    def add_last(self, value):
        """Додати елемент у кінець списку."""
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._size += 1

    def insert(self, index, value):
        """Вставити елемент за індексом (0..size)."""
        self._check_index(index, allow_end=True)
        if index == 0:
            self.add_first(value)
        elif index == self._size:
            self.add_last(value)
        else:
            right = self._node_at(index)
            left = right.prev
            node = Node(value)
            node.prev, node.next = left, right
            left.next = node
            right.prev = node
            self._size += 1

    def add_all(self, index, values):
        """Додати масив елементів, починаючи з вказаного індексу."""
        self._check_index(index, allow_end=True)
        for offset, value in enumerate(values):
            self.insert(index + offset, value)

    # ---------- видалення ----------
    def remove_first(self):
        """Видалити перший елемент списку (повертає його значення)."""
        if self.head is None:
            raise IndexError("Список порожній")
        value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._size -= 1
        return value

    def remove_last(self):
        """Видалити останній елемент списку (повертає його значення)."""
        if self.tail is None:
            raise IndexError("Список порожній")
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._size -= 1
        return value

    def remove_at(self, index):
        """Видалити елемент за індексом (повертає його значення)."""
        self._check_index(index)
        if index == 0:
            return self.remove_first()
        if index == self._size - 1:
            return self.remove_last()
        node = self._node_at(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        return node.data

    # ---------- доступ і пошук ----------
    def contains(self, value):
        """Перевірити, чи існує елемент у списку."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def get(self, index):
        """Отримати елемент за індексом."""
        self._check_index(index)
        return self._node_at(index).data

    def max(self):
        """Повернути найбільший елемент."""
        if self.head is None:
            raise ValueError("Список порожній")
        result = self.head.data
        current = self.head.next
        while current:
            if current.data > result:
                result = current.data
            current = current.next
        return result

    def min(self):
        """Повернути найменший елемент."""
        if self.head is None:
            raise ValueError("Список порожній")
        result = self.head.data
        current = self.head.next
        while current:
            if current.data < result:
                result = current.data
            current = current.next
        return result

    def size(self):
        """Отримати розмір списку."""
        return self._size

    # ---------- виведення ----------
    def __str__(self):
        """Формат: {[index:0; value:10] [index:1; value:45] ...}"""
        parts = []
        current = self.head
        i = 0
        while current:
            parts.append(f"[index:{i}; value:{current.data}]")
            current = current.next
            i += 1
        return "{" + " ".join(parts) + "}"

    def print_list(self):
        print(self)

    def __len__(self):
        return self._size


if __name__ == "__main__":
    lst = DoublyLinkedList()

    print("1. add_last(10, 45, 57):")
    for v in (10, 45, 57):
        lst.add_last(v)
    lst.print_list()

    print("2. add_first(5):")
    lst.add_first(5)
    lst.print_list()

    print("3. remove_first():", lst.remove_first())
    lst.print_list()

    print("4. remove_last():", lst.remove_last())
    lst.print_list()

    print("5. contains(45):", lst.contains(45), "| contains(99):", lst.contains(99))

    print("6. get(1):", lst.get(1))

    print("7. insert(1, 30):")
    lst.insert(1, 30)
    lst.print_list()

    print("8. remove_at(2):", lst.remove_at(2))
    lst.print_list()

    print("9. add_all(1, [100, 200, 300]):")
    lst.add_all(1, [100, 200, 300])
    lst.print_list()

    print("10. max():", lst.max())
    print("11. min():", lst.min())
    print("12. size():", lst.size())

    print("13. Обробка помилок:")
    try:
        lst.get(100)
    except IndexError as e:
        print("   IndexError:", e)