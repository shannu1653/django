from django.shortcuts import render
from deepface import DeepFace
import tempfile

# Home page
def upload_page(request):
    return render(request, "upload.html")


def predict_emotion(request):
    if request.method == 'POST':
        file = request.FILES['image']

        # Save uploaded image temporarily
        temp = tempfile.NamedTemporaryFile(delete=False)
        for chunk in file.chunks():
            temp.write(chunk)

        # Analyze emotion
        result = DeepFace.analyze(
            img_path=temp.name,
            actions=['emotion'],
            enforce_detection=False
        )

        # DeepFace returns a list → use first item
        result = result[0]

        # Get main emotion
        emotion = result['dominant_emotion']

        return render(request, "result.html", {"emotion": emotion})

    return render(request, "upload.html")
