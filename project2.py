#import random 
import random

intro=input("What is your name?")
print("WELCOME TO CARE MAX DENTAL CLINIC ",intro," Where we value your dental health!")
name=input("Name of the patient: ")
age=input("Age of the patient:")
new_patient=input("Is he/she a new patient(y)?")
if new_patient!="y":
    card_number=input("Enter your card number: ")
    #checking the validity of the card number entered
    if card_number.isdigit():
        card_number=int(card_number)
        if 1 <card_number<121277:
          print("Kindly take a ticket and wait to be called into the consultation room.")
        else:
            print("Card number must be a registered one.")
    else:
        print("Invalid input.")
else:
    print("Kindly proceed to the office desk to register yourself.")

def generate_tickets(num_rooms, num_tickets_per_room):
    all_numbers = list(range(1, num_rooms * num_tickets_per_room + 1))
    random.shuffle(all_numbers)
    tickets = [all_numbers[i * num_tickets_per_room : (i + 1) * num_tickets_per_room] for i in range(num_rooms)]
    return tickets

# Example usage: Generate 4 rooms with 10 tickets each
num_rooms = 4
num_tickets_per_room = 10
consultation_rooms = generate_tickets(num_rooms, num_tickets_per_room)

# Print the ticket numbers for each room
for room_num, room_tickets in enumerate(consultation_rooms, start=1):
    print(f"Consultation Room {room_num}: {room_tickets}")

ticket_number=input("What is your ticket number?: ")
ticket_number=int(ticket_number)

for room_num, room_tickets in enumerate(consultation_rooms, start=1):
    if ticket_number in room_tickets:
        print(f"Ticket number {ticket_number}, proceed to Consultation room {room_num}.")
        break
else:
    print("Invalid ticket number.")