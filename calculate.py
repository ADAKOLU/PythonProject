from Converters import participants


class Chat:
    def __init__(self, participant):
        self.participant = participant
        self.history = []
    def send_message(self,sender,message):
        self.history.append(f"{sender}: {message}")
        print(f"{sender} said: {message}")
    def start_chat(self):
        print("===start_chat===")
        for i in range(100):
            sender = self.participant[i % len(self.participant)]
            message = input(f"{sender}:")
            if message == "bye":
                print(f"{participants}: good bye")
                break
        self.send_message(self.participant,message)
chat = Chat(["emmanuel","francis"])
chat.start_chat()

