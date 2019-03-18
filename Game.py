# Guess Game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won')
        break
else:
    print('Try Again')

# Car Simulation
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print('Car is already started')
        else:
            started = True
            print("Car started.")
    elif command == "stop":
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To quit
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand!")

