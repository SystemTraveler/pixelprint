from PIL import Image
import xml.etree.ElementTree as ET

def rgb_to_grayscale(rgb):
    return 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]

def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

def png_to_xml(png_path, xml_path, threshold=128):
    # Открываем изображение
    img = Image.open(png_path)
    width, height = img.size

    # Создаем корневой элемент XML
    root = ET.Element("image", width=str(width), height=str(height))

    # Определяем цвета для черного и белого
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Проходим по каждому пикселю
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            gray = rgb_to_grayscale(color)
            if gray > threshold:  # Преобразуем к белому
                color_str = 'white'
            else:  # Преобразуем к черному
                color_str = 'black'
            ET.SubElement(root, "pixel", x=str(x), y=str(y), color=color_str)

    # Создаем и сохраняем XML файл
    tree = ET.ElementTree(root)
    with open(xml_path, "wb") as fh:
        tree.write(fh)

# Пример использования
png_to_xml('slipe.png', 'slipe.xml')
