class RailwayReservationSystem:
    def __init__(self):
        self.confirmed_tickets = []
        self.rac_tickets = []
        self.waiting_list_tickets = []
        self.total_berths = 63
        self.total_rac_berths = 9
        self.total_waiting_list = 10
        self.passenger_id = 1

    def book_ticket(self, name, age, gender, berth_preference):
        ticket = {
            'id': self.passenger_id,
            'name': name,
            'age': age,
            'gender': gender,
            'berth_preference': berth_preference
        }

        if age < 5:
            ticket['status'] = 'Not Allocated (Child)'
            print(f"✘ Ticket for {name} (Age: {age}) is not allocated as age is below 5.")
            self.passenger_id += 1
            return

        if len(self.confirmed_tickets) < self.total_berths:
            if (age > 60 or (gender.lower() == 'female' and age <= 5)) and berth_preference.lower() == 'lower':
                berth_preference = 'lower'
            ticket['status'] = 'Confirmed'
            ticket['berth_preference'] = berth_preference
            self.confirmed_tickets.append(ticket)
        elif len(self.rac_tickets) < self.total_rac_berths:
            ticket['status'] = 'RAC'
            ticket['berth_preference'] = 'side-lower'
            self.rac_tickets.append(ticket)
        elif len(self.waiting_list_tickets) < self.total_waiting_list:
            ticket['status'] = 'Waiting List'
            self.waiting_list_tickets.append(ticket)
        else:
            print("✘ No tickets available.")
            return

        print(f"✔ Ticket booked successfully for {name} (ID: {self.passenger_id})")
        self.passenger_id += 1

    def cancel_ticket(self, ticket_id):
        for ticket in self.confirmed_tickets:
            if ticket['id'] == ticket_id:
                self.confirmed_tickets.remove(ticket)
                if self.rac_tickets:
                    confirmed_ticket = self.rac_tickets.pop(0)
                    confirmed_ticket['status'] = 'Confirmed'
                    self.confirmed_tickets.append(confirmed_ticket)
                    if self.waiting_list_tickets:
                        rac_ticket = self.waiting_list_tickets.pop(0)
                        rac_ticket['status'] = 'RAC'
                        self.rac_tickets.append(rac_ticket)
                print(f"✔ Ticket ID {ticket_id} cancelled successfully.")
                return

        for ticket in self.rac_tickets:
            if ticket['id'] == ticket_id:
                self.rac_tickets.remove(ticket)
                if self.waiting_list_tickets:
                    rac_ticket = self.waiting_list_tickets.pop(0)
                    rac_ticket['status'] = 'RAC'
                    self.rac_tickets.append(rac_ticket)
                print(f"✔ Ticket ID {ticket_id} cancelled successfully.")
                return

        for ticket in self.waiting_list_tickets:
            if ticket['id'] == ticket_id:
                self.waiting_list_tickets.remove(ticket)
                print(f"✔ Ticket ID {ticket_id} cancelled successfully.")
                return

        print(f"✘ Ticket ID {ticket_id} not found.")

    def print_booked_tickets(self):
        if not self.confirmed_tickets and not self.rac_tickets and not self.waiting_list_tickets:
            print("\nℹ No tickets booked.")
            return

        print("\n🟢 Booked Tickets:")
        print("=" * 80)
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Gender':<10} {'Berth Preference':<15} {'Status':<15}")
        print("=" * 80)
        for ticket in self.confirmed_tickets + self.rac_tickets + self.waiting_list_tickets:
            print(f"{ticket['id']:<5} {ticket['name']:<20} {ticket['age']:<5} {ticket['gender']:<10} {ticket['berth_preference']:<15} {ticket['status']:<15}")
        print("=" * 80)
        print(f"Total booked tickets: {len(self.confirmed_tickets) + len(self.rac_tickets) + len(self.waiting_list_tickets)}")

    def print_available_tickets(self):
        available_confirmed = self.total_berths - len(self.confirmed_tickets)
        available_rac = self.total_rac_berths - len(self.rac_tickets)
        available_waiting_list = self.total_waiting_list - len(self.waiting_list_tickets)
        print("\n🟡 Available Tickets:")
        print("=" * 30)
        print(f"Confirmed Tickets: {available_confirmed}")
        print(f"RAC Tickets: {available_rac}")
        print(f"Waiting List Tickets: {available_waiting_list}")
        print("=" * 30)


def main():
    system = RailwayReservationSystem()

    while True:
        print("\n🚂 Railway Reservation System")
        print("=" * 30)
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Print Booked Tickets")
        print("4. Print Available Tickets")
        print("5. Exit")
        print("=" * 30)
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: ").strip())
            gender = input("Enter Gender: ").strip()
            berth_preference = input("Enter Berth Preference (Lower/Middle/Upper/Side-Lower): ").strip()
            system.book_ticket(name, age, gender, berth_preference)
        elif choice == '2':
            ticket_id = int(input("Enter Ticket ID to cancel: ").strip())
            system.cancel_ticket(ticket_id)
        elif choice == '3':
            system.print_booked_tickets()
        elif choice == '4':
            system.print_available_tickets()
        elif choice == '5':
            print("🔚 Exiting the system.")
            break
        else:
            print("✘ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
