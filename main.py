from src.image.imageProg import ImageProcessor

if __name__ == "__main__":
    PATH_FOLDER = "C:\\Users\\wboya\\Desktop\\TP1\\src\\input_images"
    TARGET_SIZE = 640
    processor = ImageProcessor(PATH_FOLDER)
    processor.process_folder(TARGET_SIZE)
