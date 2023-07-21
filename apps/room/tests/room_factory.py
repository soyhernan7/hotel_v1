import factory
from factory.django import DjangoModelFactory
from apps.room.models import Room


class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    type = factory.Iterator(Room.RoomTypes.choices, getter=lambda c: c[0])
    description = factory.Faker('text')
    price_per_day = factory.Faker('pydecimal', right_digits=2, positive=True, min_value=20, max_value=200)
    discount_rate = factory.Faker('random_int', min=0, max=100)
    is_available = True  # Todas las habitaciones creadas estarán disponibles
