from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import TodoSerializer
from .models import Todo
import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def post(self, request):
        payload = json.loads(request.body)
        points = payload["points"]
        # user = request.user
        try:
            polygon = Todo.objects.create(
                name=payload["name"],
                points=points,
            )
            serializer = TodoSerializer(polygon)

            return JsonResponse({'polygon': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @csrf_exempt
    @permission_classes([IsAuthenticated])
    def put(self, request):
        payload = json.loads(request.body)
        points = payload["points"]
        # user = request.user
        try:
            polygon_item = Todo.objects.filter(id=payload.id)
            polygon_item.update(**payload)
            polygon = Todo.objects.get(id=payload.id)
            serializer = TodoSerializer(polygon)
            return JsonResponse({'polygon': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)