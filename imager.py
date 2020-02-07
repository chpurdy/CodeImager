from PIL import Image, ImageDraw, ImageFont
import sys


FONT_SIZE = 16
MARGIN_WIDTH = 20
FONT = ImageFont.truetype('/usr/share/fonts/TTF/Inconsolata-Regular.ttf',FONT_SIZE)

def create_image(text_file, out_file, bgcolor=(0,0,0),fgcolor=(255,255,255)):
    '''
    Uses text_file to generate an image file saved as out_file
    '''

    text = []
    with open(text_file) as file:
        for line in file:
            text.append(line)

    
    widest = 0
    for line in text:
        if len(line) > widest:
            widest = len(line)
    
    width = widest * 9 # This shouldn't be hard-coded
    height = len(text) * FONT_SIZE + 2*MARGIN_WIDTH

    img = Image.new("RGB",(width, height),bgcolor)
    draw = ImageDraw.Draw(img)

    
    for i, line in enumerate(text): # I'm not 100% sure of this spacing
        draw.text((MARGIN_WIDTH,MARGIN_WIDTH+i*FONT_SIZE+2),line,font=FONT,fill=fgcolor)

    img.save(out_file)





def main():
    if len(sys.argv) < 3:
        print("Usage: python imager.py code.py image.png (colorscheme)")
        return

    if len(sys.argv) == 3:
        try:
            create_image(sys.argv[1], sys.argv[2])
            print(f"Image {sys.argv[2]} created.")
        except:
            print("Usage: python imager.py code.py image.png (colorscheme)")

    if len(sys.argv) == 4:
        if sys.argv[3] == 'bw':
            fgcolor = (0,0,0)
            bgcolor = (255,255,255)
        else:
            fgcolor = (255,255,255)
            bgcolor = (0,0,0)
        try:
            create_image(sys.argv[1], sys.argv[2],bgcolor,fgcolor)
            print(f"Image {sys.argv[2]} created.")
        except:
            print("Usage: python imager.py code.py image.png (colorscheme)")
if __name__ == "__main__":
    main()


