# Q1. What is the meaning of multiple inheritance?

Multiple inheritance is a feature of object-oriented programming languages, including Python, that allows a class to inherit from more than one parent class. In other words, a subclass can have multiple superclasses.

When a class inherits from multiple superclasses, it inherits all the attributes and methods of each superclass. This allows the subclass to combine the behaviors and features of its parent classes, making it more versatile and flexible.


```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Starting engine...")

class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity
    
    def recharge(self):
        print("Recharging battery...")

class ElectricCar(Vehicle, ElectricVehicle):
    def __init__(self, make, model, year, battery_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, battery_capacity)

```


```python
object1=ElectricCar(20,"suv",2023,"2500cc")
```


```python
object1.start_engine()
```

    Starting engine...
    


```python
object1.recharge()
```

    Recharging battery...
    


```python

```
n this example, Vehicle and ElectricVehicle are parent classes of ElectricCar. Vehicle provides attributes and methods for a regular vehicle, while ElectricVehicle provides attributes and methods for an electric vehicle. By inheriting from both of these classes, ElectricCar can represent a car that is both a regular vehicle and an electric vehicle.

The __init__() method of ElectricCar calls the __init__() methods of both parent classes to initialize the attributes of the subclass. The subclass can also use methods from both parent classes, such as start_engine() from Vehicle and recharge() from ElectricVehicle.

Multiple inheritance can be a powerful feature, but it can also make code more complex and harder to maintain. It is important to use multiple inheritance judiciously and to carefully consider the design of the class hierarchy.
# Q2. What is the concept of delegation?

Delegation is a programming concept in which an object passes some of its responsibilities to another object. In other words, an object delegates certain tasks to another object that is better suited to perform them.

In Python, delegation can be achieved by creating an object that holds a reference to another object and calls its methods to perform certain tasks. This object is often referred to as a "delegate" or a "wrapper".


```python
class Printer:
    def __init__(self):
        self._message = ""
    
    def write(self, message):
        self._message += message
    
    def print_message(self):
        print(self._message)

class LogPrinter:
    def __init__(self, printer):
        self._printer = printer
    
    def write(self, message):
        self._printer.write(message)
        print("Logging: " + message)
    
    def print_message(self):
        self._printer.print_message()

```

In this example, Printer is a class that can write messages to the console using the write() method and print them using the print_message() method. LogPrinter is a class that delegates its write and print responsibilities to an instance of Printer. It wraps a Printer instance and adds logging functionality to its write() method.

The LogPrinter class has a reference to a Printer object, which it calls to perform its writing and printing tasks. When the write() method of LogPrinter is called, it calls the write() method of the Printer object and adds logging functionality to it. Similarly, when the print_message() method of LogPrinter is called, it calls the print_message() method of the Printer object.

Delegation can be a powerful technique for building complex and flexible systems. It allows objects to work together in a modular and reusable way, and can make code easier to understand and maintain.

# Q3. What is the concept of composition?

Composition is a programming concept in which objects are combined to create more complex objects. In other words, a composed object contains one or more other objects as components, and uses them to perform its tasks.

In Python, composition can be achieved by creating a class that contains one or more instances of other classes as attributes. These instances can then be used to perform tasks that are required by the composed class.


```python
class Engine:
    def start(self):
        print("Engine started.")
    
    def stop(self):
        print("Engine stopped.")

class Car:
    def __init__(self):
        self._engine = Engine()
    
    def start(self):
        self._engine.start()
    
    def stop(self):
        self._engine.stop()

```

In this example, Engine is a class that represents an engine. It has methods to start and stop the engine. Car is a class that uses an instance of Engine to provide the functionality of a car. It has methods to start and stop the engine by calling the corresponding methods of the Engine instance.

The Car class contains an instance of Engine as an attribute, which is created in its constructor (__init__() method). When the start() method of Car is called, it calls the start() method of the Engine instance, which starts the engine. Similarly, when the stop() method of Car is called, it calls the stop() method of the Engine instance, which stops the engine.

Composition can be a powerful technique for building complex and flexible systems. It allows objects to work together in a modular and reusable way, and can make code easier to understand and maintain.

# Q4. What are bound methods and how do we use them?

In Python, a bound method is a method that is associated with an instance of a class. When a method is called on an instance of a class, it is automatically bound to that instance, which means that the instance is passed as the first argument (self) to the method.

Bound methods can be accessed and called in the same way as regular methods, using the dot notation (instance.method()). They can also be stored as variables, passed as arguments to other functions, and used in other ways that regular functions can be used.


```python
class Counter:
    def __init__(self):
        self._count = 0
    
    def increment(self):
        self._count += 1
    
    def decrement(self):
        self._count -= 1

c1 = Counter()
c2 = Counter()

c1.increment()  # This is equivalent to calling Counter.increment(c1)
c2.decrement()  # This is equivalent to calling Counter.decrement(c2)

print(c1._count)  # Output: 1
print(c2._count)  # Output: -1

increment_func = c1.increment  # Store the bound method as a variable
increment_func()  # Call the bound method

print(c1._count)  # Output: 2

```

    1
    -1
    2
    

In this example, Counter is a class that has two methods, increment() and decrement(), which increment and decrement an internal count variable. Two instances of the class, c1 and c2, are created.

When the increment() and decrement() methods are called on the instances, they are automatically bound to the instances, so the count variable of the correct instance is modified.

The increment() method of c1 is stored as a variable (increment_func), which can be called later. When increment_func() is called, it calls the increment() method of c1 with c1 as the first argument (self).

Bound methods can be useful for building flexible and reusable code. They allow methods to be called on specific instances of a class, and can be passed around and used in the same way as regular functions.

# Q5. What is the purpose of pseudoprivate attributes?

In Python, pseudoprivate attributes are attributes that have a double underscore prefix (__) but do not have a double underscore suffix. These attributes are not truly private, but are rather name-mangled to make them more difficult to access from outside the class.

The purpose of pseudoprivate attributes is to avoid naming conflicts between different attributes in a class hierarchy. When a subclass inherits from a superclass that has an attribute with the same name as an attribute in the subclass, the subclass can use pseudoprivate attributes to give its attribute a unique name that does not conflict with the superclass's attribute.


```python
class A:
    def __init__(self):
        self.__x = 1  # Pseudoprivate attribute
        
class B(A):
    def __init__(self):
        super().__init__()
        self.__x = 2  # Another pseudoprivate attribute

a = A()
b = B()

print(a.__x)  # Raises an AttributeError: 'A' object has no attribute '__x'
print(b.__x)  # Raises an AttributeError: 'B' object has no attribute '__x'

print(a._A__x)  # Output: 1
print(b._A__x)  # Output: 1
print(b._B__x)  # Output: 2

```

    1
    1
    2
    
In this example, A is a class that has a pseudoprivate attribute __x. B is a subclass of A that also has a pseudoprivate attribute __x. When instances of A and B are created, the __x attributes are created and given different values.

When we try to access the __x attributes of a and b using dot notation, we get AttributeErrors, because the pseudoprivate attributes have been name-mangled to _A__x and _B__x, respectively.

Pseudoprivate attributes are not true encapsulation, because they can still be accessed from outside the class by using the mangled name. However, they can help prevent accidental naming conflicts and make code more robust.

```python

```
