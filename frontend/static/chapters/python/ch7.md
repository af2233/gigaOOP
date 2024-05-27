
Композиция и агрегация – это два важных концепта в объектно-ориентированном программировании (ООП), которые используются для моделирования отношений между объектами. Они оба относятся к концепции ассоциации, но имеют свои особенности и различия.

### **Основные различия между композицией и агрегацией**

1. **Жизненный цикл объектов**:
    - **Композиция**: Жизненный цикл составного объекта (части) полностью управляется агрегирующим объектом (целым). Когда уничтожается агрегирующий объект, уничтожаются и все составные объекты. Например, если дом уничтожается, то комнаты тоже уничтожаются.
    - **Агрегация**: Составной объект (часть) может существовать независимо от агрегирующего объекта (целого). Например, студенты могут существовать независимо от университета, в котором они учатся.
2. **Тип связи**:
    - **Композиция**: Представляет сильную связь "часть-целое" (содержит). Агрегирующий объект содержит составные объекты и отвечает за их создание и удаление.
    - **Агрегация**: Представляет слабую связь "имеет" (владеет). Агрегирующий объект просто ссылается на составные объекты, но не отвечает за их создание или удаление.
3. **Управление памятью**:
    - **Композиция**: Агрегирующий объект управляет памятью составных объектов. Это означает, что составные объекты создаются и уничтожаются вместе с агрегирующим объектом.
    - **Агрегация**: Составные объекты могут существовать независимо от агрегирующего объекта и управляются отдельно. Один составной объект может быть частью нескольких агрегирующих объектов.
4. **Примеры использования**:
    - **Композиция**: Используется для моделирования отношений, где составной объект является неотъемлемой частью агрегирующего объекта. Например, двигатель является неотъемлемой частью автомобиля.
    - **Агрегация**: Используется для моделирования отношений, где составной объект может существовать независимо от агрегирующего объекта. Например, компьютер и периферийные устройства (мышь, клавиатура) могут существовать независимо друг от друга.

### **Примеры**

### **Композиция**

```python

class Engine:
    def __init__(self, power):
        self.power = power

    def __str__(self):
        return f"Engine power: {self.power} HP"

class Car:
    def __init__(self, model, engine_power):
        self.model = model
        self.engine = Engine(engine_power)

    def __str__(self):
        return f"Car model: {self.model}, {self.engine}"

# Создание автомобиля с двигателем
car = Car("Tesla Model S", 670)
print(car)

```

### **Выходные данные**

```yaml

Car model: Tesla Model S, Engine power: 670 HP
```

### **Агрегация**

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"

class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        university_str = f"University: {self.name}\n"
        for student in self.students:
            university_str += f" - {student}\n"
        return university_str

# Создание студентов
student1 = Student("Vasya Pupkin", "S12345")
student2 = Student("Fedya Mokin", "S67890")

# Создание университета
university = University("MAI University")

# Добавление студентов в университет
university.add_student(student1)
university.add_student(student2)

# Вывод информации об университете
print(university)

```

### **Выходные данные**

```yaml
University: MAI University
 - Vasya Pupkin (ID: S12345)
 - Fedya Mokin (ID: S67890)
```

### **Заключение**

Композиция и агрегация – это важные инструменты моделирования в ООП, которые позволяют создавать сложные системы из простых компонентов. Понимание различий между ними помогает выбирать правильный подход для моделирования реальных отношений между объектами.
# **Декораторы классов**

Декораторы классов в Python позволяют изменять или расширять поведение классов и их методов без изменения их исходного кода. Они могут быть использованы для различных задач, таких как регистрация классов, добавление методов, контроль доступа и логирование.

### **Примеры декораторов классов**

1. **`@classmethod` и `@staticmethod`**:
    - **`@classmethod`** используется для определения метода, который получает сам класс в качестве первого аргумента.
    - **`@staticmethod`** используется для определения метода, который не получает ни экземпляр, ни класс в качестве первого аргумента.
    
    ```python
    class MyClass:
        class_variable = 0
    
        def __init__(self, instance_variable):
            self.instance_variable = instance_variable
    
        @classmethod
        def class_method(cls):
            return cls.class_variable
    
        @staticmethod
        def static_method(x, y):
            return x + y
    
    obj = MyClass(10)
    print(MyClass.class_method())  # 0
    print(MyClass.static_method(5, 3))  # 8
    ```
    
2. **`@property`**:
    - **`@property`** позволяет определять методы, которые можно использовать как атрибуты.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        from math import pi
        return pi * (self._radius ** 2)

circle = Circle(5)
print(circle.radius)  # 5
print(circle.area)  # 78.53981633974483
circle.radius = 3
print(circle.area)  # 28.27433388230813
```