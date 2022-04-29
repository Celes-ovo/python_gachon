students = ['Ryan', 'Hansu', 'Jun']
scores = [[90, 85, 91], [92, 95, 88], [87, 94, 96]]

for i in range(0, len(scores)):
  print(students[i], end='\t')

  for j in range(0, 3):
    print(scores[i][j], end='\t')

  total = sum(scores[i])
  print('%d\t%d' %(total, total/3))