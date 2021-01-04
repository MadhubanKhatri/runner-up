# Create a Score List
score_lis = [1,2,3,4,5,6,6,6,7,8,9,9,9,10,10,10,10]

# Print the List
print('Current Scores: ', score_lis)

# Get Max Number from the list
max_num = max(score_lis)

# Count the Max Number 
max_num_count = score_lis.count(max_num)

# Apply for loop and remove Max Number from the list
for i in range(0, max_num_count):
	score_lis.remove(max_num)


# Now Max Number becomes the Runner Up Score
runner_up = max(score_lis)

# Print it
print('Runner Up Score is: ', runner_up)
