class Ticket:
    counter=0
    def __init__(self,source,destination,name):
        self.source=source
        self.destination=destination
        self.name=name
        self.ticket_id=None
    def validate_source_destination(self):
        if(self.source.upper()=="DELHI"):
            if(self.destination.lower() in ["mumbai","chennai", "pune","kolkata"]):
                return True
        else:
            return False
    def generate_ticket(self):
        if self.validate_source_destination()==True:
            Ticket.counter+=1
            self.ticket_id=self.source[0]+self.destination[0]+str(Ticket.counter)
        else:
            self.ticket_id=None

t=Ticket("Delhi","Mumbai","somali")
t.generate_ticket()
print(t.source,t.destination,t.name,t.ticket_id)
t1=Ticket("Delhi","goa","somali")
t1.generate_ticket()
print(t1.source,t1.destination,t1.name,t1.ticket_id)
