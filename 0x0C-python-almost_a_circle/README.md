 # 0x0C - Python - Almost a circle
Task # | Short Description
-------|------------
[Task 0](tests/) | All your files, classes, & methods must be united tested & be pep8 validated. Test compendium.
[Task 1](models/base.py) | class `Base` with private class attribute `__nb_object = 0` & a class constructor.
[Task 1](models/__init__.py) | Init file for class `Base`
[Task 2](models/rectangle.py) | class `Rectangle` that inherits from `Base`.
[Task 3](models/rectangle.py) | Updated class `Rectangle` with validation of all setter methods & instantiation
[Task 4](models/rectangle.py) | Updated class `Rectangle` with public method `def area(self)`.
[Task 5](models/rectangle.py) | Updated class `Rectangle` with public method `def display(self)`.
[Task 6](models/rectangle.py) | Updated class `Rectangle` by overriding the `__str__` method for a custom str rep of class.
[Task 7](models/rectangle.py) | Updated class `Rectangle` by improving public method `def display(self)`.
[Task 8](models/rectangle.py) | Updated class `Rectangle` by adding public method `def update(self, *args)`.
[Task 9](models/rectangle.py) | Updated class `Rectangle` by updating public method `def update(self, *args)` to `update(self, *args, **kwargs)`.
[Task 10](models/square.py) | class `Square` that inherits from Rectangle certain stuff.
[Task 11](models/square.py) | Updated class `Square` with public getter & setter
[Task 12](models/square.py) | Updated class `Square` with public method `def update(self, *args, **kwargs)`.
[Task 13](models/rectangle.py) | Updated class `Rectangle` with public method `def to_dictionary(self)`.
[Task 14](models/square.py) | Updated class `Square` with public method `def to_dictionary(self)`.
[Task 15](models/base.py) | Updated class `Base` by adding static method `def to_json_string(list_dictionaries)`.
[Task 16](models/base.py) | Updated class `Base` by adding class method `def save_to_file(cls, list_objs)`.
[Task 17](models/base.py) | Updated class `Base` by adding static method `def from_json_string(json_string)`.
[Task 18](models/base.py) | Updated class `Base` by adding class method `def create(cls, **dictionary)`.
[Task 19](models/base.py) | Updated class `Base` by adding class method `def load_from_file(cls)`.
 ## Lessons Learned
* What is Unit testing & how to implement it in a large project
* How to serialize & deserialize a Class
* How to write & read a JSON file
* What is `*args` & how to use it
* What is `**kwargs` & how to use it
* How to handle named arguments in a function
