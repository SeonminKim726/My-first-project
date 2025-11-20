class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            items = {}
        self.items = items

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def __add__(self, other):
        combined = ShoppingCart(self.items.copy())  # ← 핵심!!! 복사본으로 시작해야 함
        for item, qty in other.items.items():
            if item in combined.items:
                combined.items[item] += qty
            else:
                combined.items[item] = qty
        return combined

    def __str__(self):
        return f"{self.items}"
    

c1 = ShoppingCart({"tea": 1, "energy drink": 2})
c1.add_item("clock")
print(c1)

c2 = ShoppingCart({"energy drink": 3, "hat": 1})

combined = c1 + c2
print(combined)

