from django.http import HttpResponse

def home(request):
    html = """
    <html>
        <head><title>Django API Project</title></head>
        <body>
            <h2>Welcome to your Django API project!</h2>
            <p>
                Use endpoints like <code>/api/account/</code>, <code>/api/academics/</code>, etc.
            </p>
            <p>
                <a href="/admin/">Go to Django Admin &rarr;</a>
            </p>
        </body>
    </html>
    """
    return HttpResponse(html)
