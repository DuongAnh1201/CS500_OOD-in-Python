MIN_SCORE = 0 
MAX_SCORE = 10

#get a list of score from keyboard
def get_score_list():
    l =[]
    while True:
        print(f"""Type in the score. Type \"Exit\" to end: """)
        i = input()
        if i == "Exit":
            break
        l.append(int(i))
    return l
def process_scores(l):
    total = 0
    most_frequent = 0
    mode_value = -1
    sm = 10
    lg = 0
    for i in l:
        total += i
        frequent = l.count(i)
        sm = min(i, sm)
        lg = max(i, lg)
        if frequent>most_frequent:
            most_frequent = frequent
            mode_value = i
    if len(l) == 0:
        print("List empty, can't compute the average")
        return None
    else:
        avg = total/len(l)
        return sm, lg, total, avg, mode_value



def show_menu():
    print("=== MENU ===")
    print("1. Find the smallest score")
    print("2. Find the largest score")
    print("3. Find the total score")
    print("4. Find the average score")
    print("5. Find the mode (most frequent) score")
    print("6. Exit")

def main():
    #print the programming title
    print("Finding the smallest, largest, sum, average or mode")

    #Get a list of scores
    score_list = get_score_list()

    #Process scores
    sm, lg, sum, average, mode = process_scores(score_list)
    while True:
        show_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"The smallest score is: {sm}")
        elif choice == 2:
            print(f"The largest score is: {lg}")
        elif choice == 3:
            print(f"The total score is: {sum}")
        elif choice == 4:
            print(f"The average score is: {average}")
        elif choice == 5:
            print(f"The mode (most frequent) score is: {mode}") 
        elif choice == 6:
            print(f"Bye")
            break
        else:
            print("Invalid input, please try again") 
      
if __name__ == "__main__":
    main()