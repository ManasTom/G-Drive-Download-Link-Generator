#Author : MANAS TOM
# MY PROFILE : https://github.com/ManasTom

#import all essentials
from tkinter import*

#define all essentials
root = Tk()
root.title('MANAS TOM')
root.geometry('700x700')

#define the function
def generateDlink(event):
    vLink = viewLinkTextbox.get()
    vLink = vLink.split("/")
    print(vLink[5])
    D_Pre_Link = "https://drive.google.com/uc?id="
    D_Post_Link = "&export=download"
    D_Link = (D_Pre_Link + vLink[5] + D_Post_Link)
    plink = StringVar()
    plink.set(D_Link)
    DlinkLabel = Entry(root,width = 100,state = "readonly",textvariable=plink)
    DlinkLabel.pack()
    viewLinkTextbox.delete(0, END)

#bind the enter key to the function
root.bind('<Return>',generateDlink)

#add the required labels
TopLabel=Label(root,text="Enter your google drive view links here and hit ENTER key orGENERATE buttton to generate its download link")
TopLabel.pack()
TopLabel=Label(root,text="The links you paste here should be Unrestricted Viewer links")
TopLabel.pack()

# the link entry box
viewLinkTextbox = Entry(root,width = 80 , font=('Arial 10'))
viewLinkTextbox.pack()

#the generate button
GenerateButton = Button(root, text = 'Generate',width = 15, command = generateDlink)
GenerateButton.pack()

#loop all the things
root.mainloop()

#Author : MANAS TOM
# MY PROFILE : https://github.com/ManasTom
