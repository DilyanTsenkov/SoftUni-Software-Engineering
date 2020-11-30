class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        Catalogue.products.append(product)
        Catalogue.products.sort()

    def get_by_letter(self, first_letter):
        letter = []
        for el in Catalogue.products:
            if el[0] == first_letter:
                letter.insert(-1, el)
        return letter

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(Catalogue.products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))
print(catalogue)

