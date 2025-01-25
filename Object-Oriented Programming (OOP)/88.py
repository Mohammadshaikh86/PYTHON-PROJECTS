class Example:
    class_variable = "I'm a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    def instance_method(self):
        return f"Instance method, can access {self.instance_variable}"

    @classmethod
    def class_method(cls):
        return f"Class method, can access {cls.class_variable}"

    @staticmethod
    def static_method():
        return "Static method, can't access instance or class variables directly"

# Example usage
obj = Example("instance value")
print(obj.instance_method())
print(Example.class_method())
print(Example.static_method())
