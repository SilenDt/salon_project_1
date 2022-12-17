

from models.stylist import Stylist
import repositories.stylist_repository as stylist_repository
from models.client import Client
import repositories.client_repository as client_repository
from models.appointment import Appointment
import repositories.appointment_repository as appointment_repository

#stylists:
stylist_1 = Stylist("Ashleigh Stewart")
stylist_repository.save(stylist_1)

stylist_2 = Stylist("Jayde Hutton")
stylist_repository.save(stylist_2)

stylist_3 = Stylist("Zoe Lastname")
stylist_repository.save(stylist_3)

#clients:
client_1 = Client("Eilidh Morone", "7784049223")
client_repository.save(client_1)

client_2 = Client("Jane Benzies", "7924856445")
client_repository.save(client_2)

client_3 = Client("Sally Smith", "7986443232")
client_repository.save(client_3)

#appointments:
appointment_1 = Appointment(client_1, stylist_2, "Wednesday, 1:00pm")
appointment_repository.save(appointment_1)

