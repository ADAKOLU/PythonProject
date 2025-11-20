import itertools

participants = ['emmanuel', 'francis']
cycle = itertools.cycle(participants)
for i in range(100):
    sender = next(cycle)
    message = input(f"{sender}:")
    if message.lower() == 'bye':
        break
