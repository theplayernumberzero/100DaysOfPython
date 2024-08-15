student_scores = [10,20,40,12,14,214,40,245,98]

#automatically
print(f"Sum of scores: {sum(student_scores)}")
print(f"Max of scores: {max(student_scores)}")

#manually
max_score=0
total_score=0
for score in student_scores:
    total_score+=score
    if  score > max_score:
        max_score = score
print(f"Sum of scores: {total_score}")
print(f"Max of scores: {max_score}")
