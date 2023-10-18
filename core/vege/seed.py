from faker import Faker
import random 
fake = Faker()
from .models import *

def seed_db(n=10)->None:
    
    depts = Department.objects.all()
    random_idex = random.randint(0, len (depts))

    try:

        for i in range(0, n):
            department = depts[random_idex]
            student_id = f'STU-0{random.randint(0 ,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20 , 30)
            student_address = fake.address()

            student_id_obj = studentID.objects.create(student_id = student_id)

            student_obj = student.objects.create (
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address

            )

    except Exception as e:
        print(e)