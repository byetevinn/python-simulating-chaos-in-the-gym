import random


class Academy:
    def __init__(self):
        self.dumbbells = [i for i in range(10, 36) if i % 2 == 0]
        self.dumbbell_holder = {}
        self.restart_day()

    def restart_day(self):
        self.dumbbell_holder = {i: i for i in self.dumbbells}

    def list_dumbbells(self):
        return [i for i in self.dumbbell_holder.values() if i != 0]

    def list_spaces(self):
        return [i for i, j in self.dumbbell_holder.items() if j == 0]

    def get_dumbbell(self, weight):
        dumbbell_position = list(self.dumbbell_holder.values()).index(weight)
        dumbbell_key = list(self.dumbbell_holder.keys())[dumbbell_position]
        self.dumbbell_holder[dumbbell_key] = 0
        return weight

    def return_dumbbell(self, position, weight):
        self.dumbbell_holder[position] = weight

    def calculate_chaos(self):
        chaos_number = [i for i, j in self.dumbbell_holder.items() if i != j]
        return len(chaos_number) / len(self.dumbbell_holder)


class User:
    def __init__(self, type, academy):
        self.type = type  # 1 - normal | 2 - bagunceiro
        self.academy = academy
        self.weight = 0

    def start_training(self):
        weight_list = self.academy.list_dumbbells()
        self.weight = random.choice(weight_list)
        self.academy.get_dumbbell(self.weight)

    def finish_training(self):
        spaces = self.academy.list_spaces()

        if self.type == 1:
            if self.weight in spaces:
                self.academy.return_dumbbell(self.weight, self.weight)
            else:
                position = random.choice(spaces)
                self.academy.return_dumbbell(position, self.weight)

        if self.type == 2:
            position = random.choice(spaces)
            self.academy.return_dumbbell(position, self.weight)

        self.weight = 0


academy = Academy()

users = [User(1, academy) for i in range(10)]
users += [User(2, academy) for i in range(1)]

random.shuffle(users)


list_chaos = []


for k in range(50):
    academy.restart_day()

    for i in range(10):
        random.shuffle(users)
        for user in users:
            user.start_training()
        for user in users:
            user.finish_training()

        list_chaos += [academy.calculate_chaos()]


list_chaos
