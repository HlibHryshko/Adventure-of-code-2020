def part1(file):
    with open(file, 'r') as f:
        numbers = [False for i in range(2020)]

        for line in f:
            numbers[int(line.strip())] = True
        for number in range(1, 2020//2 + 1):
            if numbers[number] and numbers[2020-number]:
                print(number * (2020 - number))
                break

def part2(file):
    with open(file, 'r') as f:
        numbers = [False for i in range(2020)]

        for line in f:
            numbers[int(line.strip())] = True

        for number1 in range(1, 2020//3 + 1):
            for number2 in range(1, 2019//2 + 1):
                if numbers[number1] and numbers[number2] and numbers[2020 - number1 - number2]:
                    print(number1 * number2 * (2020 - number1 - number2))
                    break



def main():
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')


if __name__=='__main__':
    main()