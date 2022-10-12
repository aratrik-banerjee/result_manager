from tkinter import *
import math
import os
root=Tk()
root.title('Result Manager')
root.attributes('-fullscreen', True)
root.config(padx=400,pady=10,bg='#4863A0')
photo = PhotoImage(file = "images/bitlogo.png")
root.iconphoto(False, photo)

img=PhotoImage(file='images/Welcome.png')
Wlcm=Label(root,image=img,bg='#4863A0')
Wlcm.grid(row=0,column=0)
l=Label(root,bg='#4863A0',pady=25).grid(row=1,column=0)
img1=PhotoImage(file='images/back.png')
img2=PhotoImage(file='images/home.png')


#subjects
sub1to5=['English','Hindi/Bengali','Maths','Science','S.st','Gk']
sub6to10=['English','Hindi/Bengali','Maths','Science','S.st','Computer Science']
subsci1=['English','Physics','Chemistry','Maths','Biology']
subsci2=['English','Physics','Chemistry','Maths','Computer']
subsci3=['English','Physics','Chemistry','Biology','Hindi/Beng']
subsci4=['English','Physics','Chemistry','Biology','Physical Education']
subcom1=['English','B.St','Eco.','Accountancy','Physical Education']
subcom2=['English','B.St','Eco.','Accountancy','Computer Application']
subcom3=['English','B.St','Eco.','Accountancy','Hindi/Beng']
subart1=['English','Geography','History','Economics','Physical Education']
subart2=['English','Geography','History','Economics','Hindi/Beng']
subart3=['English','Geography','History','Hindi/Beng','Physical Education']

#blank
subject=[]

