from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

def convert_images_to_pdf(folder_path, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)

    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    sort_images = sorted(image_files, key=lambda x: int(x.split('_')[0]))
    
    for image_file in sort_images:
        image_path = os.path.join(folder_path, image_file)
    
        # Preload the image
        c.drawImage(image_path, 0, 0, width=8.5*inch, height=11*inch)

        # Add a new page to the PDF
        c.showPage()

    # Save the PDF
    c.save()

# Specify the folder path containing the images and the output PDF file path
folder_path = "images"
output_path = "output.pdf"

# Call the function to convert images to PDF
convert_images_to_pdf(folder_path, output_path)
