from django.http import HttpResponse


def portfolio(request):
    html_content = """
    <html>
    <head>
        <title>Welcome Page</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            p {
                color: green;
                font-size: 24px;
                text-align: center;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <p>Hello Dr.Kamaran</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)
