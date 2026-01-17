# 🏗️ Python OOP Cheat Sheet
## Classes, Objects, Methods & Inheritance

---

## 1. OOP Fundamentals

Object-Oriented Programming organizes code into **classes** (blueprints) that create **objects** (instances) with **attributes** (data) and **methods** (behavior).

| Concept | Description |
|---------|-------------|
| **Class** | A blueprint/template for creating objects. Defines attributes and methods. |
| **Object** | An instance of a class with its own unique data. |
| **Attribute** | A variable that belongs to a class or object (the data). |
| **Method** | A function that belongs to a class (the behavior). |
| **`self`** | Reference to the current instance. First parameter of instance methods. |

---

## 2. Defining Classes

### Basic Class Structure
```python
class Dog:
    """A simple Dog class."""    # Docstring
    
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a new Dog (constructor)."""
        self.name = name          # Instance attribute
        self.age = age            # Instance attribute
    
    def bark(self):
        """Make the dog bark (instance method)."""
        return f"{self.name} says Woof!"
    
    def birthday(self):
        """Celebrate birthday."""
        self.age += 1
        return f"{self.name} is now {self.age}!"
```

### Creating & Using Objects
```python
# Create objects (instances)
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

# Access instance attributes
print(buddy.name)           # "Buddy"
print(buddy.age)            # 3

# Access class attribute
print(buddy.species)        # "Canis familiaris"
print(Dog.species)          # "Canis familiaris"

# Call methods
print(buddy.bark())         # "Buddy says Woof!"
print(buddy.birthday())     # "Buddy is now 4!"

# Modify attributes
buddy.age = 5               # Direct modification
buddy.color = "brown"       # Add new attribute dynamically

# Check type
isinstance(buddy, Dog)      # True
type(buddy)                 # <class '__main__.Dog'>
```

### Class vs Instance Attributes
```python
class Counter:
    # Class attribute - shared by ALL instances
    total_count = 0
    
    def __init__(self, name):
        # Instance attribute - unique to EACH instance
        self.name = name
        self.count = 0
        Counter.total_count += 1  # Increment class attribute
    
    def increment(self):
        self.count += 1           # Modify instance attribute

c1 = Counter("A")
c2 = Counter("B")

c1.increment()
c1.increment()
c2.increment()

print(c1.count)             # 2 (instance)
print(c2.count)             # 1 (instance)
print(Counter.total_count)  # 2 (class)
```

---

## 3. Special (Dunder) Methods

"Dunder" methods (double underscore) let you define how objects behave with built-in operations.

### Common Dunder Methods

| Method | Purpose | Called When |
|--------|---------|-------------|
| `__init__(self, ...)` | Constructor | `Dog("Buddy", 3)` |
| `__str__(self)` | User-friendly string | `print(obj)`, `str(obj)` |
| `__repr__(self)` | Developer string | `repr(obj)`, in REPL |
| `__len__(self)` | Return length | `len(obj)` |
| `__eq__(self, other)` | Equality | `obj == other` |
| `__lt__(self, other)` | Less than | `obj < other` |
| `__le__(self, other)` | Less or equal | `obj <= other` |
| `__gt__(self, other)` | Greater than | `obj > other` |
| `__add__(self, other)` | Addition | `obj + other` |
| `__sub__(self, other)` | Subtraction | `obj - other` |
| `__mul__(self, other)` | Multiplication | `obj * other` |
| `__getitem__(self, key)` | Index access | `obj[key]` |
| `__setitem__(self, key, val)` | Index assignment | `obj[key] = val` |
| `__iter__(self)` | Make iterable | `for x in obj` |
| `__next__(self)` | Next item | `next(obj)` |
| `__call__(self, ...)` | Make callable | `obj()` |
| `__contains__(self, item)` | Membership | `item in obj` |
| `__bool__(self)` | Boolean value | `if obj:` |

