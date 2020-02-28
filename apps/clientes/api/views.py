from apps.clientes.models import Cliente
from rest_framework import viewsets
from apps.clientes.api.serializers import ClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):

        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer

        #def get(self, request, *args, **kwargs):
        #    return self.retrieve(request, *args, **kwargs)

        def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
        """

            cpfcnpj = self.request.query_params.get('cpfcnpj')
            pwd = self.request.query_params.get('password')
            if cpfcnpj and pwd:
                return Cliente.objects.filter(cpf_cnpj=cpfcnpj,appPassword=pwd,appHabilitado=True)
            else:
                return Cliente.objects.all()
            ##senha = self.kwargs['password']
            #return Cliente.objects.filter(cpf_cnpj=cpfcnpj,appPassword='',appHabilitado=True)



        '''
        def put(self, request, *args, **kwargs):
            return self.update(request, *args, **kwargs)
        
        def delete(self, request, *args, **kwargs):
            return self.destroy(request, *args, **kwargs)
        '''

class ClienteList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Cliente.objects.all()
        serializer = ClienteSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




