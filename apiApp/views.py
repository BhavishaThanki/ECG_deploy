from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MyDataSerializer
from .utils import predict
from rest_framework.response import Response
from rest_framework.views import APIView


class MyDataAPIView(APIView):
    def post(self, request):
        serializer = MyDataSerializer(data=request.data)
        if serializer.is_valid():
            id_value = serializer.validated_data['id']
            prediction_result = predict(id_value)
            return Response({'prediction_result': prediction_result})

        else:
            return Response(serializer.errors, status=400)


# @api_view(['POST'])
# def predict_api(request):
#     id = request.POST.get('id')
#     if id is None:
#         return Response({'error': 'id field is missing'}, status=400)
    
#     prediction_result = predict(id)
#     return Response({'prediction_result': prediction_result})


# @api_view(['GET'])
# def get_prediction(request):
#     id = request.data.get('id')
#     if id is None:
#         return Response({'error': 'ID parameter is missing'}, status=400)

#     # Call the predict function with the provided ID
#     prediction_result = predict(int(id))
#     return Response({'prediction_result': prediction_result})

