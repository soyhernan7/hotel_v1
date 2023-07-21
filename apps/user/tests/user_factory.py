# user_factory.py
import factory
from apps.user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@example.com' % n)
    name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    nit = factory.Faker('random_int')
    password = factory.PostGenerationMethodCall('set_password', 'password123')
