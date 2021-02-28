import mammoth

input_filename = "file-sample_100kB.docx"

custom_styles = """ b => b.mark
                    u => u.initialism
                    p[style-name='Heading 1'] => h1.card
                    table => table.table.table-hover.striped
                    """


bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">'
bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>'

# Optional: To ignore images by assigning this method to the `convert_image`
def ignore_image(image):
    return []


with open(input_filename, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles, convert_image=ignore_image)
    html = result.value 

edited_html = bootstrap_css + html + bootstrap_js

output_filename = "output.html"
with open(output_filename, "w") as f: 
    f.writelines(edited_html)


### You can also write your own custom CSS styles and use them for style mapping. For details, check out the tutorial.
# custom_css ="""
#     <style>
#     .red{
#         color: red;
#     }
#     .underline{
#         text-decoration: underline;
#     }
#     .ul.li{
#         list-style-type: circle;
#     }
#     table, th, td {
#     border: 1px solid black;
#     }
#     </style>
#     """









