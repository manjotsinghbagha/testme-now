from django.db import models

# Create your models here.
class Teacher(models.Model):
    username = models.CharField(unique=True,max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    subject = models.CharField(max_length=50)
    institute = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    passward = models.CharField(max_length=20,unique=True)


    def __str__(self):
        return self.username+' '+str(self.subject)

class Test(models.Model):
    creator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    key_or_passward_to_give_test_share = models.CharField(max_length=20,unique=True )

    question_1 = models.CharField(max_length=100)
    q_1_opt_1 = models.CharField(max_length=200)
    q_1_opt_2 = models.CharField(max_length=200)
    q_1_opt_3 = models.CharField(max_length=200)
    q_1_opt_4 = models.CharField(max_length=200)

    question_2 = models.CharField(max_length=100)
    q_2_opt_1 = models.CharField(max_length=200)
    q_2_opt_2 = models.CharField(max_length=200)
    q_2_opt_3 = models.CharField(max_length=200)
    q_2_opt_4 = models.CharField(max_length=200)

    question_3 = models.CharField(max_length=100)
    q_3_opt_1 = models.CharField(max_length=200)
    q_3_opt_2 = models.CharField(max_length=200)
    q_3_opt_3 = models.CharField(max_length=200)
    q_3_opt_4 = models.CharField(max_length=200)

    question_4 = models.CharField(max_length=100)
    q_4_opt_1 = models.CharField(max_length=200)
    q_4_opt_2 = models.CharField(max_length=200)
    q_4_opt_3 = models.CharField(max_length=200)
    q_4_opt_4 = models.CharField(max_length=200)

    question_5 = models.CharField(max_length=100)
    q_5_opt_1 = models.CharField(max_length=200)
    q_5_opt_2 = models.CharField(max_length=200)
    q_5_opt_3 = models.CharField(max_length=200)
    q_5_opt_4 = models.CharField(max_length=200)    
    
    question_6 = models.CharField(max_length=100)
    q_6_opt_1 = models.CharField(max_length=200)
    q_6_opt_2 = models.CharField(max_length=200)
    q_6_opt_3 = models.CharField(max_length=200)
    q_6_opt_4 = models.CharField(max_length=200)    
    
    question_7 = models.CharField(max_length=100)
    q_7_opt_1 = models.CharField(max_length=200)
    q_7_opt_2 = models.CharField(max_length=200)
    q_7_opt_3 = models.CharField(max_length=200)
    q_7_opt_4 = models.CharField(max_length=200)

    question_8 = models.CharField(max_length=100)
    q_8_opt_1 = models.CharField(max_length=200)
    q_8_opt_2 = models.CharField(max_length=200)
    q_8_opt_3 = models.CharField(max_length=200)
    q_9_opt_4 = models.CharField(max_length=200)

    question_9 = models.CharField(max_length=100)
    q_9_opt_1 = models.CharField(max_length=200)
    q_9_opt_2 = models.CharField(max_length=200)
    q_9_opt_3 = models.CharField(max_length=200)
    q_9_opt_4 = models.CharField(max_length=200)

    question_10 = models.CharField(max_length=100)
    q_10_opt_1 = models.CharField(max_length=200)
    q_10_opt_2 = models.CharField(max_length=200)
    q_10_opt_3 = models.CharField(max_length=200)
    q_10_opt_4 = models.CharField(max_length=200)

    def __str__(self):
        return self.key_or_passward_to_give_test_share
    

class User(models.Model):
    username = models.CharField(unique=True,max_length=20)
    rollno = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username+' '+str(self.rollno)

class AnsRecived(models.Model):
    username = models.CharField(max_length=20)
    rollno = models.IntegerField()
    key = models.CharField(max_length=20)
    ans_1 = models.CharField(max_length=200)
    ans_2 = models.CharField(max_length=200)
    ans_3 = models.CharField(max_length=200)
    ans_4 = models.CharField(max_length=200)
    ans_5 = models.CharField(max_length=200)
    ans_6 = models.CharField(max_length=200)
    ans_7 = models.CharField(max_length=200)
    ans_8 = models.CharField(max_length=200)
    ans_9 = models.CharField(max_length=200)
    ans_10 = models.CharField(max_length=200)
    def __str__(self):
        return self.username+ " "+ self.key
    
