from django.contrib import admin
from django.urls import path, include
from gestaoescolar.views import GestaoCreateView, GestaoListView, GestaoUpdateview, GestaoDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GestaoListView.as_view(), name='gestao_list'),
    path('create/', GestaoCreateView.as_view(), name='gestao_create'),
    path('update/<int:pk>/', GestaoUpdateview.as_view(), name='gestao_update'),
    path('delete/<int:pk>/', GestaoDeleteView.as_view(), name='gestao_delete'),
    path('professores/', include('professor.urls'))
]

