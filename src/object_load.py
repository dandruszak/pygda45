from src.schema import AlbumSchema


def load_object():
    album_data = {'artist': 'Osa Da Gnoi',
                  'title': 'G w Stereo',
                  'release_year': 2003,
                  'label': 'Blend Records',
                  'cover_url': 'https://image.ceneostatic.pl/data/products/8681989/i-osa-da-gnoi-g-w-stereo.jpg'}

    album_schema = AlbumSchema()

    album = album_schema.load(album_data)

    print(type(album))
    print(album)


if __name__ == '__main__':
    load_object()
