
# Create your models here.
from django.db import models

# Create your models here.
class manager(models.Model):
	name = models.CharField(max_length=30)

class Center(models.Model):
	city = models.CharField(max_length=30)
	email_id = models.EmailField(max_length=254)
	address = models.CharField(max_length=30)
	lat = models.FloatField()
	lon = models.FloatField()
	phone_no = models.IntegerField()
	date_of_establishment = models.DateField()

	
class Beneficiary(models.Model):
	name  = models.CharField(max_length=90)
	phone_no = models.IntegerField()
	email_id = models.EmailField(max_length=254)
	address =  models.CharField(max_length=30)

	def __str__(self):
		return self.name 



class Hospital(models.Model):
	center_id =  models.ForeignKey(Center, on_delete=models.CASCADE)
	name =  models.CharField(max_length=30)
	address =  models.CharField(max_length=30)
	lat = models.FloatField()
	lon = models.FloatField()

	def __str__(self):
		return self.name 

class Children(models.Model):
	name  = models.CharField(max_length=30)
	beneficiary_id = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
	center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
	recovery_status =  models.CharField(max_length=30)
	def __str__(self):
		return self.name 
	

class Donor(models.Model):
	name = models.CharField(max_length=30)
	email_id = models.EmailField(max_length=254)
	phone_no = models.IntegerField()
	def __str__(self):
		return self.name 




class Transaction(models.Model):
	donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
	center_id = models.ForeignKey(Center, on_delete=models.CASCADE)
	amount = models.IntegerField()
	date =  models.DateField()
	def __str__(self):
		return self.donor_id


class Question(models.Model):
	question_txt = models.CharField(max_length=254)
	category = models.CharField(max_length=25)

class Answers(models.Model):
	question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
	option_number = models.IntegerField()
	center_id = models.ForeignKey(Center, on_delete=models.CASCADE)

class FeedbackStatus(models.Model):
	children_id = models.ForeignKey(Children, on_delete=models.CASCADE)
	status = models.CharField(max_length=25)






