import random


COLORS = ["r", "b", "g", "w", "c", "y", "o"]
SIZE = 5


def make_sequence():
    sequence = [random.choice(COLORS) for _ in range(SIZE)]
    return sequence

def check(sequence, attempt):
    in_place = 0
    in_sequence = 0
    for idx, item in enumerate(attempt):
        if item == sequence[idx]:
            in_place += 1
            continue
        if item in sequence:
            in_sequence += 1

    return in_place, in_sequence

def is_correct(attemp):
    for idx, item in enumerate(attemp):
        if item not in COLORS:
            return False, idx
    return True, -1

def main():
    print("Available colors: %r" % COLORS)
    sequence = make_sequence()
    try:
        while True:
            attempt_str = input()
            if attempt_str == "SHOW":
                print(" ".join(sequence))
            attempt = attempt_str.split()
            state, idx = is_correct(attempt)
            if not state:
                print("Wrong symbol: %s" % attempt[idx])
                continue
            in_place, in_sequence = check(sequence, attempt)
            print("in place: %d, in sequence %d" % (in_place, in_sequence))
            if in_place == SIZE:
                print("sequence %s" % " ".join(sequence))
                print("You win!")
                break
    except KeyboardInterrupt:
        print("Bye!")



if __name__ == "__main__":
    main()
