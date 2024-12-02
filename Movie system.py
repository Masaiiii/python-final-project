import datetime
import uuid

class Movie:
    def __init__(self, title, genre, duration, show_times):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.show_times = show_times
        self.total_seats = 50
        self.available_seats = list(range(1, 51))

class Theater:
    def __init__(self):
        self.movies = []
        self.bookings = {}

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\n--- Available Movies ---")
        for idx, movie in enumerate(self.movies, 1):
            print(f"{idx}. {movie.title} - {movie.genre}")
            print(f"   Duration: {movie.duration} minutes")
            print(f"   Show Times: {', '.join(movie.show_times)}")
            print(f"   Available Seats: {len(movie.available_seats)}\n")

    def select_movie(self, movie_index):
        if 1 <= movie_index <= len(self.movies):
            return self.movies[movie_index - 1]
        return None

    def display_seats(self, movie):
        print(f"\n--- Seat Layout for {movie.title} ---")
        for seat in range(1, movie.total_seats + 1):
            print(f"{seat:2d}", end=" ")
            if seat % 10 == 0:
                print()  # New line every 10 seats

    def book_seats(self, movie, selected_seats):
        # Validate seat selection
        for seat in selected_seats:
            if seat not in movie.available_seats:
                print(f"Seat {seat} is already booked!")
                return None

        # Remove selected seats from available seats
        for seat in selected_seats:
            movie.available_seats.remove(seat)

        # Create booking
        booking_id = str(uuid.uuid4())[:8]
        booking = {
            'movie': movie.title,
            'seats': selected_seats,
            'timestamp': datetime.datetime.now(),
            'total_price': len(selected_seats) * 10  # $10 per ticket
        }
        self.bookings[booking_id] = booking

        return booking_id

    def view_booking(self, booking_id):
        booking = self.bookings.get(booking_id)
        if booking:
            print("\n--- Booking Details ---")
            print(f"Booking ID: {booking_id}")
            print(f"Movie: {booking['movie']}")
            print(f"Seats: {booking['seats']}")
            print(f"Total Price: ${booking['total_price']}")
            print(f"Booking Time: {booking['timestamp']}")
        else:
            print("Booking not found.")

def main():
    # Create theater
    theater = Theater()

    # Add movies
    movies = [
        Movie("Inception", "Sci-Fi", 148, ["10:00 AM", "2:00 PM", "6:00 PM"]),
        Movie("The Matrix", "Action", 136, ["11:30 AM", "3:30 PM", "7:30 PM"]),
        Movie("Interstellar", "Sci-Fi", 169, ["12:00 PM", "5:00 PM", "8:30 PM"])
    ]

    for movie in movies:
        theater.add_movie(movie)

    while True:
        print("\n--- Movie Booking System ---")
        print("1. View Movies")
        print("2. Book Movie Tickets")
        print("3. View Booking")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            theater.display_movies()
        
        elif choice == '2':
            theater.display_movies()
            movie_index = int(input("Select a movie (enter number): "))
            selected_movie = theater.select_movie(movie_index)

            if selected_movie:
                theater.display_seats(selected_movie)
                seat_input = input("Enter seat numbers (comma-separated): ")
                selected_seats = [int(seat.strip()) for seat in seat_input.split(',')]

                booking_id = theater.book_seats(selected_movie, selected_seats)
                if booking_id:
                    print(f"\nBooking successful! Your Booking ID is: {booking_id}")
            else:
                print("Invalid movie selection.")
        
        elif choice == '3':
            booking_id = input("Enter your booking ID: ")
            theater.view_booking(booking_id)
        
        elif choice == '4':
            print("Thank you for using the Movie Booking System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()