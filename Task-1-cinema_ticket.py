class CinemaTicketSystem:
    def __init__(self):
        self.seats = {
            'A': [False] * 10,
            'B': [False] * 10,
            'C': [False] * 10
        }

    def display_seats(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for row, seats in self.seats.items():
            print(row, end=' ')
            for seat in seats:
                if seat:
                    print('X', end=' ')
                else:
                    print('_', end=' ')
            print()

    def book_ticket(self, row, seat_number):
        row = row.upper()
        if row not in self.seats or seat_number < 1 or seat_number > 10:
            print("Invalid seat selection.")
            return False

        seats = self.seats[row]
        if seats[seat_number - 1]:
            print("Sorry, this seat is already booked.")
            return False

        seats[seat_number - 1] = True
        print("Ticket booked successfully!")
        return True


def main():
    cinema = CinemaTicketSystem()
    while True:
        print("\nWelcome to the Cinema Ticket Booking System")
        print("1. Display Available Seats")
        print("2. Book a Ticket")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            cinema.display_seats()
        elif choice == '2':
            row = input("Enter row (A, B, C): ")
            seat_number = int(input("Enter seat number (1-10): "))
            cinema.book_ticket(row, seat_number)
        elif choice == '3':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
