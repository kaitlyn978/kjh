from tkinter import *
root=Tk();
root.title("fibonacci")
root.geometry("444x444")
text=Entry(root)
label_series=Label(root, text="Fibonacci Series: ")
label_flower=Label(root)
label_spiral=Label(root)

def Fibonacci():
    num=10
    f_n=0
    s_n=1
    sum=0
    sum2=0
    counter=1
    while(counter<=num):
        label_series["text"]+=str(sum)+ " "
        counter=counter+1
        f_n=s_n
        s_n=sum
        sum=f_n+s_n
        sum2=sum2+sum
    label_flower["text"]="Flower is Fully Bloomed"
    label_spiral["text"]="Spirals in right direction are"+str(f_n)+"Spiral in left direction are"+str(s_n)+"\n Total spirals are"+str(sum)
btn=Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()   

