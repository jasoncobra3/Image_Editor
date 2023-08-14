from PIL import Image

im=Image.open("abc.jpg")

def rotate():
    print("\n Select operation \n 1.Anticlockwise \n 2.Clockwise \n 3.Vertical \n 4.Horizontal \n 5.Rotate 90 \n 6.Rotate 180 \n 7.Rotate 270 ")
    ch=int(input("Enter your choice:"))
    if ch==1:
        anticlock = im.transpose(Image.TRANSPOSE)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            anticlock.save("anticlock.png")
        else:
            print("Thank you for using my editor!")
        anticlock.show()
    elif ch==2:
        clock=im.transpose(Image.TRANSVERSE)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            clock.save("clock.png")
        else:
            print("Thank you for using my editor!")
        clock.show()
    elif ch==3:
        ver=im.transpose(Image.FLIP_LEFT_RIGHT)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            ver.save("vertical.png")
        else:
            print("Thank you for using my editor!")
        ver.show()
    elif ch==4:
        hor=im.transpose(Image.FLIP_TOP_BOTTOM)
        a=int(input("Would you like to save image or not (press 1 to save) :"))
        if a==1:
            hor.save("horizontal.png")
        else:
            print("Thank you for using my editor!")
        hor.show()
    elif ch==5:
        nine=im.transpose(Image.ROTATE_90)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            nine.save("90_rotate.png")
        else:
            print("Thank you for using my editor!")
        nine.show()
    elif ch==6:
        eighty=im.transpose(Image.ROTATE_180)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            eighty.save("180_rotate.png")
        else:
            print("Thank you for using my editor!")
        eighty.show()
    elif ch==7:
        seventy=im.transpose(Image.ROTATE_270)
        a = int(input("Would you like to save image or not (press 1 to save) :"))
        if a == 1:
            seventy.save("270_rotate.png")
        else:
            print("Thank you for using my editor!")
        seventy.show()


def type():
    print(f"The type and size  of file is {im.format} X {im.size}")

def resize():
    h=int(input("Enter the height to resize image:"))
    w=int(input("Enter the width to resize image:"))
    size=(h,w)
    im.thumbnail(size)
    im.save("new_img.jpeg")
    print(f"The format and size of new file is {im.format} X {im.size}")
    im.show()

def change_type():
    print("Select the file format to change the file type of image!")
    print("\n 1.png \n 2.JPEG \n 3.BMP \n 4.GIF")
    b=int(input("Enter your choice:"))
    if b==1:
        out="PNG"
    elif b==2:
        out="JPEG"
    elif b==3:
        out="BMP"
    elif b==4:
        out="GIF"
    im.save('outp.png', format=out)
    im.show()

while(True):
    print("################# IMAGE EDITOR ################")
    print("WELCOME TO MY IMAGE EDITOR")
    print("\n 1.Rotate image \n 2.Print Type and size of file \n 3.Resize file \n 4.Change File Format \n 5.Exit")
    n=int(input("Enter your operation to perform on image:"))
    if n==1:
        rotate()
    elif n==2:
        type()
    elif n==3:
        resize()
    elif n==4:
        change_type()
    elif n==5:
        print("Thank you ! Visit again , Hope you enjoy it. ")
        break


