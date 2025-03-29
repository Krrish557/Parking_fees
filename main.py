flag = True  # Controls the main loop of the program
main_text = "\nWelcome to Utopia Parking\nMenu:\n1. View Rates\n2. Check-in and Check-out\n3. Exit "

while flag:
    print(main_text)

    opt = int(input(" >> Select an option: "))

    if opt == 1:  # Display parking rates
        print('''
Time range:    Fees 
0-1 hour       $19
1-2 hours      $29 
2-3 hours      $79 
3-24 hours     $89\n\n''')

    elif opt == 2:  # Handle Check-in and Check-out process
        print("\nCheck-in Time:")
        ch_in_h = int(input(" >> hour (0-23): "))
        ch_in_m = int(input(" >> minute (0-59): "))

        print("\nCheck-out Time:")
        ch_out_h = int(input(" >> hour (0-23): "))
        ch_out_m = int(input(" >> minute (0-59): "))

        # Calculate total parking duration
        hour_diff = ch_out_h - ch_in_h
        minute_diff = ch_out_m - ch_in_m

        if minute_diff < 0:  # Adjust if minute difference is negative
            hour_diff -= 1
            minute_diff += 60

        print(f"** Total parking time: {hour_diff} hours and {minute_diff} minutes")

        # Determine parking fee based on time spent
        if hour_diff == 0 and minute_diff > 0:
            cash_ask = 19
            print("** Total fees: $19")
        elif hour_diff == 1 and minute_diff >= 0:
            cash_ask = 29
            print("** Total fees: $29")
        elif hour_diff == 2 and minute_diff >= 0:
            cash_ask = 79
            print("** Total fees: $79")
        elif hour_diff >= 3:
            cash_ask = 89
            print("** Total fees: $89")
        else:
            print("Invalid Check-out time. Please check your input.")
            continue  # Restart the loop if invalid input

        # Payment processing
        cash_ask_text = ">> Insert cash amount: (1, 2, 5, 10, 20, 50, 100 only)\n"
        total_collected = 0

        while total_collected < cash_ask:  # Loop until the required amount is collected
            cash_submitted = int(input(cash_ask_text))
            total_collected += cash_submitted
            remaining = cash_ask - total_collected

            print(f"** Total collected: ${total_collected}")
            print(f"** Remaining: ${remaining if remaining > 0 else 0}")

            if total_collected >= cash_ask:
                change = total_collected - cash_ask
                if change > 0:
                    print(f"** Change due: ${change}")
                    input("** Please collect your change. Press ENTER when done...")  # Pause for user to collect change
                print("Thanks for parking with us!")
                break  # Exit the payment loop

    elif opt == 3:  # Exit the program
        print("Exiting...")
        flag = False  # Stops the loop

    else:
        print("Invalid option. Please try again.")  # Handle incorrect menu choices
