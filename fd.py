class TodoList:
	todo = {}

	def adauga_task(self, nume, descriere):
		self.todo[nume] = descriere

	def finalizeaza_task(self, nume):
		if nume not in self.todo.keys():
			print(f"Task-ul {nume} nu se afla in lista Todo")
		else:
			self.todo.pop(nume)

	def afiseaza_todo_list(self):
		print(f"Task-urile ramase sunt: ", end='')
		print(', '.join(self.todo.keys()))

	def afiseaza_detalii_suplimentare(self, nume_task):
		if nume_task in self.todo.keys():
			print(f"Detaliile suplimentare alea task-ului {nume_task} sunt: {self.todo[nume_task]}")
		else:
			user_choice = input((f"Acest task nu este in lista Todo! Doriti sa il adaugam in lista?(y/n) "))
			if user_choice.lower() == 'y':
				description = input(f"Te rog introdu descrierea pentru noul task! : ")
				self.todo[nume_task] = description


dream_plan = TodoList()
dream_plan.adauga_task('activitate zilnica', 'sa invat programare OOP')
dream_plan.adauga_task('in fiecare seara', 'sa rezolv cu success task-urile primite')
dream_plan.afiseaza_todo_list()
dream_plan.afiseaza_detalii_suplimentare('dezvoltare profesionala')
dream_plan.finalizeaza_task('test')
dream_plan.finalizeaza_task('in fiecare seara')
dream_plan.afiseaza_todo_list()