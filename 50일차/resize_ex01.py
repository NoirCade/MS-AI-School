from PIL import Image


def expand2square(pil_img, background_color):
    width, height = pil_img.size
    # print(width, height)
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        # image add (추가 이미지, 붙일 위치(가로, 세로))
        result.paste(pil_img, (0, (width-height//2)))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        # 여기선 높이에서 가로를 뺀다
        result.paste(pil_img, ((height-width)//2, 0))
        return result


img = Image.open('./flower.png')
img_new = expand2square(img, (0, 0, 0)).resize((224, 224))
img_new.save('./resize.png', quality=100)
