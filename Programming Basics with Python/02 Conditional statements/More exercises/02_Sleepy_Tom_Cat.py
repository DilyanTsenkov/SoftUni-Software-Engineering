holidays = int(input())
work_days_play = (365 - holidays) * 63
holidays_play = holidays * 127
play_time_in_minutes = work_days_play + holidays_play
result = 30000 - play_time_in_minutes
if play_time_in_minutes >= 30000:
    print('Tom will run away')
    print(
        f'{abs(result) // 60} hours and {abs(result) % 60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{result // 60} hours and {result % 60} minutes less for play')
