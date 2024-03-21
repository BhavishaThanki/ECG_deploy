from django.urls import path
from .views import MyDataAPIView

urlpatterns = [
    # path('', predict_api, name='predict_api'),
    # path('', get_prediction, name='get_prediction'),
    path('', MyDataAPIView.as_view(), name='my-data'),

]
