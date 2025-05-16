from marshmallow import Schema, fields

class TextInputSchema(Schema):
    text = fields.Str(required=True, validate=lambda s: len(s) > 0)

class BooleanOutputSchema(Schema):
    boolean = fields.Boolean(required=True)