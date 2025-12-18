class Resource:
    def __init__(self, name, amount=1):
        self.name = name
        self.amount = amount

    def get_amount(self):
        return self.amount

    def info(self):
        return f"Ресурс: {self.name}, Количество: {self.amount}"


class Stick(Resource):
    def __init__(self, amount=1):
        super().__init__('Палка', amount)


class Stone(Resource):
    def __init__(self, amount=1):
        super().__init__('Камень', amount)


class Iron(Resource):
    def __init__(self, amount=1):
        super().__init__('Железо', amount)


class Diamond(Resource):
    def __init__(self, amount=1):
        super().__init__('Алмаз', amount)
