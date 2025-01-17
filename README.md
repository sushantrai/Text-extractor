Approach to make this model 
• 1st done little research about library that will suitable for given requirement. Where I found
it [easyocr,fitz] fulfil our requirements.
• then go through the documentations of the libraries.
Design the model for extract text from image (extract_text_from_image) 
• Here we use easyocr to extract text from image and stored the extracted text to text and join 
all the string list into a single string and return it.
• In case of error, it will return Error extracting text from image: errors it got
To extract text from pdf (extract_text_from_pdf)
• For pdf we have to deal with two type of pdf one having selectable text and other having 
scanned image 
• For selectable text i have used fitz to extract text from it. 
• If it doesn't return any text in page_text then we convert pdf into images. after conversion 
stored in PIL.Image then covert it to numpy array and stored in img_np and use 
extract_text_from_image to extract text from image.
• In case of error, it returns Error occurred: error it got
To detect file type and Which method to use (extract_text_auto) 
To determine which file type the given file is. Created a method extract_text_auto which checks for
user provided any file. if not it returns File not found else check the extension of file. If its file type is
.pdf use extract_text_from_pdf and if file type is .jpg, .jpeg, .png, .bmp, .tiff uses 
extract_text_from_image else it returns Unsupported file format
Test of the model
• First test this model on Jupiter notebook and fixed the errors.
Connecting with Frontend-end
• To connect with frontend, I used Flask
Development of Frontend
• I made sure the frontend takes care of matching all the given requirements and is userfriendly.
• Here we implemented Drag and drop and selection of file.
• It accepts only images and pdf file.
• In case of Unsupported file type, it returns Unsupported file type. Please upload a valid file.
• And some other basic errors like user doesn’t upload a file it returns = Please upload a file.
And some other while testing the application.
