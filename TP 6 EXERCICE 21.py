
import random
import string
from datetime import datetime, timedelta

def generate_random_data():
    number = random.randint(1, 100)
    letters = ''.join(random.choices(string.ascii_letters, k=5))
    today = datetime.today()
    random_date = today - timedelta(days=random.randint(1, 30))
    return f"{number}, {letters}, {random_date.strftime('%Y-%m-%d %H:%M:%S')}"

with open('random.txt', 'w') as file:
    for _ in range(10):  
        file.write(generate_random_data() + '\n')

with open("random.txt","r") as fic:
    cont = fic.read()
    print(cont)