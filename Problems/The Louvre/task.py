class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year


paint_title = input()
paint_painter = input()
paint_year = input()
paint = Painting(paint_title, paint_painter, paint_year)
print(f'"{paint.title}" by {paint.painter} ({paint.year}) hangs in the {Painting.museum}.')
