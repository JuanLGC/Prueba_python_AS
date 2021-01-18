#First test case
headlines = [
    {'id': 1, 'xmin': 100, 'xmax': 250, 'ymin': 260, 'ymax': 280},
    {'id': 0, 'xmin': 80, 'xmax': 220, 'ymin': 100, 'ymax': 110}
]

elements = [
    {'id': 2, 'xmin': 100, 'xmax': 200, 'ymin': 10, 'ymax': 90},
    {'id': 3, 'xmin': 150, 'xmax': 250, 'ymin': 140, 'ymax': 240},
    {'id': 4, 'xmin': 100, 'xmax': 120, 'ymin': 160, 'ymax': 200}
]


def segment(headlines, elements):
    headlines.sort(key=lambda y: y['ymin'])
    result = {}
    
    for element in elements:
        for headline in headlines:
            if element['ymax'] < headline['ymin'] and element['xmin'] >= headline['xmin'] and element['xmax'] <= headline['xmax']:
                if headline['id'] in result:
                    result[headline['id']].append(element['id'])
                else:
                    result[headline['id']] = [element['id']]
                break
    return result
        


print(segment(headlines, elements))