from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    cleaner_obj = Cleaner(cleaner)
    list_of_customers = []
    for customer in customers:
        cs = Customer(customer["name"], customer["food"])
        list_of_customers.append(cs)
        CinemaBar.sell_product(cs, cs.food)
    cinema_hall = CinemaHall(hall_number)
    cinema_hall.movie_session(movie, list_of_customers, cleaner_obj)
