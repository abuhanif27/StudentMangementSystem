import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from students.models import Student

# Delete all existing students
print("Deleting all existing student records...")
deleted_count = Student.objects.all().delete()[0]
print(f"Deleted {deleted_count} existing student records")

# Create 10 demo students from Bangladesh
bangladesh_students = [
    {
        'name': 'Tanvir Ahmed',
        'email': 'tanvir.ahmed@gmail.com',
        'phone': '01712345678',
        'course': 'Computer Science & Engineering'
    },
    {
        'name': 'Fatima Akter',
        'email': 'fatima.akter@gmail.com',
        'phone': '01823456789',
        'course': 'Business Administration'
    },
    {
        'name': 'Rahim Khan',
        'email': 'rahim.khan@gmail.com',
        'phone': '01934567890',
        'course': 'Electrical & Electronic Engineering'
    },
    {
        'name': 'Nusrat Jahan',
        'email': 'nusrat.jahan@gmail.com',
        'phone': '01645678901',
        'course': 'Economics'
    },
    {
        'name': 'Kamal Hossain',
        'email': 'kamal.hossain@gmail.com',
        'phone': '01756789012',
        'course': 'Information Technology'
    },
    {
        'name': 'Sabina Yasmin',
        'email': 'sabina.yasmin@gmail.com',
        'phone': '01867890123',
        'course': 'Textile Engineering'
    },
    {
        'name': 'Masud Rahman',
        'email': 'masud.rahman@gmail.com',
        'phone': '01978901234',
        'course': 'Civil Engineering'
    },
    {
        'name': 'Tania Islam',
        'email': 'tania.islam@gmail.com',
        'phone': '01689012345',
        'course': 'Pharmacy'
    },
    {
        'name': 'Imran Hasan',
        'email': 'imran.hasan@gmail.com',
        'phone': '01790123456',
        'course': 'Architecture'
    },
    {
        'name': 'Sadia Rahman',
        'email': 'sadia.rahman@gmail.com',
        'phone': '01601234567',
        'course': 'English Literature'
    }
]

# Insert students into the database
count = 0
for student_data in bangladesh_students:
    student = Student(**student_data)
    student.save()
    print(f"Created student: {student.name}")
    count += 1

print(f"Demo data creation completed. Added {count} students from Bangladesh.") 