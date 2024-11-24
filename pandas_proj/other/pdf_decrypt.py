from PyPDF2 import PdfFileReader,PdfFileWriter


# 使用示例
input_file = 'C:/Users/fernando/Desktop/anew/xs.pdf'
output_file = 'C:/Users/fernando/Desktop/anew/xsss.pdf'
password = '450345'  # 替换为实际的密码


from pypdf import PdfReader, PdfWriter

reader = PdfReader(input_file)

if reader.is_encrypted:
    reader.decrypt(password)

writer = PdfWriter(clone_from=reader)

# Save the new PDF to a file
with open(output_file, "wb") as f:
    writer.write(f)


