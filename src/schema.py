from marshmallow import Schema, fields


class AlbumSchema(Schema):
    artist = fields.Str()
    title = fields.Str()
    release_year = fields.Int()
    label = fields.Str()
    cover_url = fields.Url()
