from marshmallow import Schema, fields, post_load

from src.model import Album


class AlbumSchema(Schema):
    artist = fields.Str()
    title = fields.Str()
    release_year = fields.Int()
    label = fields.Str()
    cover_url = fields.Url()

    @post_load
    def create_album(self, data):
        return Album(**data)


def load_object():
    album_data = {'artist': 'Osa Da Gnoi',
                  'title': 'G w Stereo',
                  'release_year': 2003,
                  'label': 'Blend Records',
                  'cover_url': 'https://image.ceneostatic.pl/data/products/8681989/i-osa-da-gnoi-g-w-stereo.jpg'}

    album_schema = AlbumSchema()

    album = album_schema.load(album_data)

    print(type(album.data))
    print(album.data)


if __name__ == '__main__':
    load_object()
