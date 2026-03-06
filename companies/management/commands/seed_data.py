import random 
from django.core.management.base import BaseCommand
from companies.models import Company

INDUSTRIES = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing','Education','Energy','Real State','Media']

STATES = ['Uttar Pradesh', 'Jharkhand' , 'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Kolkata']

class Command(BaseCommand):
    help = 'Seed the database with sample company data'

    def add_arguments(self, parser):
        parser.add_argument('--count',type=int, default = 10000, help='Number of companies to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        self.stdout.write(f'Seeding database with {count} companies...  This may take a while.')
        companies = []
        for i in range(kwargs['count']):
            companies.append(Company(
                name = f'Company {i+1}',
                industry = random.choice(INDUSTRIES),
                state = random.choice(STATES),
                annual_revenue = random.randint(10000, 5000000),
                employee_count = random.randint(10, 10000),
                compliance_score = random.uniform(0, 100),
                is_active = random.choice([True,True,True ,False])
            ))
        Company.objects.bulk_create(companies, batch_size=1000)
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {kwargs["count"]} companies'))