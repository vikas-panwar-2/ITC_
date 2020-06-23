from django.shortcuts import render,get_object_or_404
from .models import team,member
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import teamSerializer
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework import generics
def team_detail(request , team_id) :
    obj = team.objects.get(team_id = team_id)
    qs = member.objects.filter(team = obj)
    return render(request,'team_detail.html',{'team' : obj , 'members' : qs})

# def team_detail(request , team_id) :
#     return HttpResponse("my name is khan")
# Create your views here.


@api_view(['GET',])
def api_detail_view(request , team_id):

    try:
        my_team = team.objects.get(team_id = team_id)
    except team.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer1 = teamSerializer(my_team , context={'request': request})
    
    
    return Response(serializer1.data)


@api_view(['GET',])
def api_list_view(request):

    try:
        my_teams = team.objects.all()
    except team.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    serializer = teamSerializer(my_teams , many=True ,  context={'request': request})
    
    return Response(serializer.data)

# class api_list_view(generics.ListAPIView):
#     queryset = team.objects.all()
#     serializer_class = teamSerializer
#     # lookup_field='team_id'

# class api_detail_view(generics.RetrieveAPIView):
#     queryset = team.objects.all()
#     serializer_class = teamSerializer
#     lookup_field = 'team_id'