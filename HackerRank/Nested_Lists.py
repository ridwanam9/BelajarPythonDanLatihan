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
        
    scores = []
    for x in range(len(nested_lists)):
        scores.append(nested_lists[x][1])

    set_scores = set(scores)
    sorted_scores = list(sorted(set_scores))

    names = []
    # find the names that have secomd lowest score
    for x in range(len(nested_lists)):
        if nested_lists[x][1] == sorted_scores[1]:
            names.append(nested_lists[x][0])
    
    names = sorted(names)
    for name in names:
        print(name)