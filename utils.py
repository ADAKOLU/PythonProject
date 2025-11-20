class Chat:
    def __init__(self,participants):
        self.participants = participants
        self.history = []
    def send_message(self,sender,message):
        self.history.append(f"{sender}: {message}")
        print(f"{sender} said: {message}")
    def start_chat(self):
        print("chat started")
        for i in range(100):
            sender = self.participants[i % len(self.participants)]
            message = input(f"{sender}:")
            if message == "quit":
                print(f"{sender} has just quited")
                break
        self.send_message(self.participants,message)
chat = Chat(["emmanuel", "faith"])
chat.start_chat()
