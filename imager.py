from PIL import Image, ImageDraw, ImageFont, ImageTk
import PIL.Image
import sys
from tkinter import filedialog
from tkinter import *
import tkinter.font


class App:
    WINDOW_WIDTH = 200
    WINDOW_HEIGHT = 200
    def __init__(self):
        self.root = Tk()
        self.root.title("CodeImager")
        self.canvas = Canvas(self.root, width=self.WINDOW_WIDTH, height=self.WINDOW_HEIGHT)
        self.canvas.pack(fill='both',expand=True)
        
        self.infilename = None
        self.image = None
        self.font_size = 16
        self.font_file = 'font/Inconsolata-Regular.ttf'
        self.font = ImageFont.truetype(self.font_file,self.font_size)
        self.set_color('wb')
        self.margin_width = 20
        self.setup()
        
    def setup(self):
        self.menu = Menu(self.root)

        # File Menu
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Open File",command=self.openfile)
        self.filemenu.add_command(label="Save Image",command=self.saveimage)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.root.quit)
        self.menu.add_cascade(label="File",menu=self.filemenu)

        # Font Menu
        self.fontmenu = Menu(self.menu, tearoff=0)
        self.fontmenu.add_command(label="Inconsolata",command=lambda:self.set_font("Inconsolata-Regular.ttf"))
        self.fontmenu.add_command(label="Anonymous",command=lambda:self.set_font("Anonymous.ttf"))
        self.fontmenu.add_command(label="Droid",command=lambda:self.set_font("DroidSansMono.ttf"))
        self.fontmenu.add_command(label="Ubuntu",command=lambda:self.set_font("UbuntuMono-R.ttf"))
        self.fontmenu.add_command(label="Bitstream",command=lambda:self.set_font("VeraMono.ttf"))
        self.menu.add_cascade(label="Font",menu=self.fontmenu)        

        # Size Menu
        self.sizemenu = Menu(self.menu, tearoff=0)
        self.sizemenu.add_command(label="16",command=lambda:self.set_size(16))
        self.sizemenu.add_command(label="18",command=lambda:self.set_size(18))
        self.sizemenu.add_command(label="20",command=lambda:self.set_size(20))
        self.sizemenu.add_command(label="22",command=lambda:self.set_size(22))
        self.menu.add_cascade(label="Size",menu=self.sizemenu)

        # Color Menu
        self.colormenu = Menu(self.menu, tearoff=0)
        self.colormenu.add_command(label="White on Black",command=lambda:self.set_color('wb'))
        self.colormenu.add_command(label="Black on White",command=lambda:self.set_color('bw'))
        self.menu.add_cascade(label="Colors",menu=self.colormenu)

        self.root.config(menu=self.menu)

    def set_color(self,colors):
        if colors == 'wb':
            self.bgcolor = (0,0,0)
            self.fgcolor = (255,255,255)
        
        elif colors == 'bw':
            self.bgcolor = (255,255,255)
            self.fgcolor = (0,0,0)

        if self.image:
            self.update_image()

    def set_size(self, size):
        self.font_size = size
        self.font = ImageFont.truetype(self.font_file,self.font_size)
        if self.image:
            self.update_image()

    def set_font(self, font):
        self.font_file = "font/" + font
        self.font = ImageFont.truetype(self.font_file ,self.font_size)
        if self.image:
            self.update_image()

    def run(self):
        self.root.mainloop()

    def openfile(self):
        self.infilename =  filedialog.askopenfilename(initialdir = "./",title = "Select file",filetypes = (("Python files","*.py"), ("Java files","*.java"),("Text files","*.txt"),("all files","*.*")))
        self.update_image()

    def update_image(self):
        self.image = self.create_image(self.infilename,font=self.font,bgcolor=self.bgcolor, fgcolor=self.fgcolor)
        render = ImageTk.PhotoImage(self.image)
        
        img = Label(self.root, image=render)
        img.image = render
        img.place(x=0,y=0,anchor='nw')
        self.canvas.config(height=render.height(), width=render.width())


    def saveimage(self):
        out_filename =  filedialog.asksaveasfilename(initialdir = "./",title = "Select file",filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
        self.image.save(out_filename)


    def create_image(self, text_file, out_file=None, font=None, bgcolor=(0,0,0),fgcolor=(255,255,255)):
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
            if font.getsize(line)[0] > widest:
                widest = font.getsize(line)[0]
        
        width = widest + 2*self.margin_width
        height = len(text) * (font.size+2) + 2*self.margin_width

        img = PIL.Image.new("RGB",(width, height),bgcolor)
        draw = ImageDraw.Draw(img)

        draw.text((self.margin_width,0),filename,font=font,fill=(0,0,255))
        for i, line in enumerate(text): # I'm not 100% sure of this spacing
            draw.text((self.margin_width, self.margin_width+i*(font.size+2)),line,font=font,fill=fgcolor)

        return img
        #img.save(out_file)


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
            App.create_image(sys.argv[1], sys.argv[2])
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
            App.create_image(sys.argv[1], sys.argv[2],bgcolor,fgcolor)
            print(f"Image {sys.argv[2]} created.")
        except:
            print("Usage: python imager.py code.py image.png (colorscheme)")

if __name__ == "__main__":
    main()


