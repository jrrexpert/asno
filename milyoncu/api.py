from milyoncu.serializers import ProductAddSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductAddView(APIView):
    authentication_classes = ()
    permission_classes = ()
    throttle_classes = ()
    serializer_class = ProductAddSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        resp = {
            "status": True
        }
        return Response(resp, status=status.HTTP_200_OK)

