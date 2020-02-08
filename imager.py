from PIL import Image, ImageDraw, ImageFont, ImageTk
import PIL.Image
import sys
from tkinter import filedialog
from tkinter import *





FONT_SIZE = 16
MARGIN_WIDTH = 20
FONT = ImageFont.truetype('/usr/share/fonts/TTF/Inconsolata-Regular.ttf',FONT_SIZE)

def create_image(text_file, out_file=None, bgcolor=(0,0,0),fgcolor=(255,255,255)):
    '''
    Uses text_file to generate an image file saved as out_file
    '''

    filename = text_file.split("/")[-1]


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

    img = PIL.Image.new("RGB",(width, height),bgcolor)
    draw = ImageDraw.Draw(img)

    draw.text((MARGIN_WIDTH,0),filename,font=FONT,fill=(0,0,255))
    for i, line in enumerate(text): # I'm not 100% sure of this spacing
        draw.text((MARGIN_WIDTH,MARGIN_WIDTH+i*FONT_SIZE+2),line,font=FONT,fill=fgcolor)

    return img
    #img.save(out_file)



class App:
    WINDOW_WIDTH = 200
    WINDOW_HEIGHT = 200
    def __init__(self):
        self.root = Tk()
        self.root.title("CodeImager")
        self.canvas = Canvas(self.root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.canvas.pack(fill='both',expand=True)
        self.setup()
        self.infilename = None
        self.image = None
        
    def setup(self):
        self.menu = Menu(self.root)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Open File",command=self.openfile)
        self.filemenu.add_command(label="Save Image",command=self.saveimage)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.root.quit)
        self.menu.add_cascade(label="File",menu=self.filemenu)
        self.root.config(menu=self.menu)


    def run(self):
        self.root.mainloop()

    def openfile(self):
        self.infilename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Python files","*.py"), ("Java files","*.java"),("Text files","*.txt"),("all files","*.*")))
        self.update_image()

    def update_image(self):
        self.image = create_image(self.infilename)
        render = ImageTk.PhotoImage(self.image)
        
        img = Label(self.root, image=render)
        img.image = render
        img.place(x=0,y=0,anchor='nw')
        self.canvas.config(height=render.height(), width=render.width())


    def saveimage(self):
        out_filename =  filedialog.asksaveasfilename(initialdir = "./",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
        self.image.save(out_filename)


def main():
    if len(sys.argv) < 3:
        app = App()
        app.run()

    
    # if len(sys.argv) < 3:
    #     
    #     print(in_filename)
    #     out_filename =  filedialog.asksaveasfilename(initialdir = "./",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    #     print(out_filename)
    #     create_image(in_filename,out_filename)

    if len(sys.argv) == 3:
        try:
            create_image(sys.argv[1], sys.argv[2])
            print(f"Image {sys.argv[2]} created.")
        except:
            print("Usage: python imager.py code.py image.png (colorscheme)")

    elif len(sys.argv) == 4:
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


