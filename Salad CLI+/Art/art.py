def read_art(artfile):
    with open(artfile, encoding='utf-8') as f:
        picture = f.read()
    return picture
