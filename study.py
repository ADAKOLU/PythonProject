class Chat:
    def __init__(self, participant):
        self.participant = participant
        self.history = []
    def send_message(self,sender,message):
        self.history.append(f"{sender}: {message}")
        print(f"{sender} said: {message}")
    def start_chat(self):
        print("=== Chat Started ===")
        for i in range(100):
            sender = self.participant[i % len(self.participant)]
            message = input(f"{sender}: ")
            if message.lower() == "quit":
                print(f"{sender} ended the chat.")
                break
        self.send_message(self.participant, message)
        print("=== Chat Ended ===")
chat = Chat(["Person 1", "Person 2"])
chat.start_chat()

