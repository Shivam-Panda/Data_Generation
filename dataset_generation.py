from data_generation import generate
import json
import random


# Format
'''
{
    "size": "(15, 15)"
    "target": "(0, 0)",
    "trend": "UP",
    "grid": "[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]"
}
'''

trends = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def generate_dataset(samples, file_name): 
    dataset = []
    for i in range(0, samples):
        # Need to determine parameters and the constraints for parameters for the generate function
        # Randomize all values
        IDEAL = 0.5
        rows = random.randint(10, 50)
        cols = random.randint(10, 50)
        size = (rows, cols)
        target = [random.randint(0, cols-1), random.randint(0, rows-1)]
        trend = trends[random.randint(0, 3)]
        uncertainty = random.random() * 100
        space = random.randint(2, 5)
        grid = generate(rows, cols, target, trend, IDEAL, uncertainty, space)
        data = {
            'size': str(size),
            'target': str(target),
            'trend': trend,
            'grid': grid
        }
        dataset.append(data)
    
    j_obj = json.dumps(dataset, indent=4)

    with(open(file_name, 'w')) as outputfile:
        outputfile.write(j_obj)

generate_dataset(3, 'data.json')