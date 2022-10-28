import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'test_firstname'
    last_name = 'test_lastname'
    username = 'test_username'
    email = 'test_email'
    password = 'qwerty'
    birth_date = factory.Faker('date_object')

    class Meta:
        model = 'users.User'


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'


class AdFactory(factory.django.DjangoModelFactory):
    name = 'Ad'
    author = factory.SubFactory(UserFactory)
    price = 1

    class Meta:
        model = 'ads.Ad'
