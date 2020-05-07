from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .resources import PersonResource
from .serializers import PersonSerializer
from django.contrib import messages
from tablib import Dataset
from .models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def export(self, request, *args, **kwargs):
        person_resource = PersonResource()
        dataset = person_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="persons.xls"'
        return response

    def simple_upload(self, request, *args, **kwargs):
        if request.method == 'POST':
            person_resource = PersonResource()
            dataset = Dataset()
            new_persons = request.FILES['myfile']
            imported_data = dataset.load(new_persons.read(), format='xlsx')
        # print(imported_data)
            for data in imported_data:
                print(data[1])
                value = Person(
                    data[0],
                )
                value.save()

        #return render(request, 'upload.html')
        return HttpResponse({'message': 'Person created'}, status=200)