# example/views.py
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

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
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        print(f'Received file: {file.name}')
        return JsonResponse({'message': f'Successfully received {file.name}'})