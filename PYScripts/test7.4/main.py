team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = "Победила команда Волшебники данных"
restring = "В команде Мастера кода %s участников" % str(team1_num)
print(restring)
print("Итого сегодня в командах %s и %s участников" % (str(team1_num), str(team2_num)))
print("Команда Волшебники данных решила {} задач".format(score2))
print("Волшебники задач решили задачи за {0:.2f} секунд".format(team1_time))
print(f"Команды решили {score1} и {score2} задач")
print(F"Результат битвы: {challenge_result}")
print(f"Было решено {tasks_total} задач. Среднее время решения: {((team1_time/score1) + (team2_time/score2))/2:.2f} секунд")