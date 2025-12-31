def find_second_lowest_score():
        print("Enter number of students:", end=" ")
        
        students = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            students.append([name, score])

        print(students)
        
        # 1. Collect all scores into a simple list
        all_scores = [person[1] for person in students]

        # 2. Use set() to get unique scores, then sort them
        unique_scores = sorted(set(all_scores))

        # 3. The second element (index 1) is the second lowest
        # (Add a check to ensure at least 2 unique scores exist)
        if len(unique_scores) > 1:
            second_lowest = unique_scores[1]

        # 4. Only collect names that match that specific score
        names = [person[0] for person in students if person[1] == second_lowest]

        # 5. Sort alphabetically and print
        names.sort()
        for name in names:
            print(name) 
            

def find_runner_up_score():
    n = int(input())
    arr = map(int, input().split())
    
    # convert map object to list
    arr_list = list(arr)
    
    # convert list to set to remove duplicates
    unique_scores = set(arr_list)
    
    # sort the unique scores
    sorted_scores = sorted(unique_scores)
    
    # the runner-up score is the second element in the sorted list
    print(sorted_scores)
    print(sorted_scores[-2])
    
    # solution 2:
    print(arr_list)
    winner = float('-inf')
    runner_up = float('-inf')
    for score in arr_list:
        if winner < score:
            runner_up = winner
            winner = score
        elif runner_up < score and score != winner:
            runner_up = score
    print(runner_up)

def test_list():
    N = int(input())
    lst = []   
   
    for _ in range(N):
        parts  = input().split()
        print("Parts:", parts)
        cmd = parts[0]

        if cmd == 'insert':
            lst.insert(int(parts[1]), int(parts[2]))
        elif cmd == 'print':
            print(lst)
        elif cmd == 'remove':
            lst.remove(int(parts[1]))
        elif cmd == 'append':
            lst.append(int(parts[1]))
        elif cmd == 'sort':
            lst.sort()
        elif cmd == 'pop':
            lst.pop()
        elif cmd == 'reverse':
            lst.reverse()
    
    
if __name__ == "__main__":

    # runner_up = find_runner_up_score()
    test_list()
    