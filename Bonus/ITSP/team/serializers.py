from rest_framework import serializers
from team.models import team , member


class memberSerializer(serializers.ModelSerializer):
    class Meta :
        model = member
        fields = ['member_name']


class teamSerializer(serializers.HyperlinkedModelSerializer):
    myurl = serializers.HyperlinkedIdentityField(view_name= 'team:team-detail' , lookup_field = 'team_id')
    # teamlist = serializers.HyperlinkedIdentityField(view_name= 'team:team-list' , lookup_field='team_id' )
    teammember = memberSerializer(many=True, read_only=True)
    
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='api:team-detail',
    #     lookup_field='team_id',
    #     )

    class Meta :
        model = team
        fields = ['myurl', 'team_id' , 'team_name' , 'teammember' ]


# class MainSerializer(serializers.Serializer):
#     team_api = teamSerializer(many=True)
#     member_api = memberSerializer(many=True)
#     Main = namedtuple('Main', ('team_api', 'member_api'))