pa1f=[]
def fresult():    
    global pa1,pa1f,pa2,pa2f,hylt,hylp,hylf,ft,fp,ftf,subject,grd,point,cgpa,prctg,roll,cls,section
    rslt=open('files/Class_'+str(cls)+'_'+str(section)+'.txt','r')
    rslt.seek(0)
    x=rslt.read()
    pos=x.index("Roll No: "+str(roll))
    y=(x[pos::])
    temp=open('files/temp.txt','w+')
    temp.write(y)
    temp.seek(0)
    z=temp.readlines()[1].replace(r'\n','').split(';')
    pa1=eval(z[0])
    pa2=eval(z[1])
    pa1f=eval(z[2])
    pa2f=eval(z[3])
    hylt=eval(z[4])
    hylp=eval(z[5])
    ft=eval(z[6])
    fp=eval(z[7])
    name=z[8]
    ftf=eval(z[9])
    subject=eval(z[10])
    mrks()

    result=Toplevel(root)
    result.attributes('-fullscreen', True)
    result.config(bg='#4863A0')
    img=PhotoImage(file='images/rslt.png')
    rsl=Label(result,image=img,bg='#4863A0')
    rsl.photo=img
    rsl.grid(row=0,column=0,columnspan=8)
   
    nm=Label(result,text='Name: '+str(name),font=('Ariel Black',18),padx=200,pady=5,bg='#4863A0',fg="white")
    nm.grid(row=1,column=0,columnspan=8)
    c=Label(result,text='Class: '+str(cls)+'-'+str(section),padx=200,font=('Ariel Black',18),pady=5,bg='#4863A0',fg="white")
    c.grid(row=2,column=0,columnspan=8)
    r=Label(result,text='Roll No: '+str(roll),font=('Ariel Black',18),padx=150,pady=10,bg='#4863A0',fg="white")
    r.grid(row=3,column=0,columnspan=8)
    sub=Label(result,text='Subject',font=('Ariel Black',18),padx=100,pady=18,bg='#4863A0',fg="white")
    sub.grid(row=4,column=0)
    p1=Label(result,text='PA I',font=('Ariel Black',18),padx=60,bg='#4863A0',fg="white")
    p1.grid(row=4,column=1)
    h=Label(result,text='Half Yearly',font=('Ariel Black',18),padx=60,bg='#4863A0',fg="white")
    h.grid(row=4,column=2,columnspan=2)
    p2=Label(result,text='PA II',font=('Ariel Black',18),padx=40,bg='#4863A0',fg="white")
    p2.grid(row=4,column=4)
    a=Label(result,text='Annual',font=('Ariel Black',18),padx=60,bg='#4863A0',fg="white")
    a.grid(row=4,column=5,columnspan=2)
    g=Label(result,text='Grade',font=('Ariel Black',18),padx=60,bg='#4863A0',fg="white")
    g.grid(row=4,column=7)
    t=Label(result,text='Theory',font=('Ariel Black',18),padx=30,bg='#4863A0',fg="white")
    t.grid(row=5,column=2)
    p=Label(result,text='Practical',font=('Ariel Black',18),padx=30,bg='#4863A0',fg="white")
    p.grid(row=5,column=3)
    t=Label(result,text='Theory',font=('Ariel Black',18),padx=30,bg='#4863A0',fg="white")
    t.grid(row=5,column=5)
    p=Label(result,text='Practical',font=('Ariel Black',18),padx=30,bg='#4863A0',fg="white")
    p.grid(row=5,column=6)
    r=6
    c=0
    for i in range(len(subject)):        
        l=Label(result,text=str(subject[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=1
    for i in range(len(subject)):        
        l=Label(result,text=str(pa1[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=2
    for i in range(len(subject)):        
        l=Label(result,text=str(hylt[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=3
    for i in range(len(subject)):        
        l=Label(result,text=str(hylp[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=4
    for i in range(len(subject)):        
        l=Label(result,text=str(pa2[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=5
    for i in range(len(subject)):        
        l=Label(result,text=str(ft[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=6
    for i in range(len(subject)):        
        l=Label(result,text=str(fp[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1
    r=6
    c=7
    for i in range(len(subject)):        
        l=Label(result,text=str(grd[i]),pady=5,bg='#4863A0',fg="white",font=('Ariel Black',16)).grid(row=r,column=c)
        r+=1

    c=Label(result,text='CGPA: '+str(cgpa),font=('Ariel Black',15),bg='#4863A0',fg="white",pady=5,padx=20)
    c.grid(row=22,column=0,sticky='w')

    p=Label(result,text='Percentage: '+str(prctg)+' %',font=('Ariel Black',15),bg='#4863A0',fg="white",pady=5,padx=20)
    p.grid(row=23,column=0,sticky='w')

    sts=''
    if prctg<=33.0:
        sts='FAILED'
    else:
        sts='PASSED'

    s=Label(result,text='Status: '+sts,font=('Ariel Black',15),bg='#4863A0',fg="white",pady=5,padx=20)
    s.grid(row=24,column=0,sticky='w')

    def qit():
        result.destroy()
    b1=Button(result,text='OK',cursor='hand2',command=qit,width=30,bg='#98AFC7').grid(row=25,column=0,columnspan=8)

def detail():               #taking details
    name_var=StringVar()
    cls_var=IntVar()
    roll_var=IntVar()
    section_var=StringVar()
    cls_var.set("")
    roll_var.set("")
    name_var.set("")
    section_var.set("")
    
    
    def subject():              #taking subject
        global name,cls,roll,section,subject
        name=name_var.get()
        cls=cls_var.get()
        roll=roll_var.get()
        section=section_var.get()
        

        def sci():          #for science stream  
            var=IntVar()
            sci=Toplevel(root)
            sci.config(pady=10,bg='#4863A0')
            sci.attributes('-fullscreen', True)
            def qt():
                sci.destroy()
                
            
            button_1=Button(sci,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=0,sticky='W',padx=50)
            def qt():
                sci.destroy()
                detail.destroy()
                stream.destroy()
            spc=Label(sci,padx=70,bg='#4863A0').grid(row=0,column=3)
            button_1=Button(sci,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=4,sticky='E')
            img=PhotoImage(file='images/subsci.png')
            sub=Label(sci,image=img)
            sub.photo=img
            sub.grid(row=0,column=1)

            
            s1=''
            s2=''
            s3=''
            s4=''
            for i in range(5):
                s1+=subsci1[i]+", "
                s2+=subsci2[i]+", "
                s3+=subsci3[i]+", "
                s4+=subsci4[i]+", "
            def sub():
                global subject
                if var.get()==1:
                    subject=subsci1
                elif  var.get()==2:
                    subject=subsci2
                elif  var.get()==3:
                    subject=subsci3
                elif  var.get()==3:
                    subject=subsci3
                elif  var.get()==4:
                    subject=subsci4
                sci.destroy()
                detail.destroy()
                stream.destroy()
                form()
                

                
            sc1=Radiobutton(sci,text=s1,pady=10,variable=var,cursor='hand2',value=1,bg='#4863A0',font=('Freestyle Script',40), command=sub,fg='white')
            sc1.grid(row=3,column=1,sticky='W')
            sc2=Radiobutton(sci,text=s2,pady=10,variable=var,cursor='hand2',value=2,bg='#4863A0',font=('Freestyle Script',40), command=sub,fg='white')
            sc2.grid(row=4,column=1,sticky='W')
            sc3=Radiobutton(sci,text=s3,pady=10,variable=var,cursor='hand2',value=3, command=sub,font=('Freestyle Script',40),bg='#4863A0',fg='white')
            sc3.grid(row=5,column=1,sticky='W')
            sc4=Radiobutton(sci,text=s4,pady=10,variable=var,cursor='hand2',value=4, command=sub,font=('Freestyle Script',40),bg='#4863A0',fg='white')
            sc4.grid(row=6,column=1,sticky='W')
            
            
            
            
        def cmrs():             #for commerce stream
            var=IntVar()
            com=Toplevel(root)
            com.config(pady=10,bg='#4863A0')
            com.attributes('-fullscreen', True)
            def qt():
                com.destroy()
                
            
            button_1=Button(com,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=0,sticky='W',padx=50)
            def qt():
                com.destroy()
                detail.destroy()
                stream.destroy()
            spc=Label(com,bg='#4863A0').grid(row=0,column=3)
            button_1=Button(com,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=4,sticky='E')
            img=PhotoImage(file='images/subcom.png')
            sub=Label(com,image=img)
            sub.photo=img
            sub.grid(row=0,column=1)
            s1=''
            s2=''
            s3=''
            
            for i in range(5):
                s1+=subcom1[i]+", "
                s2+=subcom2[i]+", "
                s3+=subcom3[i]+", "
                
            def sub():
                global subject
                if var.get()==1:
                    subject=subcom1
                elif  var.get()==2:
                    subject=subcom2
                elif  var.get()==3:
                    subject=subcom3
                elif  var.get()==3:
                    subject=subcom3
                com.destroy()
                detail.destroy()
                stream.destroy()
                form()
                

                
            cm1=Radiobutton(com,text=s1,pady=10,variable=var,cursor='hand2',value=1,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            cm1.grid(row=3,column=1,sticky='W')
            cm2=Radiobutton(com,text=s2,pady=10,variable=var,cursor='hand2',value=2,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            cm2.grid(row=4,column=1,sticky='W')
            cm3=Radiobutton(com,text=s3,pady=10,variable=var,cursor='hand2',value=3,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            cm3.grid(row=5,column=1,sticky='W')
            
        def arts():        #for arts stream
            var=IntVar()
            art=Toplevel(root)
            art.config(pady=10,bg='#4863A0')
            art.attributes('-fullscreen', True)
            def qt():
                art.destroy()
                
            
            button_1=Button(art,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=0,sticky='W',padx=50)
            def qt():
                art.destroy()
                detail.destroy()
                stream.destroy()
            spc=Label(art,bg='#4863A0').grid(row=0,column=3)
            button_1=Button(art,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=4,sticky='E')
            img=PhotoImage(file='images/subart.png')
            sub=Label(art,image=img)
            sub.photo=img
            sub.grid(row=0,column=1)
            s1=''
            s2=''
            s3=''
            
            for i in range(5):
                s1+=subart1[i]+", "
                s2+=subart2[i]+", "
                s3+=subart3[i]+", "
                
            def sub():
                global subject
                if var.get()==1:
                    subject=subart1
                elif  var.get()==2:
                    subject=subart2
                elif  var.get()==3:
                    subject=subart3
                elif  var.get()==3:
                    subject=subart3
                art.destroy()
                detail.destroy()
                stream.destroy()
                form()
                

                
            ar1=Radiobutton(art,text=s1,pady=10,variable=var,cursor='hand2',value=1,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            ar1.grid(row=3,column=1,sticky='W')
            ar2=Radiobutton(art,text=s2,pady=10,variable=var,cursor='hand2',value=2,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            ar2.grid(row=4,column=1,sticky='W')
            ar3=Radiobutton(art,text=s3,pady=10,variable=var,cursor='hand2',value=3,bg='#4863A0', command=sub,font=('Freestyle Script',40),fg='white')
            ar3.grid(row=5,column=1,sticky='W')

        
        if (cls>10) and (cls<13) :
            x=open('files/Available.txt','a+')
            x.close
            avl=open('files/Available.txt','r')
            x=avl.read()
            if 'files/Class_'+str(cls)+'_'+section+"Roll No: "+str(roll) in x:
                err=Toplevel(root)
                err.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(err)} center')
                msg=('Result of Roll No: '+str(roll)+(' already exists\nUse "View Results" to see existing result.\nUse "Delete Result" to delete existing result before re-issuing Result.'))
                l1=Label(err,text=msg,justify='left',padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.pack()
                def qt():
                    err.destroy()
                ext=Button(err,text='OK',padx=10,pady=5,command=qt,cursor='hand2',bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.pack()

            else:
                stream=Toplevel(root)
                stream.attributes('-fullscreen', True)
                stream.config(pady=10,bg='#4863A0')
                img=PhotoImage(file='images/stream.png')
                strm=Label(stream,image=img)
                stream.photo=img
                strm.grid(row=1,column=1)
                gp=Label(stream,bg='#4863A0',pady=20,padx=200).grid(row=1,column=0)

                def qt():
                    stream.destroy()
                gp=Label(stream,bg='#4863A0',pady=20,padx=200).grid(row=2,column=0)
                button_1=Button(stream,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
                button_1.grid(row=1,column=0,sticky='W',padx=50)
                com=Button(stream,text="SCIENCE",cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40, command=sci)
                com.grid(row=3,column=1)
                l=Label(stream,bg='#4863A0',pady=15).grid(row=4,column=0)
                cmrs=Button(stream,text="COMMERCE",cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40, command=cmrs)
                cmrs.grid(row=5,column=1)
                l=Label(stream,bg='#4863A0',pady=15).grid(row=6,column=0)
                art=Button(stream,text="ARTS",cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40, command=arts)
                art.grid(row=7,column=1)    

        elif (cls<11) and (cls>5):
            subject=sub6to10
            detail.destroy()
            form()
            
            
        elif (cls<6) and (cls>0):
            subject=sub1to5
            detail.destroy()
            form()

        

        
        
    detail=Toplevel(root)
    detail.attributes('-fullscreen', True)
    detail.config(pady=10,bg='#4863A0')
    imge=PhotoImage(file='images/student.png')
    Info=Label(detail,image=imge,pady=10)
    Info.photo = imge
    Info.grid(row=4,column=1,columnspan=2)

    gp=Label(detail,bg='#4863A0',pady=20,padx=200).grid(row=5,column=0)

    def qt():
        detail.destroy()

    button_1=Button(detail,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
    button_1.grid(row=4,column=0,sticky='W',padx=50)
    
    Name=Label(detail,text='Name',bg='#4863A0',font=('Freestyle Script',45),fg='white').grid(row=6,column=1)
    e1=Entry(detail,textvariable = name_var,font=(15),bg='#98AFC7',bd=5).grid(row=6,column=2,ipady=5)
    
    
    Class=Label(detail,text='Class',bg='#4863A0',font=('Freestyle Script',45),fg='white').grid(row=7,column=1)
    e2=Entry(detail,textvariable = cls_var,font=(15),bg='#98AFC7',bd=5).grid(row=7,column=2,ipady=5)
    
    Roll_No=Label(detail,text='Roll No.',bg='#4863A0',font=('Freestyle Script',45),fg='white').grid(row=8,column=1)
    e3=Entry(detail,textvariable = roll_var,font=(15),bg='#98AFC7',bd=5).grid(row=8,column=2,ipady=5)

    Section=Label(detail,text='Section',bg='#4863A0',font=('Freestyle Script',45),fg='white').grid(row=9,column=1)
    e4=Entry(detail,textvariable = section_var,font=(15),bg='#98AFC7',bd=5).grid(row=9,column=2,ipady=5)

    gp=Label(detail,bg='#4863A0',pady=20).grid(row=10,column=0)

    button_4=Button(detail,text='Submit',cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40, command=subject)
    button_4.grid(row=11,column=1,columnspan=2)
    

    


def delete():
    opt=Toplevel(root,padx=30,pady=30)
    opt.attributes('-fullscreen', True)
    opt.config(pady=10,bg='#4863A0')

    def cls():
        global cls,roll,section
        clas=Toplevel(root)
        clas.attributes('-fullscreen', True)
        clas.config(pady=10,bg='#4863A0')
        imge=PhotoImage(file='images/student.png')
        gp=Label(clas,bg='#4863A0',pady=20,padx=200).grid(row=1,column=0)

        def qt():
            clas.destroy()

        button_1=Button(clas,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=0,sticky='W',padx=50)
        Info=Label(clas,image=imge,pady=10)
        Info.photo = imge
        Info.grid(row=0,column=1,columnspan=2)
        cls_var=IntVar()
        sctn_var=StringVar()
        cls_var.set("")
        sctn_var.set("")
        gp=Label(clas,bg='#4863A0',pady=20).grid(row=1,column=0)
        def qt():
            opt.destroy()
            clas.destroy()
            
        gp=Label(clas,bg='#4863A0',pady=20,padx=150).grid(row=1,column=4)            
        button_1=Button(clas,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=4,sticky='E')
        msg=('Enter the class : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=2,column=1)

        msg=('Enter the Section : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=3,column=1)

        def sbmt():
            global cls,section
            cls=cls_var.get()
            section=sctn_var.get()
            opt.destroy()
            clas.destroy()
            deletion()
        e1=Entry(clas,textvariable=cls_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=2,column=2)
        e2=Entry(clas,textvariable=sctn_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=3,column=2)
        gp=Label(clas,bg='#4863A0',pady=20).grid(row=4,column=0)
        s=Button(clas,text='S U B M I T',cursor='hand2',bg='#98AFC7',bd=10,font=('Times New Roman',15),width=40,command=sbmt)
        s.grid(row=5,column=1,columnspan=2)

        def deletion():
            global cls,section
            
            avl=open("files/Available.txt",'a+')
            avl.seek(0)
            x=avl.read()
            
            if ('files/Class_'+str(cls)+'_'+str(section)) not in x:
                err=Toplevel(root)
                err.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(err)} center')                 
                msg=('No result of Class '+str(cls)+"-"+str(section)+' found')
                l1=Label(err,text=msg,padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.pack()
                def qt():
                    err.destroy()
                ext=Button(err,text='OK',padx=10,cursor='hand2',pady=5,command=qt,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.pack()
                
            else:
                cnfrm=Toplevel(root)
                cnfrm.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(cnfrm)} center')
                
                msg=('Results of Class '+str(cls)+" "+str(section)+' found\nAre you sure you want to delete?')
                l1=Label(cnfrm,text=msg,padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.grid(row=0,column=0,columnspan=2)
                def qt():
                    cnfrm.destroy()
                ext=Button(cnfrm,text='Cancel',cursor='hand2',padx=10,pady=5,command=qt,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.grid(row=1,column=1)

                def dele():
                    global cls,section
                    os.remove('files/Class_'+str(cls)+"_"+str(section)+'.txt')
                    avl.seek(0)
                    x=avl.readlines()
                    c=0
                    for i in range(len(x)):
                        if 'files/Class_'+str(cls)+"_"+str(section) in x[i-c]:
                            del x[i-c]
                            c+=1
                    

                    w=open("files/Available.txt",'w+')
                    w.seek(0)
                    w.writelines(x)
                    cnfrm.destroy()
                    done=Toplevel(root)
                    done.config(bg="#4863A0")                    
                    root.eval(f'tk::PlaceWindow {str(done)} center')
                    
                    
                    l1=Label(done,text='Deleted Successfully',font=('Times New Roman',15),fg='white',bg='#4863A0').pack()
                    l1=Label(done,bg='#4863A0').pack()
                    def qit():
                        done.destroy()
                    b1=Button(done,text='OK',cursor='hand2',command=qit,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20).pack()                    
                    
                    
                cfrm=Button(cnfrm,text='Delete',cursor='hand2',padx=10,pady=5,command=dele,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                cfrm.grid(row=1,column=0)
           
            
    def rol():
        global cls,roll,section
        clas=Toplevel(root)
        clas.attributes('-fullscreen', True)
        clas.config(pady=10,bg='#4863A0')
        imge=PhotoImage(file='images/student.png')
        Info=Label(clas,image=imge,pady=10)
        Info.photo = imge
        Info.grid(row=0,column=1,columnspan=2)
        cls_var=IntVar()
        roll_var=IntVar()
        sctn_var=StringVar()
        cls_var.set("")
        roll_var.set("")
        sctn_var.set("")
        gp=Label(clas,bg='#4863A0',pady=20,padx=200).grid(row=1,column=0)

        def qt():
            clas.destroy()

        button_1=Button(clas,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=0,sticky='W',padx=50)
        def qt():
            opt.destroy()
            clas.destroy()
            
        gp=Label(clas,bg='#4863A0',pady=20,padx=150).grid(row=1,column=4)            
        button_1=Button(clas,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=4,sticky='E')

        msg=('Enter the class : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=2,column=1)

        msg=('Enter the Section : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=3,column=1)

        msg=('Enter the Roll No: ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=4,column=1)

        def sbmt():
            global cls,section,roll
            roll=roll_var.get()
            cls=cls_var.get()
            section=sctn_var.get()
            opt.destroy()
            clas.destroy()
            deletion()
        e1=Entry(clas,textvariable=cls_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=2,column=2)
        e2=Entry(clas,textvariable=sctn_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=3,column=2)
        e3=Entry(clas,textvariable=roll_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=4,column=2)
        gp=Label(clas,bg='#4863A0',pady=20,padx=200).grid(row=5,column=0)
        s=Button(clas,text='Submit',cursor='hand2',bg='#98AFC7',bd=10,font=('Times New Roman',15),width=40,command=sbmt)
        s.grid(row=6,column=1,columnspan=2)

        def deletion():
            global cls,section
            
            avl=open("files/Available.txt",'a+')
            avl.seek(0)
            x=avl.read()
            
            if ('files/Class_'+str(cls)+'_'+str(section)+"Roll No: "+str(roll)) not in x:
                err=Toplevel(root)
                err.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(err)} center')
                msg=('No result of Class '+str(cls)+"-"+str(section)+" Roll No: "+str(roll)+' found')
                l1=Label(err,text=msg,padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.pack()
                def qt():
                    err.destroy()
                ext=Button(err,text='OK',cursor='hand2',padx=10,pady=5,command=qt,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.pack()
                
            else:
                cnfrm=Toplevel(root)
                cnfrm.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(cnfrm)} center')
                msg=('Results of Class '+str(cls)+"-"+str(section)+"Roll No: "+str(roll)+' found\nAre you sure you want to delete?')
                l1=Label(cnfrm,text=msg,padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.grid(row=0,column=0,columnspan=2)
                def qt():
                    cnfrm.destroy()
                ext=Button(cnfrm,text='Cancel',padx=10,cursor='hand2',pady=5,command=qt,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.grid(row=1,column=1)

                def dele():
                    global cls,section,roll
                    
                    avl.seek(0)
                    x=avl.readlines()
                    c=0
                    for i in range(len(x)):
                        if 'files/Class_'+str(cls)+"_"+str(section)+"Roll No: "+str(roll) in x[i-c]:
                            del x[i-c]
                            c+=1                        
                        
                    
                    w=open("files/Available.txt",'w+')
                    w.seek(0)
                    w.writelines(x)
                    avl.seek(0)
                    x=avl.readlines()
                    y=0
                    for i in x:
                        if 'files/Class_'+str(cls)+"_"+str(section)+"Roll No: " in i:
                            y+=1
                            break
                    c=0
                    if y==0:
                        for i in range(len(x)):
                            if 'files/Class_'+str(cls)+"_"+str(section) in x[i-c]:
                                del x[i-c]
                                c+=1
                    w=open("files/Available.txt",'w+')
                    w.seek(0)
                    w.writelines(x)
                    x=open('files/Class_'+str(cls)+'_'+str(section)+'.txt','a+')
                    x.seek(0)
                    y=(x.readlines())
                    c=0
                    b=0
                    for i in range(len(y)):
                        if ('Roll No: '+str(roll)) in y[i-c]:
                            del y[i-c]
                            del y[i-c]
                            c+=2
                            if y==[]:
                                x.close()
                                os.remove('files/Class_'+str(cls)+"_"+str(section)+'.txt')
                                avl.seek(0)
                                x=avl.readlines()
                                c=0
                                for i in range(len(x)):
                                    if 'files/Class_'+str(cls)+"_"+str(section) in x[i-c]:
                                        del x[i-c]
                                        c+=1

                                w=open("files/Available.txt",'w+')
                                w.seek(0)
                                w.writelines(x)
                                b=1
                                break
                    x=open('files/Class_1_1.txt','w+')        
                    x.writelines(y)
                    x.seek(0)
                    cnfrm.destroy()
                    done=Toplevel(root)
                    done.config(bg="#4863A0")
                    
                    root.eval(f'tk::PlaceWindow {str(done)} center')
                    l1=Label(done,text='Deleted Successfully',font=('Times New Roman',15),fg='white',bg='#4863A0').pack()
                    l1=Label(done,bg='#4863A0').pack()
                    
                    def qit():
                        done.destroy()
                    b1=Button(done,text='OK',cursor='hand2',command=qit,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20).pack()
                    
                    
                    
                cfrm=Button(cnfrm,text='Delete',cursor='hand2',padx=10,pady=5,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20,command=dele)        
                cfrm.grid(row=1,column=0)

    img=PhotoImage(file='images/sd.png')
    Wlcm=Label(opt,image=img,bg='#4863A0')
    Wlcm.photo=img
    Wlcm.grid(row=0,column=1)
    gp=Label(opt,bg='#4863A0',pady=20,padx=200).grid(row=1,column=0)

    def qt():
        opt.destroy()

    button_1=Button(opt,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
    button_1.grid(row=0,column=0,sticky='W',padx=50)
    spc=Label(opt,text=' ',pady=20,bg='#4863A0').grid(row=1,column=0)
    button_1=Button(opt,text='Class - wise',cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40,pady=10, command=cls)
    button_1.grid(row=2,column=1)
    spc=Label(opt,text=' ',pady=20,bg='#4863A0').grid(row=3,column=0)   
    button_2=Button(opt,text='Student - wise',cursor='hand2',bg='#98AFC7',bd=10,font=('Freestyle Script',25),width=40,pady=10, command=rol)
    button_2.grid(row=4,column=1)


    
        
def view():
        global cls,roll,section
        
        clas=Toplevel(root)
        clas.attributes('-fullscreen', True)
        clas.config(pady=10,bg='#4863A0')
        cls_var=IntVar()
        roll_var=IntVar()
        sctn_var=StringVar()
        cls_var.set("")
        roll_var.set("")
        sctn_var.set("")
        imge=PhotoImage(file='images/student.png')
        Info=Label(clas,image=imge,pady=10)
        Info.photo = imge
        Info.grid(row=0,column=1,columnspan=2)

        gp=Label(clas,bg='#4863A0',pady=20,padx=200).grid(row=1,column=0)

        def qt():
            clas.destroy()

        button_1=Button(clas,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=0,sticky='W',padx=50)
        
        msg=('Enter the class : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=2,column=1)

        msg=('Enter the Section : ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=3,column=1)

        msg=('Enter the Roll No: ')
        l1=Label(clas,text=msg,padx=10,pady=10,font=('Freestyle Script',45),bg='#4863A0',fg='white')
        l1.grid(row=4,column=1)

        def sbmt():
            global cls,section,roll
            roll=roll_var.get()
            cls=cls_var.get()
            section=sctn_var.get()
            clas.destroy()
            display()
        e1=Entry(clas,textvariable=cls_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=2,column=2)
        e2=Entry(clas,textvariable=sctn_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=3,column=2)
        e3=Entry(clas,textvariable=roll_var,bd=5,font=('Times New Roman',15),bg='#98AFC7').grid(row=4,column=2)
        gp=Label(clas,bg='#4863A0',pady=20,padx=200).grid(row=5,column=0)
        s=Button(clas,text='Submit',cursor='hand2',bg='#98AFC7',bd=10,font=('Times New Roman',15),width=40,command=sbmt)
        s.grid(row=6,column=1,columnspan=2)

        def display():
            global cls,section,roll,name
            
            avl=open("files/Available.txt",'a+')
            avl.seek(0)
            x=avl.read()
            
            if ('files/Class_'+str(cls)+'_'+section+"Roll No: "+str(roll)) not in x:
                err=Toplevel(root)
                err.config(bg='#4863A0')
                root.eval(f'tk::PlaceWindow {str(err)} center')
                msg=('No result of Class '+str(cls)+"-"+str(section)+" Roll No: "+str(roll)+' found')
                l1=Label(err,text=msg,padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
                l1.pack()
                def qt():
                    err.destroy()
                ext=Button(err,text='OK',cursor='hand2',padx=10,pady=5,command=qt,bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
                ext.pack()
                
            else:
                fresult()
                
            
        

button_1=Button(root,text='Create New result',bg='#98AFC7',bd=10,font=('Freestyle Script',25),cursor='hand2',width=40,command=detail)
button_2=Button(root,text='View result',bg='#98AFC7',bd=10,font=('Freestyle Script',25),cursor='hand2',width=40,command=view)
button_3=Button(root,text='Delete result',bg='#98AFC7',bd=10,font=('Freestyle Script',25),cursor='hand2',width=40,command=delete)
button_1.grid(row=2,column=0)
l=Label(root,bg='#4863A0').grid(row=3,column=0)
button_2.grid(row=4,column=0)
l=Label(root,bg='#4863A0').grid(row=5,column=0)
button_3.grid(row=6,column=0)
l=Label(root,bg='#4863A0').grid(row=7,column=0)
def qt():
        root.destroy()
        quit()

button_4=Button(root,text='Quit',bg='#C24641',bd=5,font=('Segoe Print',10),cursor='hand2',width=10, command=qt)
button_4.grid(row=8,column=0,columnspan=2,sticky='E')    

def mrks():
        global pa1,pa1f,pa2,pa2f,hylt,hylp,hylf,ft,fp,ftf,subject,grd,point,cgpa,prctg
        grd=[]
        point=0
        
        for i in range(len(subject)):
            if ftf[i]>=91:
                grd.append('A1')
                point+=10
                
            elif ftf[i]>=81:
                grd.append('A2')
                point+=9
                
            elif ftf[i]>=71:
                grd.append('B1')
                point+=8
                
            elif ftf[i]>=61:
                grd.append('B2')
                point+=7
                
            elif ftf[i]>=51:
                grd.append('C1')
                point+=6
                
            elif ftf[i]>=41:
                grd.append('C2')
                point+=5
                
            elif ftf[i]>=31:
                grd.append('D')
                point+=4
                
            elif ftf[i]>=21:
                grd.append('E1')        
                
            else:
                grd.append('E2')
                
        cgpa=round(point/len(subject),2)
        
        prctg=round(cgpa*9.5,2)
        
def form():
    x=open('files/Available.txt','a+')
    x.close
    avl=open('files/Available.txt','r')
    x=avl.read()
    if 'files/Class_'+str(cls)+'_'+section+"Roll No: "+str(roll) in x:
        err=Toplevel(root)
        err.config(bg='#4863A0')
        root.eval(f'tk::PlaceWindow {str(err)} center')
        msg=('Result of Roll No: '+str(roll)+(' already exists\nUse "View Results" to see existing result.\nUse "Delete Result" to delete existing result before re-issuing Result.'))
        l1=Label(err,text=msg,justify='left',padx=10,pady=10,font=('Times New Roman',15),fg='white',bg='#4863A0')
        l1.pack()
        def qt():
            err.destroy()
        ext=Button(err,text='OK',padx=10,pady=5,command=qt,cursor='hand2',bg='#98AFC7',bd=5,font=('Times New Roman',10),width=20)        
        ext.pack()

    else:
        global subject
        
        form=Toplevel(root)
        form.attributes('-fullscreen', True)
        form.config(bg='#4863A0')
        

        m1=StringVar()
        m2=StringVar()
        m3=StringVar()
        m4=StringVar()
        m5=StringVar()
        m6=StringVar()
        m7=StringVar()
        m8=StringVar()
        m9=StringVar()
        m10=StringVar()
        m11=StringVar()
        m12=StringVar()
        m13=StringVar()
        m14=StringVar()
        m15=StringVar()
        m16=StringVar()
        m17=StringVar()
        m18=StringVar()
        m19=StringVar()
        m20=StringVar()
        m21=StringVar()
        m22=StringVar()
        m23=StringVar()
        m24=StringVar()
        
        
        def qt():
            form.destroy()
            detail()

        button_1=Button(form,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=0,sticky='W',padx=50)
        def qt():
            form.destroy()
            
        button_1=Button(form,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
        button_1.grid(row=0,column=7,sticky='E')
        img=PhotoImage(file='images/ftm.png')
        hdng1=Label(form,image=img)
        hdng1.photo=img
        hdng1.grid(row=0,column=1, columnspan=6)
            
        hdng2=Label(form, text='Periodic Assessment 1' ,bg='#4863A0',font=('Freestyle Script',35),fg='yellow')    #Periodic Assessment 1
        hdng2.grid(row=1,column=1, columnspan=6)

        hdng3=Label(form, text='M.M: 25' )    
        hdng3.config(font=('Freestyle Script',25),fg='yellow',bg='#4863A0')
        hdng3.grid(row=1,column=7)

        s1=Label(form, text=subject[0],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=2,column=0)
        s2=Label(form, text=subject[1],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=2,column=3)
        s3=Label(form, text=subject[2],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=2,column=6)
        s4=Label(form, text=subject[3],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=0)
        s5=Label(form, text=subject[4],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=3)
        
        b1=Entry(form, textvariable=m1,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=2,column=1)
        b2=Entry(form, textvariable=m2,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=2,column=4)
        b3=Entry(form, textvariable=m3,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=2,column=7)
        b4=Entry(form, textvariable=m4,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=1)
        b5=Entry(form, textvariable=m5,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=4)
        
        if len(subject)==6:
            s6=Label(form, text=subject[5],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=6)
            b6=Entry(form, textvariable=m6,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=7)

        hdng3=Label(form, text='Half Yearly Theory' ,bg='#4863A0',font=('Freestyle Script',35),fg='yellow',padx=100 )       #Half Yearly Theory
        
        hdng3.grid(row=4,column=1, columnspan=6)

        hdng4=Label(form, text='M.M: 70' )    
        hdng4.config(font=('Freestyle Script',25),fg='yellow',bg='#4863A0')
        hdng4.grid(row=4,column=7)

        s1=Label(form, text=subject[0],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=5,column=0)
        s2=Label(form, text=subject[1],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=5,column=3)
        s3=Label(form, text=subject[2],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=5,column=6)
        s4=Label(form, text=subject[3],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=0)
        s5=Label(form, text=subject[4],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=3)

        b1=Entry(form, textvariable=m7,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=5,column=1)
        b2=Entry(form, textvariable=m8,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=5,column=4)
        b3=Entry(form, textvariable=m9,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=5,column=7)
        b4=Entry(form, textvariable=m10,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=1)
        b5=Entry(form, textvariable=m11,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=4)
        
        if len(subject)==6:
            s6=Label(form, text=subject[5],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=6)
            b6=Entry(form, textvariable=m12,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=7)        

        

        hdng5=Label(form, text='Periodic Assessment 2'  ,bg='#4863A0',font=('Freestyle Script',35),fg='yellow',padx=100)        #Periodic Assessment 2
        
        hdng5.grid(row=10,column=1, columnspan=6)

        hdng6=Label(form, text='M.M: 25' )    
        hdng6.config(font=('Freestyle Script',25),fg='yellow',bg='#4863A0')
        hdng6.grid(row=10,column=7)

        s1=Label(form, text=subject[0],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=11,column=0)
        s2=Label(form, text=subject[1],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=11,column=3)
        s3=Label(form, text=subject[2],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=11,column=6)
        s4=Label(form, text=subject[3],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=12,column=0)
        s5=Label(form, text=subject[4],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=12,column=3)

        b1=Entry(form, textvariable=m13,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=11,column=1)
        b2=Entry(form, textvariable=m14,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=11,column=4)
        b3=Entry(form, textvariable=m15,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=11,column=7)
        b4=Entry(form, textvariable=m16,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=12,column=1)
        b5=Entry(form, textvariable=m17,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=12,column=4)


        if len(subject)==6:
            s6=Label(form, text=subject[5],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=12,column=6)
            b6=Entry(form, textvariable=m18,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=12,column=7)
            
        hdng6=Label(form, text='Annual Exam Theory' ,bg='#4863A0',font=('Freestyle Script',35),fg='yellow',padx=100 )           #Annual Exam
        hdng6.grid(row=13,column=1, columnspan=6)

        hdng7=Label(form, text='M.M: 70' )    
        hdng7.config(font=('Freestyle Script',25),fg='yellow',bg='#4863A0')
        hdng7.grid(row=13,column=7)

        s1=Label(form, text=subject[0],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=14,column=0)
        s2=Label(form, text=subject[1],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=14,column=3)
        s3=Label(form, text=subject[2],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=14,column=6)
        s4=Label(form, text=subject[3],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=15,column=0)
        s5=Label(form, text=subject[4],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=15,column=3)

        b1=Entry(form, textvariable=m19,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=14,column=1)
        b2=Entry(form, textvariable=m20,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=14,column=4)
        b3=Entry(form, textvariable=m21,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=14,column=7)
        b4=Entry(form, textvariable=m22,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=15,column=1)
        b5=Entry(form, textvariable=m23,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=15,column=4)
        
        if len(subject)==6:
            s6=Label(form, text=subject[5],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=15,column=6)
            b5=Entry(form, textvariable=m24,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=15,column=7)

        def practical():
            x=float(m1.get())
            
            global pa1,pa1f,pa2,pa2f,hylt,hylp,hylf,ft,fp,ftf,subject
            pa1=[float(m1.get()),float(m2.get()),float(m3.get()),float(m4.get()),float(m5.get())]
            hylt=[float(m7.get()),float(m8.get()),float(m9.get()),float(m10.get()),float(m11.get())]
            pa2=[float(m13.get()),float(m14.get()),float(m15.get()),float(m16.get()),float(m17.get())]
            ft=[float(m19.get()),float(m20.get()),float(m21.get()),float(m22.get()),float(m23.get())]

            if  len(subject)==6:
                pa1.append(float(m6.get()))
                hylt.append(float(m12.get()))
                pa2.append(float(m18.get()))
                ft.append(float(m24.get()))

            

            
            prc=Toplevel(root)
            prc.attributes('-fullscreen', True)
            prc.config(bg='#4863A0')

            m25=StringVar()
            m26=StringVar()
            m27=StringVar()
            m28=StringVar()
            m29=StringVar()
            m30=StringVar()
            m31=StringVar()
            m32=StringVar()
            m33=StringVar()
            m34=StringVar()
            m35=StringVar()
            m36=StringVar()

            def qt():
                prc.destroy()
                

            button_1=Button(prc,image=img1,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=0,sticky='W',padx=50)
            def qt():
                prc.destroy()
                form.destroy()
                
            button_1=Button(prc,image=img2,cursor='hand2',bg='#4863A0',font=('Times New Roman',15), command=qt)
            button_1.grid(row=0,column=5)
            img=PhotoImage(file='images/prctl.png')
            hdng4=Label(prc,image=img,bg='#4863A0')
            hdng4.photo=img
            
            hdng4.grid(row=0,column=1, columnspan=4)

            
            hdng5=Label(prc, text='Half Yearly Practical/Project' ,padx=100,pady=5,font=('Freestyle Script',35),fg='yellow',bg='#4863A0',bd=5)
            
            hdng5.grid(row=2,column=0, columnspan=6)
            
            hdng6=Label(prc, text='M.M: 20' )
            hdng6.config(padx=10,pady=20,font=('Freestyle Script',35),fg='yellow',bg='#4863A0',bd=5)
            hdng6.grid(row=2,column=5)

            s1=Label(prc, text=subject[0],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=0)
            s2=Label(prc, text=subject[1],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=2)
            s3=Label(prc, text=subject[2],padx=50,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=3,column=4)
            s4=Label(prc, text=subject[3],padx=100,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=4,column=0)
            s5=Label(prc, text=subject[4],padx=100,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=4,column=2)

            b1=Entry(prc, textvariable=m25,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=1)
            b2=Entry(prc, textvariable=m26,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=3)
            b3=Entry(prc, textvariable=m27,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=3,column=5)
            b4=Entry(prc, textvariable=m28,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=4,column=1)
            b5=Entry(prc, textvariable=m29,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=4,column=3)
        
            if len(subject)==6:
                s6=Label(prc, text=subject[5],padx=50,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=4,column=4)
                b6=Entry(prc, textvariable=m30,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=4,column=5)

            hdng7=Label(prc, text='Annual Exam Practical/Project',padx=100,pady=5 ,font=('Freestyle Script',35),fg='yellow',bg='#4863A0',bd=5)
            
            hdng7.grid(row=5,column=0, columnspan=6)

            hdng8=Label(prc, text='M.M: 20' )
            hdng8.config(padx=100,pady=20,font=('Freestyle Script',35),fg='yellow',bg='#4863A0',bd=5)
            hdng8.grid(row=5,column=5)

            s1=Label(prc, text=subject[0],padx=50,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=0)
            s2=Label(prc, text=subject[1],padx=50,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=2)
            s3=Label(prc, text=subject[2],padx=50,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=6,column=4)
            s4=Label(prc, text=subject[3],padx=50,pady=5,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=7,column=0)
            s5=Label(prc, text=subject[4],padx=30,font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5).grid(row=7,column=2)

            b1=Entry(prc, textvariable=m31,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=1)
            b2=Entry(prc, textvariable=m32,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=3)
            b3=Entry(prc, textvariable=m33,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=6,column=5)
            b4=Entry(prc, textvariable=m34,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=7,column=1)
            b5=Entry(prc, textvariable=m35,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=7,column=3)
        
            if len(subject)==6:
                s6=Label(prc, text=subject[5],font=('Times New Roman ',15),fg='white',bg='#4863A0',bd=5,padx=30).grid(row=7,column=4)
                b6=Entry(prc, textvariable=m36,font=('Times New Roman',10),bg='#98AFC7',bd=3).grid(row=7,column=5)


            def prctl():
                global pa1f,pa2,pa2f,hylt,hylp,hylf,ft,fp,ftf,subject
                pa1f=[]
                pa2f=[]
                hylf=[]
                ftf=[]
                hylp=[float(m25.get()),float(m26.get()),float(m27.get()),float(m28.get()),float(m29.get())]
                fp=[float(m31.get()),float(m32.get()),float(m33.get()),float(m34.get()),float(m15.get())]

                if  len(subject)==6:
                    hylp.append(float(m30.get()))            
                    fp.append(float(m36.get()))
                
                for i in range(len(subject)):
                    a=(pa1[i]/25)*10
                    pa1f.append(a)

                for i in range(len(subject)):
                    a=(pa1[i]/25)*10
                    pa2f.append(a)
                    
                for i in range(len(subject)):
                    a=pa1f[i]+hylt[i]+hylp[i]
                    hylf.append(a)

                for i in range(len(subject)):
                    a=pa2f[i]+ft[i]+fp[i]
                    ftf.append(a)

                form.destroy()
                prc.destroy()
                
                final()
                    

            Submit=Button(prc, text='S U B M I T ', padx=20, command=prctl,cursor='hand2',bg='#98AFC7',bd=5,font=('Times New Roman',11),width=50)
            Submit.grid(row=20, column =0, columnspan=8)
                

            
            
            
                
            
        Submit=Button(form, text='S U B M I T ', command=practical,cursor='hand2',bg='#98AFC7',bd=5,font=('Times New Roman',11),width=50)
        Submit.grid(row=20, column =0, columnspan=8)

    def final():         
        global pa1,pa1f,pa2,pa2f,hylt,hylp,hylf,ft,fp,ftf,subject
        rslt=open('files/Class_'+str(cls)+'_'+str(section)+'.txt','a+')
        rslt.write('Roll No: '+str(roll)+'\n')
        rslt.write(str(pa1)+';')
        rslt.write(str(pa2)+';')
        rslt.write(str(pa1f)+';')
        rslt.write(str(pa2f)+';')
        rslt.write(str(hylt)+';')
        rslt.write(str(hylp)+';')
        rslt.write(str(ft)+';')
        rslt.write(str(fp)+';')
        rslt.write(str(name)+';')
        rslt.write(str(ftf)+';')
        rslt.write(str(subject)+'\n')
        
        rslt.seek(0)
       


        fresult()
        #saving available
        avl=open("files/Available.txt",'a+')
        avl.seek(0)
        if ('files/Class_'+str(cls)+'_'+section) not in avl.read():
            avl.write('files/Class_'+str(cls)+'_'+section+'\n')
            avl.write('files/Class_'+str(cls)+'_'+section+"Roll No: "+str(roll)+'\n')
        else:
            avl.write('files/Class_'+str(cls)+'_'+section+"Roll No: "+str(roll)+'\n')
        avl.close()
        rslt.close()
       

mainloop()

