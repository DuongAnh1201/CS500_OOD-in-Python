import random
EMPTY = 0
OCCUPIED = 1
RESERVED = 2
# Create a two-dimensional list containing a parking lot
# with randomly assigned parking space values.
# This function returns a two-dimensional list.
def create_parking_lot(size: int) -> list:
    '''
    # Create a two-dimensional list containing a parking lot
    # with randomly assigned parking space values.
    # This function returns a two-dimensional list.
    '''
    parking = [[EMPTY] * size for _ in range(size)] 
    for row in range(size):
        for col in range(size):
            parking[row][col] = random.randint(0,2)
    return parking


def print_parking_lot(parking_lot: list) -> None:
    ''' 
    Print the parking lot from the two-dimensional list.
    . = Empty
    X = Occupied
    R = Reserved
    '''

    for row in parking_lot:
        for col in row:
            if col == 0:
                print(".", end = "")
            elif col == 1:
                print("X", end = "")
            else:
                print("R", end = "")
        print()
# Print statistics about the different types
# of parking spaces.
def print_statistics(parking_lot: list) -> None:
    '''
    Print statistics about the different types of parking spaces.
    '''
    TOTAL_SPACE = pow(len(parking_lot), 2)
    empty_space = 0
    occupied_space = 0
    reserved_space = 0
    for row in parking_lot:
        for col in row:
            if col == 0:
                empty_space += 1
            elif col == 1:
                occupied_space += 1
            else:
                reserved_space += 1
    print("Statistics: ")
    print(f"Empty: {empty_space} ({(empty_space/TOTAL_SPACE*100):.2f}%)")
    print(f"Occupied: {occupied_space} ({(occupied_space/TOTAL_SPACE*100):.2f}%)")
    print(f"Reserved: {reserved_space} ({(reserved_space/TOTAL_SPACE*100):.2f}%)")
    print(f"Total spaces: {TOTAL_SPACE}")

                
def main():
    size = int(input("Please enter the size of the parking lot: "))
    if size<= 0:
        print("ERROR, The size of the parking lot is invalid, please try again")
    parking_lot = create_parking_lot(size)
    print_parking_lot(parking_lot)
    print_statistics(parking_lot)

if __name__ == "__main__":
    main()