
Пространства имен и области видимости определяют контексты, в которых имена переменных и функций могут быть использованы. Это помогает избегать конфликтов имен и обеспечивает организованную структуру кода.

### **Примеры пространств имен и областей видимости**

1. **Локальная область видимости**:
    - Переменные, объявленные внутри функции, доступны только в этой функции.
    
    ```python
    def foo():
        local_var = 10
        print(local_var)
    
    foo()  # 10
    print(local_var)  # NameError: name 'local_var' is not defined
    ```
    
2. **Глобальная область видимости**:
    - Переменные, объявленные на уровне модуля, доступны во всем модуле.
    
    ```python
    global_var = 20
    
    def bar():
        print(global_var)
    
    bar()  # 20
    ```
    
3. **Область видимости классов и объектов**:
    - Атрибуты и методы классов имеют область видимости внутри классов и могут быть доступны через экземпляры.
    
    ```python
    class MyClass:
        class_variable = 30
    
        def __init__(self, instance_variable):
            self.instance_variable = instance_variable
    
        def method(self):
            print(self.instance_variable)
            print(MyClass.class_variable)
    
    obj = MyClass(40)
    obj.method()  # 40, 30
    ```
    
4. **Пространства имен встроенных функций**:
    - Встроенные функции и константы Python доступны во всех областях видимости.
```python
print(len("Hello"))  # 5
```