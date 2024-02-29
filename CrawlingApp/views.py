from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from . import jungna
from CrawlingApp.models import ProductTable

def search_view(request):
    # URL에서 쿼리 매개변수 "query" 가져오기
    query = request.GET.get('query', '')

    # 검색 실행
    jungna.jungna_search(query)
    
    # 검색 결과를 데이터베이스에서 가져오기
    outputDB = jungna.get_products_by_category(query)
    
    # 결과를 렌더링하여 반환
    return render(request, 'search_results.html', {'outputDB': outputDB})