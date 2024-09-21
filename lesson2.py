num_completed_tusks = 12
num_hours_spent = 1.5
course = "Pyton"
print(num_hours_spent, num_completed_tusks, course)
time = num_hours_spent / num_completed_tusks
print('Курс:',course, ',',
      'всего задач:', num_completed_tusks,','
      'затрачено часов:', num_hours_spent, ',',
      'среднее время выполнения ',time, 'часа')