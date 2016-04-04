def __ask(q, n):
    i = int(input(q))
    if i > n or i <= 0:
        __ask(q, n)
    return i

def EE():
    courses = ['CMPE12',
               'CMPE12L',
               'CMPE100',
               'CMPE100L',
               'CMPE185',
               'CMPE16',
               'CMPE107',
               'MATH23A',
               'MATH23B',
               'PHYS5A',
               'PHYS5B',
               'PHYS5C',
               'PHYS5L',
               'PHYS5M',
               'PHYS5N',
               'PHYS5D',
               'EE101',
               'EE101L',
               'EE103',
               'EE103L',
               'EE171',
               'EE171L',
               'EE151',
               'EE135',
               'EE135L',
               'EE145',
               'EE145L',
               
               ]

    ans = __ask('\
Choose:\n\
1. CMPE13/L\n\
2. CMPS12A/L\n\
3. CMPS5 & CMPS11\n', 3)
    if ans == 1: courses.append('CMPE13'); courses.append('CMPE13L')
    elif ans == 2:
        courses.append('CMPS12')
        courses.append('CMPS12L')
    elif ans == 3:
        ans = __ask('\
Choose:\n\
1. CMPS5C\n\
2. CMPS5J\n\
3. CMPS5P\n', 3)
        if ans == 1:
            courses.append('CMPS5C')
        if ans == 2:
            courses.append('CMPS5J')
        if ans == 3:
            courses.append('CMPS5P')
            
    ans = __ask('\
Choose:\n\
1. MATH19A/B\n\
2. MATH20A/B\n', 2)
    if ans == 1:
        courses.append('MATH19A')
        courses.append('MATH19B')
    elif ans == 2:
        courses.append('MATH20A')
        courses.append('MATH20B')
        
    ans = __ask('\
Choose:\n\
1. AMS10\n\
2. MATH21\n', 2)
    if ans == 1:
        courses.append('AMS10')
    elif ans == 2:
        courses.append('MATH21')
        
    ans = __ask('\
Choose:\n\
1. AMS20\n\
2. MATH24\n', 2)
    if ans == 1:
        courses.append('AMS20')
    elif ans == 2:
        courses.append('MATH24')

    ans = __ask('\
Choose:\n\
1. EE80T\n\
2. CMPE80H\n\
3. TIM80C\n', 3)
    if ans == 1:
        courses.append('EE80T')
    elif ans == 2:
        courses.append('CMPE80H')
    elif ans == 3:
        courses.append('TIM80C')

    ans = __ask('\
Choose:\n\
1. CMPE80E\n\
2. BME80G\n\
3. PHIL22\n\
4. PHIL24\n\
5. PHIL28\n', 5)
    if ans == 1:
        courses.append('CMPE80E')
    elif ans == 2:
        courses.append('BME80G')
    elif ans == 3:
        courses.append('PHIL22')
    elif ans == 4:
        courses.append('PHIL24')
    elif ans == 5:
        courses.append('PHIL28')

    ans = __ask('\
Choose:\n\
1. Communications, Signals, Systems, and Controls concentration\n\
2. Electronics and Optics concentration\n', 2)
    if ans == 1:
        for x in range(0,3):
            ans = __ask('\
Choose:\n\
1. EE130/L\n\
2. EE230\n\
3. EE136\n\
4. EE152\n\
5. EE252\n\
6. EE153\n\
7. EE250\n\
8. EE154\n\
9. EE241\n\
10. EE251\n\
11. EE253\n\
12. EE261\n\
13. EE262\n\
14. EE264\n\
15. CMPE118/L\n\
16. CMPE150/L\n\
17. CMPE251\n', 17)
            if ans == 1:
                courses.append('EE130')
                courses.append('EE130L')
            elif ans == 2:
                courses.append('EE230')
            elif ans == 3:
                courses.append('EE136')
            elif ans == 4:
                courses.append('EE152')
            elif ans == 5:
                courses.append('EE252')
            elif ans == 6:
                courses.append('EE153')
            elif ans == 7:
                courses.append('EE250')
            elif ans == 8:
                courses.append('EE154')
            elif ans == 9:
                courses.append('EE241')
            elif ans == 10:
                courses.append('EE251')
            elif ans == 11:
                courses.append('EE253')
            elif ans == 12:
                courses.append('EE261')
            elif ans == 13:
                courses.append('EE262')
            elif ans == 14:
                courses.append('EE264')
            elif ans == 15:
                courses.append('CMPE118')
                courses.append('CMPE118L')
            elif ans == 16:
                courses.append('CMPE150')
                courses.append('CMPE150L')
            elif ans == 17:
                courses.append('CMPE251')
    elif ans == 2:
        for x in range(0,3):
            ans = __ask('\
Choose:\n\
1. EE104\n\
2. EE115\n\
3. EE130/L\n\
4. EE230\n\
5. EE136\n\
6. EE154\n\
7. EE241\n\
8. EE157/L\n\
9. EE172\n\
10. EE221\n\
11. EE173/L\n\
12. EE175/L\n\
13. EE176/L\n\
14. EE177/L\n\
15. EE178\n\
16. EE180J\n\
17. EE211\n\
18. EE213\n\
19. EE231\n\
20. CMPE118/L\n\
21. CMPE121/L\n\
22. CMPE167/L\n', 22)
            if ans == 1:
                courses.append('EE104')
            elif ans == 2:
                courses.append('EE115')
            elif ans == 3:
                courses.append('EE130')
                courses.append('EE130L')
            elif ans == 4:
                courses.append('EE230')
            elif ans == 5:
                courses.append('EE136')
            elif ans == 6:
                courses.append('EE154')
            elif ans == 7:
                courses.append('EE241')
            elif ans == 8:
                courses.append('EE157')
                courses.append('EE157L')
            elif ans == 9:
                courses.append('EE172')
            elif ans == 10:
                courses.append('EE221')
            elif ans == 11:
                courses.append('EE173')
                courses.append('EE173L')
            elif ans == 12:
                courses.append('EE175')
                courses.append('EE175L')
            elif ans == 13:
                courses.append('EE176')
                courses.append('EE176L')
            elif ans == 14:
                courses.append('EE177')
                courses.append('EE177L')
            elif ans == 15:
                courses.append('EE178')
            elif ans == 16:
                courses.append('EE180J')
            elif ans == 17:
                courses.append('EE211')
            elif ans == 18:
                courses.append('EE213')
            elif ans == 19:
                courses.append('EE231')
            elif ans == 20:
                courses.append('CMPE118')
                courses.append('CMPE118L')
            elif ans == 21:
                courses.append('CMPE121')
                courses.append('CMPE121L')
            elif ans == 22:
                courses.append('CMPE167')
                courses.append('CMPE167L')

    ans = __ask('\
Choose:\n\
1. EE104\n\
2. EE115\n\
3. EE130/L\n\
4. EE230\n\
5. EE136\n\
6. EE154\n\
7. EE241\n\
8. EE157/L\n\
9. EE172\n\
10. EE221\n\
11. EE173/L\n\
12. EE175/L\n\
13. EE176/L\n\
14. EE177/L\n\
15. EE178\n\
16. EE180J\n\
17. EE211\n\
18. EE213\n\
19. EE231\n\
20. CMPE118/L\n\
21. CMPE121/L\n\
22. CMPE167/L\n\
23. EE152\n\
24. EE252\n\
25. EE153\n\
26. EE250\n\
27. EE251\n\
28. EE253\n\
29. EE261\n\
30. EE262\n\
31. EE264\n\
32. CMPE150/L\n\
33. CMPE251\n', 33)
    if ans == 1:
        courses.append('EE104')
    elif ans == 2:
        courses.append('EE115')
    elif ans == 3:
        courses.append('EE130')
        courses.append('EE130L')
    elif ans == 4:
        courses.append('EE230')
    elif ans == 5:
        courses.append('EE136')
    elif ans == 6:
        courses.append('EE154')
    elif ans == 7:
        courses.append('EE241')
    elif ans == 8:
        courses.append('EE157')
        courses.append('EE157L')
    elif ans == 9:
        courses.append('EE172')
    elif ans == 10:
        courses.append('EE221')
    elif ans == 11:
        courses.append('EE173')
        courses.append('EE173L')
    elif ans == 12:
        courses.append('EE175')
        courses.append('EE175L')
    elif ans == 13:
        courses.append('EE176')
        courses.append('EE176L')
    elif ans == 14:
        courses.append('EE177')
        courses.append('EE177L')
    elif ans == 15:
        courses.append('EE178')
    elif ans == 16:
        courses.append('EE180J')
    elif ans == 17:
        courses.append('EE211')
    elif ans == 18:
        courses.append('EE213')
    elif ans == 19:
        courses.append('EE231')
    elif ans == 20:
        courses.append('CMPE118')
        courses.append('CMPE118L')
    elif ans == 21:
        courses.append('CMPE121')
        courses.append('CMPE121L')
    elif ans == 22:
        courses.append('CMPE167')
        courses.append('CMPE167L')
    elif ans == 23:
        courses.append('EE152')
    elif ans == 24:
        courses.append('EE252')
    elif ans == 25:
    	courses.append('EE153')
    elif ans == 26:
    	courses.append('EE250')
    elif ans == 27:
    	courses.append('EE251')
    elif ans == 28:
    	courses.append('EE253')
    elif ans == 29:
    	courses.append('EE261')
    elif ans == 30:
    	courses.append('EE262')
    elif ans == 31:
    	courses.append('EE264')
    elif ans == 32:
    	courses.append('CMPE150')
    	courses.append('CMPE150L')
    elif ans == 33:
    	courses.append('CMPE251')

    ans = __ask('\
Choose:\n\
1. Senior Design Project EE129A/B/C (15 units)\n\
2. Senior Thesis EE195 (12 units)\n', 2)
    if ans == 1:
        courses.append('EE129A')
        courses.append('EE129B')
        courses.append('EE129C')
    elif ans == 2:
        courses.append('EE195')

    print(courses)

    ans = input("Input a comma-separated list of classes you have already taken").upper().replace(" ","").split(",")

    for taken in ans:
        if any(course == taken for course in courses):
            courses.remove(taken)

    return courses
