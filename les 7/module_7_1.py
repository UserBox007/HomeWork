from importlib.resources import read_text
from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return self.to_str(self)

    def to_str(self, product = None):
        if product is None:
            return self.name + ", " + str(self.weight) + ", " + self.category
        else:
            return product.name + ", " + str(product.weight) + ", " + product.category

class Shop:
    __file_name = 'products.txt'
    def get_products(self):

        file = open(Shop.__file_name, 'r')
        text = str(file.read())
        file.close()

        return text

    def add(self, *products):

        text = self.get_products()
        print(text)

        for product in products:
            index = text.find(product.name + ", " + str(product.weight))
            if index == -1:
                text = text + Product.to_str(product) + "\n"
            else:
                print(f'Продукт {product.name} уже есть в магазине')

            file = open(Shop.__file_name, 'w')
            file.write(text)
            file.close()






s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())