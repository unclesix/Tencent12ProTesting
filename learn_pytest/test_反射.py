

class Person:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


p = Person("jerry")  #实例化类，并传入name值
print(hasattr(p, "name")) #hasattr判断实例有没有属性、方法
print(getattr(p, "name")) #getattr获取元素的属性值
f = getattr(p,"eat")    #获取实例的属性值并调用eat方法
f()

#查看属性是否存在，如果没有，赋予age，并给予一个默认值20；如果有，则直接拿过来用。
print(getattr(p, "age", "20"))