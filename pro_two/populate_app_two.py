import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_two.settings')

import django
django.setup()

# Fake Script
import random
from apptwo.models import User
from faker import Faker

fakegen = Faker()

# def add_user():
#     t = User.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        # top = add_topic()

        # Create fake data
        fake_first_name, fake_last_name = fakegen.name().split(" ")
        fake_email = str(fake_first_name)+"@"+str(fake_last_name)+".com"

        # Create the new webpage entry
        user = User.objects.get_or_create(
            first_name=fake_first_name,
            last_name=fake_last_name,
            email=fake_email)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('Populate complete')
