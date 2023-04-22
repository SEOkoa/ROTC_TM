import pandas as pd
from PIL import Image
import io

# read the Excel file into a pandas DataFrame
df = pd.read_excel('Members/62기 명단.xlsx')

# convert the DataFrame to an HTML table
html_table = pd.DataFrame(df).to_html()

# create an image from the HTML table
img = Image.open(io.BytesIO(html_table.encode()))

# save the image to a file
img.save('example.png')
