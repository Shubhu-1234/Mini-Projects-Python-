# Library Management System
class Library:
    def __init__(self,librarian,booklist,catlog):
        self.librarian=librarian
        self.booklist=booklist
        self.catlog=catlog

    def display_books(self):
        return self.booklist

    def display_catlog(self):
        return self.catlog

    def lend_books(self):
        while True:
            print(self.booklist)
            print("Enter book name:")
            a = str(input()).capitalize()
            boo = self.booklist.count(a)
            if boo == 0:
                print("Invalid Choice")
                continue
            else:
                print("Enter your name:")
                b = input().capitalize()
                x=b.isalpha()
                if x==False:
                    print("Invalid Choice")
                    continue
                else:
                    c = self.catlog.get(a)
                    if c == b:
                        return "Sorry the book had been lended already"
                    else:
                        self.catlog.update({a: b})
                        self.booklist.remove(a)
                        with open("Library.txt", "a") as f:
                            s = f"Time:[{v}]           Bookname:[{a}]           Bookowner:[{b}]               Debited\n"
                            f.write(s)
            return f"{a} book has been successfully lended."

    def donate_books(self):
        while True:
            print("Enter the book name:")
            d = str(input().capitalize())
            x=d.isalpha()
            if x==False:
                print("Invalid Choice")
                continue
            else:
                self.booklist.append(d)
            return f"{d} book has been successfully donated."

    def return_books(self):
        while True:
            print(self.catlog)
            print("Enter the book name:")
            e = str(input().capitalize())
            boo=self.catlog.get(e)
            print(boo)
            if boo==0:
                print("Invalid Choice")
                continue
            else:
                print(self.catlog)
                print("Enter your name:")
                f = input().capitalize()
                y = f.isalpha()
                print(f)
                if f != boo:
                    print("Invalid Choice")
                    continue
                else:
                        g = f
                        self.catlog.pop(e)
                        self.booklist.append(e)
                        with open("Library.txt", "a") as f:
                            s = f"Time:[{v}]           Bookname:[{e}]           Bookowner:[{g}]              Credited\n"
                            f.write(s)
            return f"{e} book has been successfully returned"

    @classmethod
    def getdate(cls):
        from datetime import datetime
        now = datetime.now()
        # print(now.strftime('%Y/%m/%d %H:%M:%S'))  # 24-hour format
        now.strftime('%Y/%m/%d %I:%M:%S %p')  # 12-hour format
        return now.strftime('%d/%m/%Y %I:%M:%S %p')  # This will print "16/06/2022 08:50:57 PM"

List_of_books=['C','C++','Java','Python']
Lended_books={}
Library_name="Shubham's Library"
Shubham_library=Library(Library_name,List_of_books,Lended_books)
v=Library.getdate()
v=str(v)
while True:
    print("1.Display Books\n2.Display Catlog\n3.Lend Books\n4.Donate Books\n5.Return Books")
    h=int(input())
    if h==1:
        print(Shubham_library.display_books())
    elif h==2:
        print(Shubham_library.display_catlog())
    elif h==3:
        print(Shubham_library.lend_books())
    elif h==4:
        print(Shubham_library.donate_books())
    elif h==5:
        print(Shubham_library.return_books())
    else:
        break




