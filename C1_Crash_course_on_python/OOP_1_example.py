class Elevator:
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
        """Initializes the Elevator instance."""
    def up(self):
        if self.current < self.top:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -=1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
    def __str__(self):
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

# Now add the str method to your Elevator class definition above so that when printing the elevator using the print(
# ) method, we get the current floor together with a message. For example, in the 5th floor it should say "Current
# floor: 5"
elevator.go_to(5)
print(elevator)