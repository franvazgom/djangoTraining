import json
from .models import Project

class Data:
    def get_test_data(self):
        data = {'nombre':'Juan Pérez'}
        return json.dumps(data)
    
    def get_sum(self, num1, num2):
        sum = num1 + num2
        res = {'sum':sum}
        return json.dumps(res)
    
    def get_projects(self, parameters=None):
        projects = Project.objects.all()
        if parameters:
            if 'title' in parameters:
                projects = projects.filter(title__contains = parameters['title'])
            if 'description' in parameters:
                projects = projects.filter(description__contains = parameters['description'])
        return projects