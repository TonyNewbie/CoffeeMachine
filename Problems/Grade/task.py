score = float(input())
max_score = float(input())
score_percent = score / max_score * 100
if score_percent >= 90:
    print('A')
elif score_percent >= 80:
    print('B')
elif score_percent >= 70:
    print('C')
elif score_percent >= 60:
    print('D')
else:
    print('F')
