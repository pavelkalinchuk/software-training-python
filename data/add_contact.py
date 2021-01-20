from model.contact import Contact

constant = [
    Contact(
        first_name="Иван",
        last_name="Иванов",
        middle_name="Иванович",
        address="Москва, ул. Строителей, 1",
        email="ivan@mail.ru",
        phone_mobile="+7(913)123-23-67",
        phone_home="+7(495)781-22-09",
        phone_work="+7(495)123-20-00",
        phone_secondary="+7(800)100-00-00")
]
#
#
# def random_string_fio(maxlen):
#     symbols = string.ascii_letters
#     return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_string_address(maxlen):
#     symbols = string.ascii_letters + string.digits + " " * 5
#     return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_string_email():
#     symbols = string.ascii_lowercase + string.digits
#     return "".join([random.choice(symbols) for i in range(5)]) + "@" + "".join(
#         [random.choice(symbols) for i in range(5)]) + "." + "".join([random.choice(symbols) for i in range(3)])
#
#
# def random_string_phone():
#     symbols = string.digits
#     return "+" + "".join([random.choice(symbols) for i in range(11)])
#
#
# testdata = [
#     Contact(
#         first_name=random_string_fio(10),
#         last_name=random_string_fio(10),
#         middle_name=random_string_fio(10),
#         address=random_string_address(30),
#         email=random_string_email(),
#         phone_mobile=random_string_phone(),
#         phone_home=random_string_phone(),
#         phone_work=random_string_phone(),
#         phone_secondary=random_string_phone())
# ]
