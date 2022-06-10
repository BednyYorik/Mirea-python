class FSM:
    def __init__(self):
        self.current_state = 'a'

    def move(self):
        if (self.current_state == 'a'):
            self.current_state = 'b'
            return 0
        elif (self.current_state == 'c'):
            self.current_state = 'd'
            return 3
        elif (self.current_state == 'd'):
            self.current_state = 'f'
            return 5
        elif (self.current_state == 'e'):
            self.current_state = 'f'
            return 6
        elif (self.current_state == 'f'):
            self.current_state = 'g'
            return 8
        else:
            raise KeyError

    def drive(self):
        if (self.current_state == 'b'):
            self.current_state = 'c'
            return 1
        elif (self.current_state == 'e'):
            self.current_state = 'g'
            return 7
        else:
            raise KeyError

    def view(self):
        if (self.current_state == 'b'):
            self.current_state = 'e'
            return 2
        elif (self.current_state == 'd'):
            self.current_state = 'e'
            return 4
        elif (self.current_state == 'f'):
            self.current_state = 'c'
            return 9
        else:
            raise KeyError


def main():
    return FSM()
