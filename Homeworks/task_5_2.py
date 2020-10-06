pupils = [
    {'firstname' : 'Masha',
     'Group' : 12,
     'physics' : 7,
     'informatics': 8,
     'history' : 10,
     },


    {'firstname': 'Sveta',
     'Group': 13,
     'physics': 9,
     'informatics': 3,
     'history': 7,
     },

    {'firstname': 'Dasha',
     'Group': 11,
     'physics': 2,
     'informatics': 6,
     'history': 3
     },

]


for stud in pupils:
    gpa = (stud['physics'] + stud['informatics'] + stud['history']) / len(pupils)
# GPA - grade point average
    print(f"{stud['firstname']}'s average score is: {round(gpa , 2)} ")
    if gpa >= 4:
        print (stud)


