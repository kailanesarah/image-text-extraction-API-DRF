from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
import pytesseract
from PIL import Image
from spellchecker import SpellChecker


'''O tesseract sempre apresenta um erro. 
Se não resolver adicionando o caminho a path, use
essa segunda opção e coloque o caminho diretamente no arquivo'''

caminho_tesseract = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"


class ExtractTextImageView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [AllowAny]

    def getImageRequest(self, request):
        return request.FILES.get('image')

    def extractTextImageRequest(self, image):
        return pytesseract.image_to_string(Image.open(image))

    def corretionTextImageRequest(self, textImage):
        spell = SpellChecker()
        return spell.correction(textImage)

    def post(self, request, *args, **kwargs):
        image = self.getImageRequest(request)

        if not image:
            return JsonResponse({"Message": "Nenhuma imagem foi recebida"}, status=400)

        textImage = self.extractTextImageRequest(image)
        correctionText = self.corretionTextImageRequest(textImage)
        cleanedText = correctionText.replace('\n', ' ')

        return Response({
            "message": "Imagem recebida!",
            "filename": image.name,
            "size": image.size,
            "Text Image": cleanedText

        })


class TranslateTextImageView(APIView):
    def get(self, request):
        return JsonResponse({"message": "Traduzindo texto da imagem"})
