def solution(survey, choices):
    # [[R,T], [C,F], [J,M], [A,N]]

    answer_list = []
    dict_a = {}
    for i in range(len(survey)):
        test = survey[i]
        choice = choices[i]
        char = ''
        score = 0
        # print(test, choice)
        if choice == 1:
            # print(test[0], 3)
            char = test[0]
            score = 3
        elif choice == 2:
            # print(test[0], 2)
            char = test[0]
            score = 2
        elif choice == 3:
            # print(test[0], 1)
            char = test[0]
            score = 1
        elif choice == 4:
            pass
        elif choice == 5:
            # print(test[1], 1)
            char = test[1]
            score = 1
        elif choice == 6:
            # print(test[1], 2)
            char = test[1]
            score = 2
        elif choice == 7:
            # print(test[1], 3)
            char = test[1]
            score = 3
        
        
        if char in dict_a:
            dict_a[char] += score
        else:
            dict_a[char] = score
        
    char_list = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']

    if dict_a.get('R', 0) < dict_a.get('T', 0):
        answer_list.append('T')
    else:
        answer_list.append('R')

    if dict_a.get('C', 0) < dict_a.get('F', 0):
        answer_list.append('F')
    else:
        answer_list.append('C')

    if dict_a.get('J', 0) < dict_a.get('M', 0):
        answer_list.append('M')
    else:
        answer_list.append('J')

    if dict_a.get('A', 0) < dict_a.get('N', 0):
        answer_list.append('N')
    else:
        answer_list.append('A')    
    
    # print(''.join(answer_list))
        
    answer = ''
    return ''.join(answer_list)