### Example: Complete Class with Dunder Methods
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """User-friendly string."""
        return f"Point at ({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer string - ideally can recreate object."""
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, other):
        """Check equality."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        """Add two points."""
        return Point(self.x + other.x, self.y + other.y)
    
    def __len__(self):
        """Distance from origin (as int)."""
        return int((self.x**2 + self.y**2)**0.5)

# Usage
p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)               # "Point at (3, 4)"  ← __str__
repr(p1)                # "Point(3, 4)"      ← __repr__
p1 == Point(3, 4)       # True               ← __eq__
p3 = p1 + p2            # Point(4, 6)        ← __add__
len(p1)                 # 5                  ← __len__
```

### Making Objects Iterable
```python
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1, 0
```

---

## 4. Inheritance

Create new classes based on existing ones. Child classes inherit attributes and methods from parent classes.

### Basic Inheritance
```python
# Parent (Base) class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def eat(self):
        return f"{self.name} is eating"

# Child class (inherits from Animal)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # Call parent's __init__
        self.breed = breed          # Add new attribute
    
    def speak(self):                # Override parent method
        return "Woof!"
    
    def fetch(self):                # Add new method
        return f"{self.name} is fetching!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

dog.speak()             # "Woof!" (overridden)
dog.eat()               # "Buddy is eating" (inherited)
dog.fetch()             # "Buddy is fetching!" (Dog only)
dog.breed               # "Golden Retriever"

cat.speak()             # "Meow!" (overridden)
cat.eat()               # "Whiskers is eating" (inherited)

# Check inheritance
isinstance(dog, Dog)     # True
isinstance(dog, Animal)  # True
issubclass(Dog, Animal)  # True
```

### The super() Function
```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, I'm {self.name}"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's __init__
        self.age = age
    
    def greet(self):
        # Call parent's method and extend it
        parent_greeting = super().greet()
        return f"{parent_greeting}, and I'm {self.age} years old"

c = Child("Alex", 10)
c.greet()  # "Hello, I'm Alex, and I'm 10 years old"
```

### Multiple Inheritance
```python
class Flyable:
    def fly(self):
        return "Flying!"

class Swimmable:
    def swim(self):
        return "Swimming!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"

duck = Duck("Donald")
duck.speak()            # "Quack!"
duck.fly()              # "Flying!"
duck.swim()             # "Swimming!"
duck.eat()              # "Donald is eating"

# Method Resolution Order (MRO)
Duck.__mro__
# (<class 'Duck'>, <class 'Animal'>, <class 'Flyable'>, 
#  <class 'Swimmable'>, <class 'object'>)
```

---

## 5. Method Types

### Instance, Class, and Static Methods
```python
class Product:
    # Class attribute
    tax_rate = 0.15
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Instance method - has access to instance (self)
    def get_total(self):
        return self.price * (1 + self.tax_rate)
    
    # Class method - has access to class (cls), not instance
    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate
    
    # Class method - alternative constructor
    @classmethod
    def from_string(cls, product_string):
        name, price = product_string.split(",")
        return cls(name, float(price))
    
    # Static method - no access to instance or class
    @staticmethod
    def is_valid_price(price):
        return price > 0

# Usage
Product.set_tax_rate(0.20)          # Call on class
Product.is_valid_price(100)         # True (static)

item = Product("Laptop", 1000)
item.get_total()                    # 1200.0

# Alternative constructor
item2 = Product.from_string("Phone,500")
item2.name                          # "Phone"
```

### When to Use Each

| Type | Use When | Access |
|------|----------|--------|
| **Instance method** | Need access to instance data | `self` |
| **Class method** | Need to modify class state or create alternative constructors | `cls` |
| **Static method** | Utility function related to class but needs no class/instance data | Neither |

---

## 6. Properties & Encapsulation

Use `@property` to create managed attributes with getters, setters, and deleters.

### Property Decorator
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius       # "Private" by convention
    
    @property
    def radius(self):
        """Getter for radius."""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @radius.deleter
    def radius(self):
        """Deleter."""
        print("Deleting radius")
        del self._radius
    
    @property
    def area(self):
        """Read-only computed property."""
        return 3.14159 * self._radius ** 2
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

# Usage - looks like attribute access!
c = Circle(5)
print(c.radius)         # 5 (calls getter)
c.radius = 10           # Calls setter
print(c.area)           # 314.159 (computed)
c.radius = -5           # Raises ValueError!
del c.radius            # Calls deleter
```

### Naming Conventions for Access Control

| Pattern | Meaning | Example |
|---------|---------|---------|
| `name` | Public - free to access | `self.name = "Dog"` |
| `_name` | Protected - internal use (convention) | `self._balance = 0` |
| `__name` | Private - name mangling applied | `self.__secret = "x"` |
| `__name__` | Dunder - special Python methods | `__init__`, `__str__` |

```python
class BankAccount:
    def __init__(self, balance):
        self.owner = "Public"           # Public
        self._balance = balance         # Protected (convention)
        self.__pin = "1234"             # Private (name mangled)
    
    def get_pin(self):
        return self.__pin

account = BankAccount(100)
account.owner                   # "Public" - accessible
account._balance                # 100 - accessible but "private"
account.__pin                   # AttributeError!
account._BankAccount__pin       # "1234" - name mangling
account.get_pin()               # "1234" - via method
```

---

## 7. Dataclasses (Python 3.7+)

Simplify class creation for classes that mainly store data.

### Basic Dataclass
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

# Automatically generates:
# - __init__
# - __repr__
# - __eq__

user = User("Fana", 25, "fana@example.com")
print(user)         # User(name='Fana', age=25, email='fana@example.com')
user == User("Fana", 25, "fana@example.com")  # True
```

### Dataclass with Defaults and Options
```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0                           # Default value
    tags: List[str] = field(default_factory=list)  # Mutable default
    _internal: str = field(default="", repr=False)  # Exclude from repr
    
    def total_value(self):
        """Can still add regular methods."""
        return self.price * self.quantity

# Usage
p = Product("Laptop", 999.99, 5)
p.tags.append("electronics")
p.total_value()  # 4999.95
```

### Dataclass Options
```python
@dataclass(frozen=True)         # Immutable
class Point:
    x: float
    y: float

p = Point(3, 4)
p.x = 5                         # FrozenInstanceError!

@dataclass(order=True)          # Adds comparison methods
class Person:
    name: str
    age: int

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p1 > p2                         # True (compares field by field)
sorted([p1, p2])                # Sorted by name, then age
```

### Comparison: Regular Class vs Dataclass

```python
# Without dataclass (verbose)
class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age}, email={self.email!r})"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return (self.name, self.age, self.email) == (other.name, other.age, other.email)

# With dataclass (concise)
@dataclass
class User:
    name: str
    age: int
    email: str

# Same functionality with much less code!
```

---

## 8. Abstract Base Classes

Define interfaces that subclasses must implement.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Subclasses must implement this."""
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        """Regular method - can be used as-is."""
        return f"Area: {self.area()}, Perimeter: {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Can't instantiate abstract class
# shape = Shape()  # TypeError!

rect = Rectangle(10, 5)
rect.area()             # 50
rect.perimeter()        # 30
rect.describe()         # "Area: 50, Perimeter: 30"
```

---

## 💡 Pro Tips

1. **Always define `__repr__`** for debugging; define `__str__` for user-friendly output

2. **Use `super()`** to call parent class methods in inheritance

3. **Prefer composition over inheritance** when "has-a" makes more sense than "is-a"
   ```python
   # Inheritance: Dog IS-A Animal
   # Composition: Car HAS-A Engine
   class Car:
       def __init__(self):
           self.engine = Engine()  # Composition
   ```

4. **Use `@dataclass`** for simple data containers—reduces boilerplate significantly

5. **Single underscore `_var`** is convention for "internal"; **double underscore `__var`** triggers name mangling

6. **Use `@property`** to add validation without changing the interface

7. **Keep classes focused** - each class should have a single responsibility

8. **Use abstract base classes** when you want to enforce an interface

9. **Document your classes** with docstrings - describe what the class does and how to use it

10. **Use type hints** for better code readability and IDE support:
    ```python
    def greet(name: str) -> str:
        return f"Hello, {name}"
    ```

---

*Created for W Chats Marketplace*
