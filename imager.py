from PIL import Image, ImageDraw, ImageFont
import sys


FONT_SIZE = 16
MARGIN_WIDTH = 20
FONT = ImageFont.truetype('/usr/share/fonts/TTF/Inconsolata-Regular.ttf',FONT_SIZE)

def create_image(text_file, out_file):
    text = []
    with open(text_file) as file:
        for line in file:
            text.append(line)

    
    widest = 0
    for line in text:
        if len(line) > widest:
            widest = len(line)
    
    width = widest * 9
    height = len(text) * FONT_SIZE + 2*MARGIN_WIDTH

    img = Image.new("RGB",(width, height))
    draw = ImageDraw.Draw(img)

    
    for i, line in enumerate(text):
        draw.text((MARGIN_WIDTH,MARGIN_WIDTH+i*FONT_SIZE+2),line,font=FONT,fill=(255,255,255))

    img.save(out_file)





def main():
    create_image('adventure.py','adventure.png')

if __name__ == "__main__":
    main()


