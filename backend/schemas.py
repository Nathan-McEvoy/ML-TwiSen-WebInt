from marshmallow import Schema, fields, validate

class TextInputSchema(Schema):
    text = fields.Str(required=True, validate=lambda s: len(s) > 0)

class TextOutputSchema(Schema):
    result = fields.Str(
        required=True,
        validate=validate.OneOf(['Positive', 'Neutral', 'Negative', 'Irrelevant'])
    )