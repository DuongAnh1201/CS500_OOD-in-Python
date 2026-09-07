MIN_SCORE = 0 
MAX_SCORE = 10

#get a list of score from keyboard
def get_score_list():
    score_list_str = input("Enter a list of scores (0-10) separated by a space: ")
    score_list = score_list_str.split(" ")
    for i in range(len(score_list)):
        score_list[i] = int(score_list[i])
    return score_list

def process_scores(l):
    total = 0
    sm = 10
    lg = 0
    #Build a frequency list
    frequent_list = [0]*(MAX_SCORE-MIN_SCORE+1)
    for i in l:
        total += i
        frequent = l.count(i)
        if i<sm:
            sm = i
        if i>lg:
            lg = i
        frequent_list[i] += 1
    most_frequent = 0
    mode_value = -1
    for i in range(len(frequent_list)):
        if frequent_list[i] > most_frequent:
            most_frequent = frequent_list[i]
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
    print(score_list)

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