import random

# Car Class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    # Accelerate method
    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    #Drive method
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

#1.Create one car and print properties
print("=== Part 1 ===")
car = Car("ABC-123", 142)

print("Registration number:", car.registration_number)
print("Maximum speed:", car.max_speed)
print("Current speed:", car.current_speed)
print("Travelled distance:", car.travelled_distance)

#2. Test accelerate method
print("\n=== Part 2 ===")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("Current speed after acceleration:", car.current_speed)

#Emergency brake
car.accelerate(-200)
print("Final speed after brake:", car.current_speed)

#3. Test drive method
print("\n=== Part 3 ===")

car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)

print("Travelled distance after driving:", car.travelled_distance)

#4. Car race simulation
print("\nPart 4: Car Race")
cars = []

#Create 10 cars
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

#Race loop
race_finished = False

while not race_finished:
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race_finished = True
            break

# Print results
print("\nRace Results:")
print(f"{'Reg Number':<10} {'Max Speed':<10} {'Speed':<10} {'Distance':<10}")

for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<10.2f}")