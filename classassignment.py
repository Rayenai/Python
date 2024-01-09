class multipleFunctions():
    def Subfields():
      subfields=["Machine Learning","Neural networks","Vision","Robotics","Speech processing","Natural Language processing"]
      print("Sub-fields in AI are:")
      for i in subfields:
         sub_fields=print(i)
      return sub_fields

    def Oddeven():
     num = int(input("Enter a Number: "))
     if num % 2 == 1:
        print(num,"is odd number")
        message = "odd number"
     else:
        print(num,"is Even number")
        message = "Even number"
     return message
    
    def Elegible():
     gender=input("Your gender:")
     age=int(input("Your age:"))
     if(gender=="Male"):
        if(age==21):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
     else:
        if(age==18):
            print("ELIGIBLE")
            message="ELIGIBLE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
     return message

     def percentage():
      subject1=int(input("Subject1="))
      subject2=int(input("Subject2="))
      subject3=int(input("Subject3="))
      subject4=int(input("Subject4="))
      subject5=int(input("Subject5="))
      total=subject1+subject2+subject3+subject4+subject5
      print("Total :",total)
      percent=print("Percentage :",float(total/500)*100)
      return percent

     def triangle():
      Height=int(input("Height:"))
      Breadth=int(input("Breadth:"))
      Area=(Height*Breadth)/2
      print("Area:",float(Area))
      Height1=int(input("Height1="))
      Height2=int(input("Height2="))
      Breadth=int(input("Breadth="))
      Perimeter=Height1+Height2+Breadth
      p=print("Perimeter of triangle",Perimeter)
      return p