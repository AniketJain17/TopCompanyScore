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


## Indexes
### Company Table
- Added at industry for  fast filter by industry
- annual_revenue for  fast scoring queries
- is_active for  filter active companies only

### CompanyScore Table
- total_score for  fast sorting
- rank for fast rank lookups

## Optimizations
- bulk_create with batch_size=1000 for seeding
- select_related to avoid N+1 queries
- DENSE_RANK() at DB level for ranking
- DB indexes on all filtered/sorted fields
- .only() to fetch minimal fields during scoring
   
