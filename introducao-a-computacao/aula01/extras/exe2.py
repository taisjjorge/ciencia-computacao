#   conversao de segundos em dias/horas/minutos/segundos restantes

enter = int(input("Por favor, entre com o número de segundos que deseja converter: "))

days = enter // 86400
hours_rest = enter % 86400
hours = hours_rest // 3600
minutes_rest = hours_rest % 3600
minutes = minutes_rest // 60
seconds_rest = minutes_rest % 60

print(f"{days} dias, {hours} horas, {minutes} minutos e {seconds_rest} segundos.")


