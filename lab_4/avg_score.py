kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59,85,30,90]
eng_score = [49,79,48,60,100]
midterm_score = [kor_score, math_score, eng_score]
print (midterm_score[0][2])

total_score_per = [1,2,3,4,5]
avg_score_per = [1,2,3,4,5]

for i in range(0, 5):
    for j in range(0, 3):
        total_score_per[i] += midterm_score[j][i]
    avg_score_per[i] = total_score_per[i] // 3
    print("The average of", i, "is", avg_score_per[i])

# student_score = [0,0,0,0,0]
# i = 0
# for subject in midterm_score:
#     for score in subject:
#         student_score[i] += score
#         i += 1
#     i = 0
# else:
#     a,b,c,d,e = student_score
#     student_average = [a//3,b//3,c//3,d//3,e//3]
#     print(student_average)
