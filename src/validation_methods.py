from marshmallow import Schema, fields, validates, ValidationError


class AlbumSchema(Schema):
    artist = fields.Str()
    title = fields.Str()
    release_year = fields.Int()
    label = fields.Str()
    cover_url = fields.Url()

    @validates('artist')
    def validate_artist_is_hype(self, artist):
        if not artist.lower().startswith('lil'):
            raise ValidationError('Not hype enough :C')


def load_object():
    album_data = {'artist': 'Krzysztof Komeda',
                  'name': 'Astigmatic',
                  'release_year': 1966,
                  'label': 'Muza',
                  'cover_url': 'https://upload.wikimedia.org/wikipedia/en/3/32/Krzysztof_Komeda_-_Astigmatic.jpg'}

    album_schema = AlbumSchema()
    album = album_schema.load(album_data)

    print(album.errors)


if __name__ == '__main__':
    load_object()
