# example/views.py
from datetime import datetime
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from vercel_app.process_file import create_latex_file

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)

@csrf_exempt
def process_the_upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        processed_file = create_latex_file()
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="processed_file.tex"'
        response.write(processed_file.getvalue())
        return response
    else:
        return HttpResponseBadRequest('Invalid request')
