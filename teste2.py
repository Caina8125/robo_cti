import aspose.ocr as ocr

api = ocr.AsposeOcr()

# Initialize RecognitionSettings
settings = ocr.RecognitionSettings()
settings.auto_denoising = True
settings.auto_contrast = True

# Specify the PDF document as input
input = ocr.OcrInput(ocr.InputType.PDF)

# Access the scanned PDF and set the page number and total number of pages
input.add("source.pdf", 0, 1)

# Process the PDF file for text recognition with OCR
result = api.recognize(input , settings)

# Save the searchable output PDF file
api.save_multipage_document("searchable.pdf", ocr.SaveFormat.PDF, result)