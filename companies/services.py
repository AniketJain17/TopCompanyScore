from django.db import connection
from .models import Company, CompanyScore


def calculate_scores(annual_revenue , compliance_score):
    revenue_Score = min(annual_revenue / 10000, 100) 
    total_Score = (revenue_Score * 0.6) + (compliance_score * 0.4) 
    return round(total_Score, 2)


def calculate_and_store_score():
    active_companies = Company.objects.filter(is_active=True).only('id', 'annual_revenue', 'compliance_score')

    to_create = []
    to_update = []

    existing_scores = CompanyScore.objects.filter(company__in=active_companies).values_list('company_id', flat=True) 
    existing_ids = set(existing_scores)

    for company in active_companies:
        score = calculate_scores(company.annual_revenue, company.compliance_score)

        if company.id in existing_ids:
            cs = CompanyScore(company=company, total_score=score)
            to_update.append(cs)

        else:
            to_create.append(CompanyScore(company=company, total_score=score))  

    if to_create:
        CompanyScore.objects.bulk_create(to_create)

    if to_update:
        CompanyScore.objects.filter(company_id__in=[cs.company_id for cs in to_update]).delete()   
        CompanyScore.objects.bulk_create(to_update)

    assign_ranks()    


def assign_ranks():

    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE companies_companyscore 
            SET rank = ranked.dense_rank
            FROM (
               SELECT id , DENSE_RANK() OVER (ORDER BY total_score DESC) AS dense_rank
                FROM companies_companyscore
            ) AS ranked
            WHERE companies_companyscore.id = ranked.id
        """)
