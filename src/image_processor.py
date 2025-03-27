from PIL import Image
import cv2

# Загрузка изображения
image = cv2.imread("sample.png")
if image is None:
    print("Ошибка: изображение не найдено!")
else:
    # Конвертация в RGB (для PIL)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)

    # Изменение размера
    resized_image = pil_image.resize((200, 200))
    resized_image.save("output.jpg")
    print("Изображение обработано и сохранено как output.jpg")