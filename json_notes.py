import json


# ftone = np.argmax(Data)

notes = {200: 'x',259: 'C4', 290: 'D4', 326: 'E4', 346: 'F4', 388: 'G4', 436: 'A4',489: 'B4',518: 'C5', 600: 'x'}

# fclosest = min(notes, key=lambda x: abs(x - ftone))

with open('data.txt', 'w') as outfile:
    json.dump(notes, outfile)