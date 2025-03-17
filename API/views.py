from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
import pytesseract
from deep_translator import GoogleTranslator
from API.utils import  extract_text_from_image, correct_text, get_translation_request_data, translate_text


'''O tesseract sempre apresenta um erro. 
Se não resolver adicionando o caminho ao path, use
essa segunda opção e coloque o caminho diretamente no arquivo'''

caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"

class ExtractTextImageView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def post(self, request):
        image= request.FILES.get('image')

        if not image:
            return JsonResponse({"message": "Nenhuma imagem foi recebida."}, status=400)

        try:
            text_image = extract_text_from_image(image)
            cleaned_text = text_image.replace('\n', ' ')
            #final_text = correct_text(cleaned_text)

            return Response({
                "message": "Imagem recebida!",
                "filename": image.name,
                "size": image.size,
                #"text_image": final_text,
                "text_image": cleaned_text
            })
        except Exception as e:
            return JsonResponse({"error": f"Erro ao processar a imagem: {str(e)}"}, status=500)


class TranslateTextImageView(APIView):
    permission_classes = [AllowAny]
    IDIOMAS_SUPORTADOS = GoogleTranslator().get_supported_languages(as_dict=True)

    def post(self, request):
        dados_request = get_translation_request_data(request)

        if not dados_request:
            return JsonResponse({"error": "Dados faltando. Certifique-se de enviar 'text', 'source' e 'target'."}, status=400)

        text = dados_request["original_text"]
        source = dados_request["source_lang"]
        target = dados_request["target_lang"]

        try:
            translated_text = translate_text(text, source, target)
            return JsonResponse({"translated_text": translated_text})
        except Exception as e:
            return JsonResponse({"error": f"Erro ao traduzir o texto: {str(e)}"}, status=500)
