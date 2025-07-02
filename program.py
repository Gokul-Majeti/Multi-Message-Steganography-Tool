from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
import  os

class Stegano:  
    def main(self, root):
        root.title('Multi Message Steganography Tool')
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry(f"{width}x{height}+0+0")  
        bg_image=Image.open("background.jpg")
        bg_photo=ImageTk.PhotoImage(bg_image)
        bg_label=Label(root,image=bg_photo)
        bg_label.image=bg_photo
        bg_label.place(relwidth=1, relheight=1)
        frame = Frame(root,bg='#FFFFFF',bd=0)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)        
        title = Label(frame,text='Multi Message Steganography Tool')
        title.config(font=('Helvetica',35, 'bold'),bg='#FFFFFF')
        title.grid(pady=20)
        encode = Button(frame,text="Encode",command= lambda :self.input(frame), width=10,height=2,bg='#65CCB8' )
        encode.config(font=('Helvetica',16, 'bold'))
        encode.grid(row=2,pady=10)
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), width=10,height=2,bg='#65CCB8')
        decode.config(font=('Helvetica',16, 'bold'))
        decode.grid(pady = 10,row=3)
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def back(self,frame):
        frame.destroy()
        self.main(root)

    def input(self,F):
        F.destroy()
        self.F1=Frame(root,bg='#FFFFFF')
        self.F1.place(relx=0.5, rely=0.5, anchor=CENTER)
        label=Label(self.F1,text='Enter no. of messsages you want to encode:')
        label.config(font=('Helvetica',25,'bold'),bg='#FFFFFF')
        label.grid(row=0,column=0,pady=10)
        self.entry = Entry(self.F1, font=('Helvetica', 15,'bold'),bg='#F0F0F0', bd=2, relief='solid')
        self.entry.grid(row=1, column=0, pady=10)
        submit_button = Button(self.F1, text="Submit",font=('Helvetica', 16, 'bold'), width=10,height=2,bg='#65CCB8',
                       command=lambda: self.store_input())
        submit_button.grid(row=2, column=0, pady=10)
       
    def store_input(self):
        try:
            Stegano.n = int(self.entry.get())
            if Stegano.n<=0:
                raise ValueError()
            self.encode_frame1(self.F1)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            self.entry.delete(0, 'end')

    def encode_frame1(self,F):
        F.destroy()
        F2 = Frame(root,bg='#FFFFFF')
        F2.place(relx=0.5, rely=0.5, anchor=CENTER)
        label1= Label(F2,text='Select the Image to hide messages :')
        label1.config(font=('Helvetica',20, 'bold'),bg = '#FFFFFF')
        label1.grid(row=0,column=0,pady=10)
        self.current_message=1
        button = Button(F2,text='Select',command=lambda : self.encode_frame2(F2), width=10,height=2,bg='#65CCB8')
        button.config(font=('Helvetica',18,'bold'))
        button.grid(row=1,column=0,pady=10)
        button_back = Button(F2, text='Cancel', command=lambda : self.back(F2))
        button_back.config(font=('Helvetica',18,'bold'), width=10,height=2,bg='#65CCB8')
        button_back.grid(row=2,column=0,pady=10)

    def decode_frame1(self,F):
        F.destroy()
        F2 = Frame(root,bg='#FFFFFF')
        F2.place(relx=0.5, rely=0.5, anchor=CENTER)
        label1 = Label(F2, text='Select Image with Hidden text:')
        label1.config(font=('Helvetica',25,'bold'),bg = '#FFFFFF')
        label1.grid(pady=10)
        label1.config(bg = '#FFFFFF')
        button = Button(F2, text='Select', command=lambda :self.decode_frame2(F2))
        button.config(font=('Helvetica',18,'bold'), width=10,height=2,bg='#65CCB8')
        button.grid(pady=10)
        button_back = Button(F2, text='Cancel', command=lambda : Stegano.back(self,F2))
        button_back.config(font=('Helvetica',18,'bold'), width=10,height=2,bg='#65CCB8')
        button_back.grid(pady=10)     

    def encode_frame2(self, F2):
        self.F3 = Frame(root, bg='#FFFFFF')
        self.F3.place(relx=0.5, rely=0.5, anchor=CENTER)
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png')])
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
            return
        else:
            try:
                self.myimg = Image.open(myfile)
            except Exception as e:
                messagebox.showerror("Error","Select a png image")
                return
            new_image = self.myimg.resize((325, 225))
            self.img = ImageTk.PhotoImage(new_image)            
            label3 = Label(self.F3, text='Selected Image', font=('Helvetica', 20, 'bold'), bg='#FFFFFF')
            label3.grid(row=0, column=0, pady=10)
            board = Label(self.F3, image=self.img,bg='#F0F0F0', bd=2, relief='solid')
            board.image = self.img
            board.grid(row=1, column=0, pady=15)
            self.text_boxes=[]
            self.add_message_entry()
        F2.destroy()

    def add_message_entry(self):
        for widget in self.F3.grid_slaves():
            if widget.grid_info()["row"] >= 2: 
                widget.grid_forget()
        label2 = Label(self.F3, text=f'Enter message {self.current_message}:', font=('Helvetica', 14, 'bold'), bg='#65CCB8',height=3)
        label2.grid( pady=15)
        self.text = Text(self.F3, width=50, height=3,bg='#F0F0F0', bd=2, relief='solid',font='bold')
        self.text.grid(pady=15)
        encode_button = Button(self.F3, text='Encode', command=lambda: self.save_and_next_message(), font=('Helvetica', 14, 'bold'), bg='#65CCB8')
        encode_button.config(width=10,height=2)
        encode_button.grid( pady=15)
        if(Stegano.n==self.current_message):
            button_back = Button(self.F3, text='Cancel', command=lambda: self.back(self.F3), font=('Helvetica', 14, 'bold'), bg='#65CCB8')
            button_back.config(width=10,height=2)
            button_back.grid( pady=10)
        if self.current_message < Stegano.n:
            skip_button = Button(self.F3, text='Skip', command=self.skip, font=('Helvetica', 14, 'bold'), bg='#65CCB8')
            skip_button.config(width=10,height=2)
            skip_button.grid( pady=15)

    def save_and_next_message(self):
        message = self.text.get("1.0", END).strip()
        if not message:
            messagebox.showwarning("Warning", f"Please enter message {self.current_message}")
            return
        self.text_boxes.append(message)
        if self.current_message == Stegano.n:
            self.encode_multiple(self.text_boxes, self.myimg, self.F3)
        else:
            self.current_message += 1
            self.add_message_entry()

    def skip(self):
        self.text_boxes.append("")
        self.current_message += 1
        self.add_message_entry()

    def decode_frame2(self, F2):
        F3 = Frame(root, bg='#FFFFFF')    
        myfile = tkinter.filedialog.askopenfilename(filetypes=[('png', '*.png') ])        
        if not myfile:
            messagebox.showerror("Error", "You have selected nothing!")
        else:            
            try:
                myimg = Image.open(myfile)
            except Exception as e:
                messagebox.showerror("Error", "Select a png image")
                return 
            new_image = myimg.resize((375, 275))
            img = ImageTk.PhotoImage(new_image)
            label4 = Label(F3, text='Selected Image:')
            label4.config(font=('Helvetica', 14, 'bold'), bg='#FFFFFF')
            label4.grid(row=0, column=0, pady=5)
            board = Label(F3, image=img,bg='#F0F0F0', bd=2, relief='solid')
            board.image = img
            board.grid(row=1, column=0, pady=20)
            decoded_messages = self.decode(myimg)
            listbox = Listbox(F3, bg='#FFFFFF', font=('Helvetica', 12,'bold'), width=70, height=len(decoded_messages),bd=3,relief='groove',borderwidth=3)
            listbox.grid(row=2, column=0, pady=20) 
            for i, message in enumerate(decoded_messages):
                listbox.insert(END, f'Decoded Message {i + 1}: {message}')
            button_back = Button(F3, text='Cancel', command=lambda: self.back(F3))
            button_back.config(font=('Helvetica', 16, 'bold'), width=10, height=2, bg='#65CCB8')
            button_back.grid(row=3, column=0, pady=20) 
            F3.grid()
            F2.destroy() 
            
    def decode(self, image):
        image_data = iter(image.getdata())
        data = []
        binary_str = ''
        markerseq='@%'
        while True:
            pixels = [value for value in next(image_data)[:3] +
                    next(image_data)[:3] +
                    next(image_data)[:3]]
            for i in pixels[:8]:
                binary_str += '0' if i % 2 == 0 else '1'
            char = chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0: 
                if char:
                    data.append(char)  
                break
            data.append(char)
            binary_str = ''  
        decoded_data = ''.join(data).strip()
        decoded_data = [msg for msg in decoded_data.split('#$') if msg]
        decoded_data[0]=decoded_data[0][2:]
        return decoded_data
    
    def generate_Data(self,data):
        newdata = []
        for i in data:
            newdata.append(format(ord(i), '08b'))
        return newdata
    
    def modifyPixels(self,pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                        pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
    
    def encode(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)
        for pixel in self.modifyPixels(newImg.getdata(), data):
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1
        return newImg
    
    def encode_multiple(self, text_boxes, myImg, F3):
        all_data = '@%'
        for text in text_boxes:
            data = text  
            if data:  
                all_data += data + '#$'
        if not all_data.strip():
            messagebox.showinfo("Alert", "Kindly enter text in at least one TextBox")
        else:
            newImg = myImg.copy()
            newImg=self.encode(newImg, all_data)
            self.showimages(myImg,newImg,F3)            

    def showimages(self, myImg, newImg, F):
        Fs = Frame(root, bg='#FFFFFF')
        Fs.place(relx=0.5, rely=0.5, anchor=CENTER) 
        original = myImg.resize((500, 500))
        original_tk = ImageTk.PhotoImage(original)
        label1 = Label(Fs, text='Original Image')
        label1.config(font=('Helvetica', 15, 'bold'), bg='#FFFFFF')
        label1.grid(row=0, column=0, padx=15, pady=15)
        board1 = Label(Fs, image=original_tk,bg='#F0F0F0', bd=2, relief='solid')
        board1.image = original_tk
        board1.grid(row=1, column=0, padx=0, pady=15)
        encoded = newImg.resize((500, 500))
        encoded_tk = ImageTk.PhotoImage(encoded)
        label2 = Label(Fs, text='Encoded Image')
        label2.config(font=('Helvetica', 15, 'bold'), bg='#FFFFFF')
        label2.grid(row=0, column=1, padx=15, pady=15)
        board2 = Label(Fs, image=encoded_tk,bg='#F0F0F0', bd=2, relief='solid')
        board2.image = encoded_tk
        board2.grid(row=1, column=1, padx=15, pady=15)
        F.destroy()
        save_button = Button(Fs, text="Save Encoded Image", command=lambda: self.save_encoded_image(newImg, myImg,Fs))
        save_button.config(font=('Helvetica', 14, 'bold'), bg='#65CCB8')
        save_button.grid(row=2, columnspan=2, pady=10)
        button_back = Button(Fs, text="Back", command=lambda: self.back(Fs))
        button_back.config(font=('Helvetica', 14, 'bold'), bg='#65CCB8')
        button_back.grid(row=3, columnspan=2, pady=10)
        Fs.grid() 

    def save_encoded_image(self, newImg, myImg,Fs):
        temp = os.path.splitext(os.path.basename(myImg.filename))[0]
        newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp, filetypes=[('png', '*.png') ], defaultextension=".png"))
        messagebox.showinfo("Success", "Encoding Successful")
        self.back(Fs)

root = Tk()
o = Stegano()
o.main(root)
root.mainloop()