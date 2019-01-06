
class calculate_gpa():

	def __init__(self,allgpa):
		self.allgpa=allgpa

	def add(self,new_gpa):
		self.allgpa.append(new_gpa)

	def mean(self):
 		mean_gpa=sum(self.allgpa)/len(self.allgpa)
 		return mean_gpa


gpa_init=calculate_gpa([])
gpa_init.add(4)
gpa_init.add(5)
gpa_init.add(6)

#print(" Mean of all gpa")
print(gpa_init.mean())