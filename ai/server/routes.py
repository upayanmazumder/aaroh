from flask import Blueprint, request, jsonify, current_app
from llm_processor import get_aaroh_output

bp = Blueprint("api", __name__)


@bp.route("/simplify", methods=["POST"])
def simplify_text_endpoint():
    """Accepts JSON {"text": "..."} and returns simplified output + quiz."""
    if not request.is_json or "text" not in request.json:
        return jsonify({"error": "Missing 'text' field in JSON request"}), 400

    complex_text = request.json.get("text")
    current_app.logger.info(
        "Received simplify request; len(text)=%d", len(complex_text or "")
    )

    result, success = get_aaroh_output(complex_text)

    if success:
        return jsonify(result), 200
    else:
        current_app.logger.exception("LLM processing failed")
        return jsonify({"error": result}), 500


@bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200
