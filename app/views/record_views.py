import re
from app.model.record import Records
from app.serializers.record_serializer import RecordSerializers
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from app.config import record_models

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordSerializers
    permission_classes = [AllowAny]

    def get_record_model(self, record_type):  
        for recordes in record_models:
            if recordes.type == record_type.upper():  # Ensure type is UPPERCASE for consistent matching
                return recordes
        return None

    @action(methods=['POST'], detail=False, url_path='create_record')
    def create_record(self, request):
        try:
            data = request.data
            data['type']=data['record_model'].upper()
            record_model = self.get_record_model(data['type'])
            if record_model is None:
                return Response({"error": "RecordModel type not found"}, status=status.HTTP_400_BAD_REQUEST)
            attributes = data.get('attributes', [])
            for attr in record_model.attributes:
                if attr.is_mandatory:
                    attr_found = False
                    for data_attribute in attributes:
                        if data_attribute['name'].upper() == attr.type and 'value' in data_attribute and data_attribute['value']:
                            attr_found = True
                            break
                    if not attr_found:
                        return Response({"error": f"Attribute '{attr.name}' is mandatory"}, status=status.HTTP_400_BAD_REQUEST)

            for attr in attributes:
                attribute_model = next((am for am in record_model.attributes if am.type == attr['name'].upper()), None)
                if attribute_model:
                    attr['type']=attr['name'].upper()
                    if not re.match(attribute_model.validation, attr['value']):
                        return Response({"error": f"Attribute '{attribute_model.name}' value does not match "}, status=status.HTTP_400_BAD_REQUEST)
            record_serializer = RecordSerializers(data=data)
            if record_serializer.is_valid():
                record_serializer.save()
                return Response(record_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(record_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
