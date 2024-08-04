import requests
import time
import xml.etree.ElementTree as ET

def paint_pixel(x, y, color):
    url = "https://api.pixelbattles.ru/pix"
    headers = {}

    data = {
        "x": x,
        "y": y,
        "color": color
    }

    while True:
        try:
            response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()
            response_text = response.text.strip()

            if response_text == "ok":
                return "ok"
            elif response_text == "skip":
                print(f"Пиксель ({x}, {y}) пропущен.")
                return "skip"
            elif response_text == "await":
                print(f"Необходима задержка для пикселя ({x}, {y}).")
                time.sleep(3.5)
            else:
                print(f"Неожиданный ответ: {response_text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return None

def process_xml(xml_path, start_x=0, start_y=0):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Перебираем все пиксели
    for index, pixel in enumerate(root.findall('pixel')):
        x = int(pixel.get('x')) + start_x
        y = int(pixel.get('y')) + start_y
        color = pixel.get('color')

        # Отправляем запрос
        while True:
            result = paint_pixel(x, y, color)
            if result == "ok":
                print(f"Закрашен пиксель ({x}, {y}) цветом {color}")
                break
            elif result == "skip":
                break
            # Если результат не "ok" и не "skip", повторяем запрос

# Пример использования
process_xml('slipe.xml', start_x=0, start_y=0)
