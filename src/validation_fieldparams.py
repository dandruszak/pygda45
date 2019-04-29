from marshmallow import Schema, fields
from marshmallow.validate import Length


class AlbumSchema(Schema):
    artist = fields.Str(validate=Length(min=10))
    title = fields.Str()
    release_year = fields.Int(required=True)
    label = fields.Str(allow_none=True)
    cover_url = fields.Url()


def load_object():
    album_data = {'artist': 'ESPRIT 空想',
                  'name': 'virtua.zip',
                  'label': '',
                  'cover_url': 'https://f4.bcbits.com/img/a4042324845_10.jpg'}

    album_schema = AlbumSchema()
    album = album_schema.load(album_data)

    print(album.errors)


if __name__ == '__main__':
    load_object()
