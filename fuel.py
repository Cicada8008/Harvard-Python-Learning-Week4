def main():

    while True:

        try:

            # Prompt the user for input

            fraction = input("Fraction: ")



            # Split the input into X and Y

            x, y = fraction.split("/")



            # Convert X and Y into integers

            x = int(x)

            y = int(y)



            # Check for valid fraction

            if y == 0:

                raise ZeroDivisionError

            if x > y:

                raise ValueError



            # Calculate the percentage

            percentage = (x / y) * 100



            # Output based on the percentage

            if percentage <= 1:

                print("E")

            elif percentage >= 99:

                print("F")

            else:

                print(f"{round(percentage)}%")



            # Exit the loop if we successfully get a valid input

            break



        except (ValueError, ZeroDivisionError):

            # Catch exceptions and prompt the user again

            pass



if __name__ == "__main__":

    main()
