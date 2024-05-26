# **Исключения в ООП**

Исключения в объектно-ориентированном программировании позволяют управлять ошибками и исключительными ситуациями, которые могут возникнуть во время выполнения программы. В Python можно создавать собственные классы исключений, наследуя их от встроенных классов исключений.

### **Примеры обработки и создания исключений**

1. **Обработка исключений**:
    - Используйте блоки **`try`**, **`except`**, **`else`** и **`finally`** для обработки исключений.
    
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print("No errors occurred")
    finally:
        print("This will always execute")
    ```
    
2. **Создание собственных исключений**:
    - Создавайте собственные классы исключений, наследуя их от **`Exception`** или его подклассов.
    
    ```python
    class CustomError(Exception):
        pass
    
    def risky_function(x):
        if x < 0:
            raise CustomError("Negative value not allowed")
    
    try:
        risky_function(-1)
    except CustomError as e:
        print(f"Caught an exception: {e}")
    ```
    
3. **Исключения в методах классов**:
    - Обработка и генерация исключений внутри методов классов.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(150)
except ValueError as e:
    print(f"Error: {e}")
```