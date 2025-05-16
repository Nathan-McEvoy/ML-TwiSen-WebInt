from flask import Flask
from flask_smorest import Api, Blueprint, abort
from schemas import TextInputSchema, TextOutputSchema
import joblib

app = Flask(__name__)

app.config["API_TITLE"] = "ML Text Sentiment Analysis"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui/"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

model = joblib.load("ml_data/twitter_training.pkl")

mlTextSent_bp = Blueprint('mlTextSent_bp', __name__, url_prefix='/api')

@mlTextSent_bp.route("/text-sentiment", methods=["POST"])
@mlTextSent_bp.arguments(TextInputSchema)
@mlTextSent_bp.response(200, TextOutputSchema)
def check_sentiment(payload):
    text = payload["text"]
    result = model.predict([text])[0]
    valid_outputs = ['Positive', 'Neutral', 'Negative', 'Irrelevant']
    if result not in valid_outputs:
        raise ValueError(f"{result} is not a valid sentiment value")
    else:
        return {"result": result}

api.register_blueprint(mlTextSent_bp)

if __name__ == '__main__':
    app.run(debug=True)