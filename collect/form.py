from django.forms import ModelForm
from .models import User, Teacher, Test, AnsRecived

class RegNewUsr(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class RegNewTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class NewTest(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class Answer(ModelForm):
    class Meta:
        model = AnsRecived
        fields = '__all__'