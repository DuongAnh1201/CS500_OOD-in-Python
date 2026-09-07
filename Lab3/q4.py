def survey():

    menu = ["Pizza", "Hot Dog", "Ham", "Cheese"]

    votes = [
        [0, 0], 
        [0, 0],
        [0, 0],
        [0, 0]
    ]

    while True:
        for i in range(len(menu)):
            answer = input(f"Do you like {menu[i]} (y/n): ")
            if answer.lower() == "y":
                votes[i][0] += 1
            else:
                votes[i][1] += 1
        conf = input("Do you have another student (y/n): ")
        if conf.lower() == "n":
            break

    return menu, votes


def main():
    print("An Electronic Survey of Lunch Menu")
    menu, votes = survey()
    print(f'{"":<15}{"Like":<8}{"Dislike"}')

    for i in range(len(menu)):

        print(f"{menu[i]:<15}{votes[i][0]:<8}{votes[i][1]}")


if __name__ == "__main__":

    main()