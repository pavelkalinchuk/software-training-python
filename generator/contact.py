import string
import random
import os.path
import json
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
out = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a


def random_string_fio(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_address(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_email():
    symbols = string.ascii_lowercase + string.digits
    return "".join([random.choice(symbols) for i in range(5)]) + "@" + "".join(
        [random.choice(symbols) for i in range(5)]) + "." + "".join([random.choice(symbols) for i in range(3)])


def random_string_phone():
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(11)])


testdata = [
    Contact(
        first_name=random_string_fio(10),
        last_name=random_string_fio(10),
        middle_name=random_string_fio(10),
        address=random_string_address(30),
        email=random_string_email(),
        phone_mobile=random_string_phone(),
        phone_home=random_string_phone(),
        phone_work=random_string_phone(),
        phone_secondary=random_string_phone()) for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", out)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
