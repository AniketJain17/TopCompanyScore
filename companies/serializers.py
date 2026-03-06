from rest_framework import serializers
from .models import Company, CompanyScore


class TopCompanySerializer(serializers.Serializer):
    name = serializers.CharField()
    industry = serializers.CharField()
    state = serializers.CharField()
    annual_revenue = serializers.FloatField()
    total_score = serializers.FloatField()
    rank = serializers.IntegerField()


class CompanyDetailSerializer(serializers.Serializer):
    total_score = serializers.SerializerMethodField()
    rank = serializers.SerializerMethodField()

    class Meta: 
        model = Company
        fields = ['name', 'industry', 'state', 'annual_revenue', 'employee_count', 'compliance_score', 'total_score', 'rank']
    

    def get_total_score(self, obj):
        try:
            return obj.score.total_score
        except CompanyScore.DoesNotExist:
            return None
        

    def get_rank(self, obj):
        try:
            return obj.score.rank
        except CompanyScore.DoesNotExist:
            return None    