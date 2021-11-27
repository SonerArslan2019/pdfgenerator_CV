import pdfkit

"""
out.pdf olarak arslanyapi nin web sitesi pdf e donusturuldu.
https://www.youtube.com/watch?v=m3u3oLgDcJI
https://wkhtmltopdf.org/downloads.html
https://pypi.org/project/pdfkit/
"""
path_wkhtmltopdf = r"/usr/bin/wkhtmltopdf"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_url('https://www.arslanyapi.com.tr/', r'./out.pdf', configuration=config)


