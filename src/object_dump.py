from src.model import Album
from src.schema import AlbumSchema


def dump_object():
    my_album = Album(artist='DJ Smokey',
                     title='Positive Squad The Soundtrack, Vol. 1',
                     release_year=2017,
                     label='Positive Squad Records',
                     cover_url='https://f4.bcbits.com/img/a0587082445_10.jpg')

    album_schema = AlbumSchema()

    album_dict = album_schema.dump(my_album)
    print(type(album_dict.data))
    print(album_dict.data)

    album_json = album_schema.dumps(my_album)
    print(type(album_json.data))
    print(album_json.data)


if __name__ == '__main__':
    dump_object()
