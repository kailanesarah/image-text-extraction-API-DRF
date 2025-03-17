from django.http import JsonResponse
from rest_framework.response import Response
import pytesseract
from PIL import Image
from deep_translator import GoogleTranslator
from rest_framework import status
import language_tool_python



def extract_text_from_image( image):
    return pytesseract.image_to_string(Image.open(image))


def correct_text(text):
    tool = language_tool_python.LanguageTool('pt-br')
    tool.enabled_rules = ["PT_MA", "PT_VS"]
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text


def get_translation_request_data(request):
    try:
        original_text = request.data.get("text")
        source_lang = request.data.get("source")
        target_lang = request.data.get("target")

        if not original_text or not source_lang or not target_lang:
            return None

        return {
            "original_text": original_text,
            "source_lang": source_lang,
            "target_lang": target_lang}
    except Exception as e:
        return Response({"error": f"Error while capturing request data: {str(e)}"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def translate_text(original_text, source_lang, target_lang):
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        translated_text = translator.translate(original_text)
        return translated_text

    except Exception as e:
        return Response({"error": f"Error while translating the text: {str(e)}"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
