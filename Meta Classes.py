# Singletoms using metaclasses.
class SingletonType(type):
    def __call__(clscls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance
# Using a metaclass.
type(5)
type(str)
type([1, 2, 3])


# Custom functionality with metaclass.
def __new__(cls,class_name, class_pareetn, class_dict):
    print("Creating class", class_name)
    new_class = super().__new__(cls.class_name, class_pareetn, class_dict)
    return new_class
class Spma(metaclass=VerboseMetaClass):
    def eggs(self):
        print("[insret example string here]")
s = Spam()
s.eggs()


