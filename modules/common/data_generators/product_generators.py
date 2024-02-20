from faker import Faker
from .datasets import fruits, fruit_descriptions, vegetables, vegetable_descriptions

fake = Faker()


def product_generator(start, count):
    food_data = []
    for i in range(start, count + 1):
        if i % 2:
            name = fake.unique.random_element(vegetables).capitalize()
            description = fake.random_element(vegetable_descriptions)

        else:
            name = fake.unique.random_element(fruits).capitalize()
            description = fake.random_element(fruit_descriptions)

        quantity = fake.random_int(min=5, max=400)
        food_data.append((i, name, description, quantity))
    return str(food_data)[1:-1]
