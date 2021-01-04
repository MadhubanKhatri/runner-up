score_lis = [1,2,3,4,5,6,6,6,7,8,9,9,9,10,10,10,10]
print('Current Scores: ', score_lis)

max_num = max(score_lis)
max_num_count = score_lis.count(max_num)

for i in range(0, max_num_count):
	score_lis.remove(max_num)

runner_up = max(score_lis)
print('Runner Up Score is: ', runner_up)	










































# score_lis = [1,2,3,8,8,8,7,7,9,9]
# print('Current Scores: ', score_lis)
# max_num = max(score_lis)
# max_num_count = score_lis.count(max_num)

# for i in range(0, max_num_count):
# 	score_lis.remove(max_num)
# print('Runner Up Score is: ', max(score_lis))