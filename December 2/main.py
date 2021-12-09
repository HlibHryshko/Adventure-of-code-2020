def part1(file):
    with open(file, 'r') as f:
        limits = []
        passwords = []

        for line in f:
            limits.append([line.split(':')[0].strip().split()[1].strip()])
            limits[-1] += [int(i.strip()) for i in line.split(':')[0].strip().split()[0].split('-')]
            passwords.append(line.split(':')[1].strip())
        
        counter = 0
        for i in range(len(passwords)):
            count = passwords[i].count(limits[i][0])
            if count >= limits[i][1] and count <= limits[i][2]:
                counter += 1
        print(counter)

def part2(file):
    with open(file, 'r') as f:
        limits = []
        passwords = []

        for line in f:
            limits.append([line.split(':')[0].strip().split()[1].strip()])
            limits[-1] += [int(i.strip()) for i in line.split(':')[0].strip().split()[0].split('-')]
            passwords.append(line.split(':')[1].strip())
        
        counter = 0
        for i in range(len(passwords)):
            if (passwords[i][limits[i][1] - 1] == limits[i][0]) ^ (passwords[i][limits[i][2] - 1] == limits[i][0]):
                counter += 1
        print(counter) 



def main():
    part1('dataset_train.txt')
    part1('dataset.txt')
    part2('dataset_train.txt')
    part2('dataset.txt')


if __name__=='__main__':
    main()