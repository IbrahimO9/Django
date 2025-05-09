from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html><body>
        <h1>Home Page</h1>
        <p>Welcome to the Home Page!</p>
        <a href="/about/">About</a> | 
        <a href="/projects/">Projects</a> | 
        <a href="/contact/">Contact</a>
    </body></html>
    """)

def about(request):
    return HttpResponse("""
    <html><body>
        <h1>About Page</h1>
        <p>This is the About Page.</p>
        <a href="/">Home</a> | 
        <a href="/projects/">Projects</a> | 
        <a href="/contact/">Contact</a>
    </body></html>
    """)

def projects(request):
    return HttpResponse("""
    <html><body>
        <h1>Web Project</h1>
        <p>This is web project created by django.</p>
        <a href="/">Home</a> | 
        <a href="/about/">About</a> | 
        <a href="/contact/">Contact</a>
    </body></html>
    """)

def contact(request):
    return HttpResponse("""
    <html><body>
        <h1>Contact Page</h1>
        <p>Contact us</p>
        <a href="/">Home</a> | 
        <a href="/about/">About</a> | 
        <a href="/projects/">Projects</a>
    </body></html>
    """)
