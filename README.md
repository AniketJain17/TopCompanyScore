# Company Ranking Backend 

## Setup Instructions

### 1. Clone and Install
git clone https://github.com/AniketJain17/TopCompanyScore.git
cd company_ranking 
python -m venv venv 
venv/scripts/activate
pip install -r requirements.txt

### 2. Run Migrations
python manage.py makemigrations
python manage.py migrate 

### 3. Seed Data 
python manage.py seed_data 
python manage.py seed_data --count 50000 (For 50000 data entry)

### 4. Run server 
python manage.py runserver 

### 5. Calculate Score 
  On postman run - POST /api/companies/calculate 



  API endpoint 
     companies/top/'  : Get Top Companies 
   companies/<int:pk>/' Get company details 


   
