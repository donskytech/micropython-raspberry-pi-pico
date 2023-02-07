import ujson

class ReadColorsService():
    def __init__(self):
        pass
    
    def read_colors(self):
        with open('colors.json', 'r') as f:
            colors_dict = ujson.load(f)
            return colors_dict["colors"]
