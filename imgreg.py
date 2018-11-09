from PIL import Image
import pytesseract 

def getImage():
    fileName = '1.jpg'
    img = Image.open(fileName)
    print('未转化前的: ', img.mode, img.format)
    return img

def convert_Image(img, standard=127.5):
    image = img.convert('L')

    pixels = image.load()
    for x in range(image.width):
        for y in range(image.height):
            if pixels[x, y] > standard:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return image

def change_Image_to_text(img):
    testdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
    textCode = pytesseract.image_to_string(img, lang='eng', config=testdata_dir_config)
    # todo 去掉非法字符，只保留字母数字
    return textCode

def main():
    img = convert_Image(getImage())
    img.save('2.jpg')
    print('识别的结果：', change_Image_to_text(img))

if __name__ == '__main__':
    main()
