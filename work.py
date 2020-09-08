import cv2
import tkinter.filedialog as file
import tkinter

# Point object defined (Attributes x and y)
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# Returns monitor resolution
def monitorRes():
    root = tkinter.Tk()
    root.withdraw()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return width, height

# Asks user to browse for the image they want to open
def askfile():
    file_path = file.askopenfilename()
    img = cv2.imread(file_path)
    return img

# Displays the image selected by the user
def displayimg(img):
    cv2.imshow("File", img)
    cv2.waitKey(0)

# Prints the image height and width
def imgpropprint(img):
    h , w = img.shape[:2]
    print("Image height: " + str(h))
    print("Image width: " + str(w))

# Returns height and width
def imgprop(img):
    h , w = img.shape[:2]
    return w, h

# Starting main code
image = askfile()
imgpropprint(image)
displayimg(image)
