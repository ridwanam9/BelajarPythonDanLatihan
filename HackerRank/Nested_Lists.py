# Given the names and grades for each student in a class of  
# students, store them in a nested list and print the name(s) 
# of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second 
# lowest grade, order their names alphabetically 
# and print each name on a new line.

if __name__ == '__main__':
    nested_lists = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_lists.append([name, score])

    sorted_by_lowest_score = sorted(nested_lists, key=lambda x: x[1])

    set_of_score = []

    # remove dupliacate score by converting the list into set
    for x in range(len(sorted_by_lowest_score)):
        set_of_score.append(sorted_by_lowest_score[x][1])

    # find the names that have secomd lowest score
    for x in range(len(sorted_by_lowest_score)):
        if sorted_by_lowest_score[x][1] == set_of_score[1]:
            print(sorted_by_lowest_score[x][0])


