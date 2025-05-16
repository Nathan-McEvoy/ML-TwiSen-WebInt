from marshmallow import Schema, fields

class TextInputSchema(Schema):
    text = fields.Str(required=True, validate=lambda s: len(s) > 0)

class TextOutputSchema(Schema):
    text = fields.Str(
        required=True,
        validate=lambda s: s in ['Positive' 'Neutral' 'Negative' 'Irrelevant']
    )