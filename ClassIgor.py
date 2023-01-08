class Igor:
    'The Igor class is created for teaching of junior students Code add'
    name = 'Igor'
    age = 28
    tall = 175

    def __init__(self, x = 1, y = 1):
        print(f"Constructor X and Y == {x}, {y}")
        self.x = x
        self.y = y

    def __del__(self):
        print(f'I am dead X and Y == {self.x}, {self.y}')

    def vb(self):
        if self.age == 55:
            print('Secret age')
        else:
            return self.age

    def vb2(self):
        print('Function of class')