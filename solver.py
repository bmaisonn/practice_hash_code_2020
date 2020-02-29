import argparse


def pizza_types_from_file(filepath):
    with open(filepath) as f:
        max_pizza_size = int(f.readline().split(' ')[0])
        l = f.readline()
        return max_pizza_size, list((i, int(size)) for (i, size) in enumerate(l.rstrip('\n').split(' ')))
    

def solve(filepath, outfilepath):
    max_pizza_size, pizza_types = pizza_types_from_file(filepath)
    pizza_types = sorted(pizza_types, key=lambda el: el[1], reverse=True)
    
    pizza_sum = 0
    selected_types = []
    for pizza in pizza_types:
        if pizza[1] + pizza_sum > max_pizza_size:
            continue
        selected_types.append(pizza[0])
        pizza_sum += pizza[1]
        
    with open(outfilepath, 'w') as f:
        f.write(f'{len(selected_types)}\n')
        f.write(' '.join([str(t) for t in selected_types])+'\n')
        
    print(selected_types)
    print(pizza_sum)
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    args = parser.parse_args()
    
    solve(args.input, args.output)