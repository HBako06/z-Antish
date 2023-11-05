import boto3

def detect_text_from_image(image):
    #documentName = "captcha.jpg"
    documentName = image

    with open(documentName, 'rb') as document:
        imageBytes = bytearray(document.read())

    region = 'us-east-1' 
    aws_access_key_id = 'AKIAY4UO3BBQSW6YEBI3'
    aws_secret_access_key = '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'

    textract = boto3.client('textract', region_name=region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    response = textract.detect_document_text(Document={'Bytes': imageBytes})

    # Lista para almacenar el texto detectado
    detected_text = []

    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            detected_text.append(item["Text"])

    # Unir las líneas de texto en un solo string usando join
    unified_text = ' '.join(detected_text)

    return unified_text

p =detect_text_from_image('captcha.jpg')
print(p)