import boto3

'''

s3_connection = boto3.resource('s3')
						
s3_object = s3_connection.Object(textractproject,'')
s3_response = s3_object.get()

stream = io.BytesIO(s3_response['Body'].read())
image=Image.open(stream)

client = boto3.client('textract')

image_binary = stream.getvalue()
response = client.analyze_document(Document={'Bytes': image_binary},
	FeatureTypes=["TABLES", "FORMS"])

blocks = response['Blocks']
print(blocks)


for block in blocks:
    if 'Text' in block:
        print('    Detected: ' + block['Text'])



for bucket in s3.buckets.all():
	print(bucket.name)

'''


docName = "example1.jpg"

with open(docName, 'rb') as document:
    imageBytes = bytearray(document.read().strip())

textract = boto3.client('textract')

info = textract.detect_document_text(Document={'Bytes': imageBytes})

for words in info["Blocks"]:
    if words["BlockType"] == "LINE":
        print (words["Text"])