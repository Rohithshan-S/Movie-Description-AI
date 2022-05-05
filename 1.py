from tkinter import *
#pip install imdbpy
import imdb

def search():
 root2=Toplevel()
 root2.attributes('-alpha',1.0)
 root2.geometry('890x600+200+50')
 root2.title('Movie Information')

 backpic=PhotoImage(file='toppic.png')
 backpicLabel=Label(root2,image=backpic).place(x=0,y=0)

 titleLabel=Label(root2,text='title',font=('arial',30,'bold'),fg='white',bg='#B39266')
 titleLabel.place(x=60,y=30)
 titlenameLabel=Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 titlenameLabel.place(x=300, y=30)

 directorLabel = Label(root2, text='director', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 directorLabel.place(x=60, y=100)

 directornameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 directornameLabel.place(x=300, y=100)
 yearLabel = Label(root2, text='year', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 yearLabel.place(x=60, y=170)

 yearnameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 yearnameLabel.place(x=300, y=170)

 runtimeLabel = Label(root2, text='runtime', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 runtimeLabel.place(x=60, y=240)

 runtimenameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 runtimeLabel.place(x=300, y=240)

 genreLabel = Label(root2, text='genre', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 genreLabel.place(x=60, y=310)

 genrenameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 genrenameLabel.place(x=300, y=310)

 ratingLabel = Label(root2, text='rating', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 ratingLabel.place(x=60, y=370)

 ratingnameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 ratingnameLabel.place(x=300, y=370)

 casteLabel = Label(root2, text='cast', font=('arial', 30, 'bold'), fg='white', bg='#B39266')
 casteLabel.place(x=60, y=450)

 castenameLabel = Label(root2, font=('arial', 30, 'bold'), fg='white', bg='#B39266', wraplength=615, justify=LEFT)
 castenameLabel.place(x=300, y=450)
 hr=imdb.IMDb()
 movie_name=movieEntry.get()

 movies=hr.search_movie(movie_name)
 index=movies[0].getID()

 movie=hr.get_movie(index)
 title=movie['title']
 titlenameLabel.config(text=title)
 year=movie['year']
 yearnameLabel.config(text=year)
 rating=movie['rating']
 ratingnameLabel.config(text=rating)
 genre=movie['genres']
 genrenameLabel.config(text=genre)
 director=movie['directors']
 for director in movie['directors']:
   directornameLabel.config(text=director)
 for runtime in movie['runtime']:
  hours=int(runtime)//60
  minutes=int(runtime)%60

 runtimenameLabel.config(text=str(hours)+ ' hours ' +str(minutes)+ ' minutes ' )

 cast=movie['cast']

 list_of_cast=(',').join(map(str,cast))
 castlist=list_of_cast.split(',')
 listitem=castlist[0:5]
 strr=''
 for i in listitem:
     if i==listitem[4]:
       strr=strr+i+'.'
     else:
       strr=strr+i+','

 castenameLabel.config(text=strr)





 root2.mainloop()







root=Tk()



root.geometry('1057x650+100+40')


root.title('Movie Description ')
bgpic=PhotoImage(file='pic.png')
bglabel=Label(root,image=bgpic).place(x=0,y=0)
movieLabel=Label(root,text='Movie Name-',font=('algerian',30,'bold'),bg='#DEDCDD',fg='red')
movieLabel.place(x=200,y=570)

movieEntry=Entry(root,font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE,bg='#DEDCDD')
movieEntry.place(x=490,y=575)

moviesearchButton=Button(root,text='SEARCH',font=('FELIX TITLING',20,'bold'),bd=5,relief=GROOVE
                            ,command=search)
moviesearchButton.place(x=880,y=565)
root.mainloop()
