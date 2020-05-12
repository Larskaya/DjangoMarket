from django.db import models

class Computer(models.Model):
	image = models.ImageField(upload_to = 'computers/', max_length = 100)

	name = models.CharField(default = '', max_length = 100)
	price = models.CharField(default = '', max_length = 10)
	ram_size = models.CharField(default = '', max_length = 100) # 8gb
	ram_type = models.CharField(default = '', max_length = 100) # ddr4
	processor = models.CharField(default = '', max_length = 100)
	cpu_frequency = models.CharField(default = '', max_length = 100) # 3600
	processor_cores = models.CharField(default = '', max_length = 100) # 4
	ssd_capacity = models.CharField(default = '', max_length = 100) # 1024

	category = models.CharField(default = '', max_length = 20)

	def __str__(self):
		return self.name

