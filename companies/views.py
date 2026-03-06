from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Company , CompanyScore
from .serializers import TopCompanySerializer , CompanyDetailSerializer
from .services import calculate_and_store_score


# Create your views here.

class CalculateScoreView(APIView):
    def post(self, request):
        try:
            calculate_and_store_score()
            return Response({"message": "Scores calculated and rank assigned."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TopCompaniesView(APIView):
    def get(self , request):
        limit = int(request.query_params.get('limit', 50))
        industry = request.query_params.get('industry')
        state = request.query_params.get('state')

        queryset = CompanyScore.objects.select_related('company').filter(company__is_active=True).order_by('rank')

        if industry:
            queryset = queryset.filter(company__industry=industry)
        if state:
            queryset = queryset.filter(company__state=state)

        queryset = queryset[:limit]

        results = []
        for cs in queryset:
            company_data = {
                "name": cs.company.name,
                "industry": cs.company.industry,
                "state": cs.company.state,
                "annual_revenue": cs.company.annual_revenue,
                "total_score": cs.total_score,
                "rank": cs.rank
            }
            results.append(company_data)        
        serializer = TopCompanySerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CompanyDetailView(APIView):
    def get(self, request, pk):
        try: 
            company = Company.objects.select_related('score').get(pk=pk)
        except Company.DoesNotExist:
            return Response({"error": "Company not found."}, status=status.HTTP_404_NOT_FOUND)    
       
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)