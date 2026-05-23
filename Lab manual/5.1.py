Class Student:
      def _init_(self,name,marks):
          self.name=name
          self.marks=marks
      def show(self):
          print(self.name,self.marks)
      def result(self):
          print("pass" if self.marks>=50 else"fail")
      s=Student(input("Name:"),int(input("Marks:")))
      s.show()
      s.result()