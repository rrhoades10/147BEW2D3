service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def add_ticket(ticket_number, name, issue, status):
    if ticket_number not in service_tickets:
        service_tickets[ticket_number] = {"Customer": name, "Issue": issue, "Status": status}
    else:
        print("That ticket already exists")

    return "Ticket Succesfully Opened"

add_ticket("Ticket003", "Linda", "Dirty Hardrive", "open")

print(service_tickets)
    
