from src.schema import AlbumSchema


def load_object():
    album_data = {'artist': 'Dave Rodgers',
                  'name': 'SUPER EUROBEAT presents DAVE RODGERS Special COLLECTION Vol.2',
                  'release_year': 'i am an integer, promise',
                  'label': 'Rodgers & Contini Records',
                  'cover_url': 'not///a----url'}

    album_schema = AlbumSchema()
    album = album_schema.load(album_data)

    print(album.errors)


if __name__ == '__main__':
    load_object()
