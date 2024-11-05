import os
from datetime import datetime
from PIL import Image, ImageOps


class ImageProcessor:
    def __init__(self, path: str):
        self._path = path

    def process_folder(self, target_size: int):
        """
        Processes all image files in a specified folder and resizes them to the target size.
                Args:
                    target_size: size of the new image
        """
        id_folder = datetime.now().strftime("%Y%m%d%H%M%S")
        output_folder = "datasets/" + id_folder

        try:
            os.mkdir(output_folder)
        except FileExistsError:
            print("Folder already exists")

        for name_file in os.listdir(self._path):
            image_path = os.path.join(self._path, name_file)
            if os.path.isfile(image_path):
                self.processing_image(image_path, output_folder, target_size)

    def processing_image(self, image_path: str, output_path: str, target_size: int):
        """
        Resizes and pads an image to fit the specified target size while maintaining aspect ratio.
        The method resizes the image based on its aspect ratio, adding padding (if necessary) to fit the target size.
        The processed image is saved to the specified output path.
                    Args:
                        image_path (str): The file path of the image to be processed.
                        output_path (str): The target folder where the processed image will be saved.
                        target_size (int): The desired size (width or height) for the resized image.
        """
        image = Image.open(image_path)
        try:
            ratio_image = image.width / image.height

            if ratio_image > 1:
                new_width = target_size
                new_height = int(target_size / ratio_image)
                image_redefine = image.resize((new_width, new_height))
                vertical_padding = target_size - new_height
                color = (114, 114, 114) if image.mode == "RGB" else 114
                image_padding = ImageOps.expand(
                    image_redefine, border=(0, 0, 0, vertical_padding), fill=color
                )
            elif ratio_image < 1:
                new_height = target_size
                new_width = int(target_size * ratio_image)
                image_redefine = image.resize((new_width, new_height))
                horizontal_padding = target_size - new_width
                color = (114, 114, 114) if image.mode == "RGB" else 114
                image_padding = ImageOps.expand(
                    image_redefine, border=(0, 0, horizontal_padding, 0), fill=color
                )
            else:
                image_padding = image.resize((target_size, target_size))

            output_path = os.path.join(output_path, os.path.basename(image_path))
            image_padding.save(output_path)

        finally:
            image.close()
