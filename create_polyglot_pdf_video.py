def polyglot(pdf_path, video_path, output_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    with open(video_path, 'rb') as video_file:
        video_data = video_file.read()

    with open(output_path, 'wb') as out_file:
        out_file.write(pdf_data)
        out_file.write(video_data)

    print(f"Polyglot file created: {output_path}")


videopath = input("Enter Video Path: ")
pdfpath = input("Enter Pdf Path: ")
outp = input("output path: ")

polyglot(pdfpath, videopath, outp)