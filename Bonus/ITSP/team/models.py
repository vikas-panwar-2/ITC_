from django.db import models
from uuid import uuid4
def create_id():
    return 'ITS'+ str(uuid4())[:10]

class team (models.Model):
    team_id = models.CharField(primary_key=True, default=create_id, editable=False, max_length=20 )
    team_name = models.CharField(max_length=255)
        
        
    def __str__(self):
        return f'{self.team_name}'

class member (models.Model):
    member_name = models.CharField(primary_key=True, default=create_id, editable=False, max_length=20)
    team = models.ForeignKey(team,related_name = 'teammember' ,on_delete=models.CASCADE)