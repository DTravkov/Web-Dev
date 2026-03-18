from rest_framework.response import Response
from rest_framework import status

class ResponseTemplates:
    @staticmethod
    def ok(data=[], **kwargs):
        return Response({"status" : "200", "data":data, **kwargs}, status=status.HTTP_200_OK)
    @staticmethod
    def no_content(**kwargs):
        return Response({"status" : "204", **kwargs}, status=status.HTTP_204_NO_CONTENT)
    
    @staticmethod
    def not_found(**kwargs):
        return Response({"status" : "404","errors" : ["Entry does not exist"], **kwargs}, status=status.HTTP_404_NOT_FOUND)
    @staticmethod
    def bad_request(errors=[], **kwargs):
        return Response({"status" : "400","errors" : errors, **kwargs}, status=status.HTTP_400_BAD_REQUEST)
    

def get_default_category():
    from .models import ProductCategory
    result, _ = ProductCategory.objects.get_or_create(name="default")
    return result


