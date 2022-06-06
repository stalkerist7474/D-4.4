from django.urls import path
from .views import NewsList, NewsDetail, NewsListForSearck, NewsCreateView, NewsDeleteView, NewsUpdateView
 
 
urlpatterns = [
    
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='newsDetail'), 
    path('search', NewsListForSearck.as_view()),
    path('add/', NewsCreateView.as_view(), name='create_news'), 

    path('edit/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete')

]