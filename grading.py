# Class
class Subject:
    bangla = "Bangla"
    english = "English"
    math = 'Math'
    arabic = 'Arabic'
    physics = 'Physics'

class Student:
    nahid = 'Nahid Hasan'
    nabab = 'Nabab Khan'
    samsu = 'Samsul Islam'
    kawsar = 'Kawsar Bhuyian'
    audry = 'Rahnuma Rah Audry'

# Dictionary
nahid_marks_list={'Bangla': 50, 'English': 80, 'Math': 90, 'Arabic': 75, 'Physics': 100}
nabab_marks_list={'Bangla': 55, 'English': 70, 'Math': 99, 'Arabic': 55, 'Physics': 60}
samsu_marks_list={'Bangla': 20, 'English': 85, 'Math': 44, 'Arabic': 66, 'Physics': 70}
kawsar_marks_list={'Bangla': 80, 'English': 88, 'Math': 40, 'Arabic': 95, 'Physics': 62}
audry_marks_list={'Bangla': 50, 'English': 79, 'Math': 100, 'Arabic': 55, 'Physics': 99}

# List
sub_list=["Bangla","English","Math","Arabic","Physics"]


# Dynamic Method
def get_marks(student_name, sub_list, marks_list):
    total_marks=0
    for subject in sub_list:
        if marks_list[subject]>79 and marks_list[subject]<=100:
            print(student_name+ " got 'A+'  in " +subject)
        elif marks_list[subject]>69 and marks_list[subject]<80:
            print(student_name+ " got 'A' in " +subject)
        elif marks_list[subject]>59 and marks_list[subject]<70:
            print(student_name+ " got 'A-' in " +subject)
        elif marks_list[subject]>49 and marks_list[subject]<60:
            print(student_name+ " got 'B' in " +subject)
        elif marks_list[subject]>39 and marks_list[subject]<50:
            print(student_name+ " got 'D' in " +subject)
        elif marks_list[subject]<40 and marks_list[subject]>=0:
            print(student_name+ " 'failed in' " +subject)
        else:
            print("Sorry! Your Entered Marks Are Not Valid.")
        total_marks=total_marks+marks_list[subject]
    return total_marks

nahid_total_marks=get_marks(Student().nahid, sub_list, nahid_marks_list)
print("Total Marks = ",nahid_total_marks)
print("********************************************************")
audry_total_marks=get_marks(Student().audry, sub_list, audry_marks_list)
print("Total Marks = ",audry_total_marks)
print("********************************************************")
nabab_total_marks=get_marks(Student().nabab, sub_list, nabab_marks_list)
print("Total Marks = ",nabab_total_marks)
print("********************************************************")
kawsar_total_marks=get_marks(Student().kawsar, sub_list, kawsar_marks_list)
print("Total Marks = ",kawsar_total_marks)
print("********************************************************")
samsu_total_marks=get_marks(Student().samsu, sub_list, samsu_marks_list)
print("Total Marks = ",samsu_total_marks)
print("********************************************************")

student_marks_dict={'Nahid Hasan': nahid_total_marks, 'Rahnuma Rah Audry': audry_total_marks, 'Nabab Khan': nabab_total_marks, 'Kawsar Bhuyian': kawsar_total_marks, 'Samsul Islam': samsu_total_marks}

sorted_student_marks_dict=dict(sorted(student_marks_dict.items(), key=lambda item: item[1],reverse=True))

def top_scorer(sorted_student_marks_dict):
    index=0
    for score in sorted_student_marks_dict:
        index=index+1
        if index==1:
            print("Name: ", score, "Marks: ",sorted_student_marks_dict[score], "Position: 1st")
        elif index==2:
            print("Name: ", score, "Marks: ",sorted_student_marks_dict[score], "Position: 2nd")
        elif index==3:
            print("Name: ", score, "Marks: ",sorted_student_marks_dict[score], "Position: 3rd")
        elif index==4:
            print("Name: ", score, "Marks: ",sorted_student_marks_dict[score], "Position: 4th")
        else:
            print("Name: ", score, "Marks: ", sorted_student_marks_dict[score], "Position: 5th")

print(top_scorer(sorted_student_marks_dict))