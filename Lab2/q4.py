def convert(mins):
    hour = (mins//60)%24
    minute = (mins%60)
    return f"{hour:02d}:{minute:02d}"
def main():
    print("Finding the time before and after x minutes: ")
    #Get the input
    current_time = input("Enter a time (hh:mm): ")
    shift = int(input("Enter the time shift in minutes: "))

    #Process the input
    current_time_str = current_time.split(":")
    hour = int(current_time_str[0])
    minute = int(current_time_str[1])
    total_current_mins = hour*60 + minute
    after = total_current_mins + shift
    before = total_current_mins - shift
    print("Before: ", convert(before))
    print("After: ", convert(after))

if __name__ == "__main__":
    main()
