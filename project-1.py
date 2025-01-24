def main():
  # Opening Function - This Function Load the data of the file in a Variable and make it Available for whole Program
  def opening():
    
    mode = "rb"
    import pickle
    
    file = open("tables_structure_and_data.dat" , mode)
    
    try:
      while True:
        mn = pickle.load(file)
        return mn
    except EOFError:
        file.close()
      
  main = opening()
  print("Available Tables : " , main["table_names"] , main)

  def selector(name , content):
    temp = True
    count = 0

    while temp:
        for a in name:
                            
          if a in list("abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=[]\;"+"\'"+",./{}|:"+"\""+">?<	 "):
                  count += 1
          else:
                  pass
                                
        if  count == 0:
                name = int(name)
                temp = False
                               
        else:
                             
                temp = True
                print("\nERROR : WRONG DATATYPE\n")
                name = input(content)
                count = 0
    return name
       

  # create function

  def create():

    print("\n    WARNING - Do this Very carefully Otherwise You may Regret Afterwhile and also can't handle its after effects")
    print("  As You Once Enter the Name of the Table and Fields it will Not Change Forever !!\n")
    
    #file opening
    
    import pickle
    mode = "wb"
    file = open("tables_structure_and_data.dat" , mode)

    # Variables
   
    field_names = []
    data_type_collection = []
    content = {}

    #Entry of name and number of fields

    name=input("Enter name of the Table : ")
    
    if name in main["table_names"]:
      print("Error : File Already Exists")
    
    temp = True
    
    number_of_fields=input("How many fields do you want in your Table (" + name + ") : ")
    
    temp_list=[]
    
    for a in range(100):
      
        temp_list+=[str(a)]
        
    while temp:
      
      if  number_of_fields in temp_list:
        number_of_fields=int(number_of_fields)
        temp=False
        
      else:
       
        temp=True
        print("WRONG INPUT")
        number_of_fields=input("How many fields do you want in your Table (" + name + ") : ")
      
      
  # Loop (Filling of Variables (field_names & data_type_collection)
    
    for a in range(number_of_fields):
      
        field = str(input("Enter name of the field ({}) : ".format(a+1)))
        print("\n")
        
        field_names+=[field]
        content[field]=[]

        print("WARNING\n")
        print('''Enter (int) if the data that you want to enter \
into the '{}' is numeric values'''.format(field))
        print('''Enter (str) if the data that you want to enter \
into '{}' is collection of Alphabets or mixer of Alphabets and Numbers\n'''.format(field))
        
        
        data_type=str(input("Enter the type of data that you want to enter in the " + field + " field : "))
        print("\n")
        
        situation=True
        
        while situation:
          
          if data_type in["int","str"]:
            data_type_collection+=[data_type]
            situation=False
            
          else:
        
             print("\nERROR : Wrong Input. Rewrite The DataType\n")
             print("WARNING\n")
             print('''Enter (int) if the data that you want to enter into \
the '{}' is numeric values'''.format(field))
             print('''Enter (str) if the data that you want to enter \
into '{}' is collection of Alphabets or mixer of Alphabets and Numbers\n'''.format(field))
          
             data_type = str(input('''Enter the type of data that you want to enter \
in the ''' + field+ " field Again : "))
             print("\n")
             
             situation=True
             

    main["table_names"]+=[name]
    main[name]=[name,number_of_fields,field_names,data_type_collection,content]
    
    # writing in the file
    
    pickle.dump(main,file)
    file.close()

  # insert function

  def insert():

    if len(main["table_names"]) != 0 :
      
      print("Entered Tables : " , main["table_names"])
      name = input("Enter the name of the table in which you want to insert the data : ")
      
      if name in main["table_names"] :
        if len(main[name][2])!=0 :
          
          number=input("How many record do you want to insert in the Table (" + name + ") : ")
          temp_list=[]
          temp=True
          
          for a in range(100):
            temp_list+=[str(a)]
            
          while temp:
            
            if  number in temp_list:
              
              number=int(number)
              temp=False
              
            else:
             
              temp=True
              print("WRONG INPUT")
              number=input("How many fields do you want in your Table("+name+") : ")
          
          print("\nThese are the fields that are present in the Table ("+name+"): "+str(main[name][2]))
          print("\nThese are the data type that are present in the Table ("+name+") "+str(main[name][3]))
          print("These data_type corresponds to the field order")
          
          for a in range(number):
            for b in range(len(main[name][2])):
              
              data=input("Enter the data that you want to enter in the "+main[name][2][b]+" : ")
              
              if main[name][3][b]=="int":
                data=selector(data,'''Enter the data that you want to enter in \
  the '''+main[name][2][b]+" : ")

                
                temp=main[name][2]
                main[name][4][temp[b]]+=[data]

              elif main[name][3][b]=="str":
                temp=main[name][2]
                main[name][4][temp[b]]+=[data]
                
            print("\n")

          # writing in the file
          
          mode="wb"
          import pickle
          file=open("tables_structure_and_data.dat",mode)
          pickle.dump(main,file)
          file.close()

        else:
          print('''\nERROR : This Table Does Not Conatin Any Field . First \
Add A Field in This Table and Then Try Again!!!''')
      else:
        print('''\nERROR : Demanded Table does not Exists.\n''')
    else:
      print('''\nERROR : Any Table does not exist in this Program . Create\
  a Table and Then Try Again!!\n''')

  def show():
     
    size=20
    structure1="+--------------------"              
    structure2="+--------------------+"                  

    space=" "
    per="|"
    
    if len(main["table_names"])!=0:
      
      print("Entered Tables : ",main["table_names"])
      name=input("Enter the name of the Table that you want to See : ")
      
      if name in main["table_names"]:
        
        field = main[name][2]
        data_type = main[name][3]
        data = main[name][4]

        if len(field)!=0:
          if len(data[field[0]])!=0:
            
            for a in range(len(data[field[0]])):
              if a==0:
                  structure = space*6+structure1*(len(field)-1)+structure2
                  print(structure)
                  
              for b in range(len(field)):
                  if a==0:
                    if b==0 and len(field)!=1:
                      
                      data1=field[b]
                      temp=size-len(data1)
                      structure=space*6+per+data1+temp*space
                      print(structure,end="")
                      
                    if b==0 and len(field)==1:
                      
                      data1=field[b]
                      temp=size-len(data1)
                      structure=space*6+per+data1+temp*space+per
                      print(structure)
                      
                      structure=space*6+structure1*(len(field)-1)+structure2
                      print(structure)
                    
                      for c in range(len(field)):
                          if c==0:
                            
                            data1=str(data[field[c]][a])
                            temp=size-len(data1)
                            structure="Row "+str(a)+" "+per+data1+temp*space+per
                            print(structure)
                         
                    if b>0 and b<(len(field)-1):
                      
                      data1=field[b]
                      temp=size-len(data1)
                      structure=per+data1+temp*space
                      print(structure,end="")
                    
                    if b==len(field)-1 and len(field)!=1:
                      
                      data1=field[b]
                      temp=size-len(data1)
                      structure=per+data1+temp*space+per
                      print(structure)
                      structure=space*6+structure1*(len(field)-1)+structure2
                      print(structure)
                      
                      for c in range(len(field)):
                        if c==0:
                          
                          data1=str(data[field[c]][a])
                          temp=size-len(data1)
                          structure="Row "+str(a)+" "+per+data1+temp*space
                          print(structure,end="")
                          
                        if c>0 and c<len(field)-1:
                          data1=str(data[field[c]][a])
                          temp=size-len(data1)
                          structure=per+data1+temp*space
                          print(structure,end="")
                          
                        if c==len(field)-1 :
                          data1=str(data[field[c]][a])
                          temp=size-len(data1)
                          structure=per+data1+temp*space+per
                          print(structure)
                        
                        
                  else:
                    
                    if b==0 and len(field)!=1:
                      
                      data1=str(data[field[b]][a])
                      temp=size-len(data1)
                      structure="Row "+str(a)+" " +per+data1+temp*space
                      print(structure,end="")
                      
                    if b==0 and len(field)==1:
                      
                      data1=str(data[field[b]][a])
                      temp=size-len(data1)
                      structure="Row "+str(a)+" " +per+data1+temp*space+per
                      print(structure)
                      
                    if b>0 and b<len(field)-1:
                      
                      data1=str(data[field[b]][a])
                      temp=size-len(data1)
                      structure=per+data1+temp*space
                      print(structure,end="")
                      
                    if b==len(field)-1 and len(field)!=1:
                      
                      data1=str(data[field[b]][a])
                      temp=size-len(data1)
                      structure=per+data1+temp*space+per
                      print(structure)
                      

            structure=space*6+structure1*(len(field)-1)+structure2
            print(structure)

          else:
            print("\nERROR : No Data is present in this Table ('{}')\n".format(name))
        else:
          print("\nERROR : There is no fields in this Table( {} )\n".format(name))
      else:
        print("\nERROR : Demanded Table does not exist\n")
    else:
      print("\nERROR : Any Table does not exist in this Program . Create a Table and Then Try Again!!\n")

  # Delete_field Function

  def delete_field():
     
      
      if len(main["table_names"])!=0:
        
         print("Entered Tables : ",main["table_names"])
         name=input("Enter the name of the Table in which you want to Delete the Field : ")
         
         if name in main["table_names"]:
           
          print('''\nThese are the Fields that are present in\
  the Table ('{}') : '''.format(name),main[name][2],)

          if len(main[name][2])!=0:

            field=input("Enter the field that you want to delete from the Table ('{}') : ".format(name))

            if field in main[name][2]:
          
              del main[name][4][field]
              main[name][1]-=1
              pos=main[name][2].index(field)
              del main[name][2][pos]
              del main[name][3][pos]

              # writing in the file

              mode="wb"
              import pickle
              file=open("tables_structure_and_data.dat",mode)
              pickle.dump(main,file)
              file.close()

            else:
              print("\nERROR : Entered Field Name Does Not exist in This Table ({})".format(name))
          else:
            print("\nERROR : This Table({}) Does not Contain any Fields\n".format(name))
         else:
           print("\nERROR : Demanded Table does not exist.\n")
      else:
        print('''\nERROR : Any Table does not exist in this Program . Create\
  a Table and Then Try Again!!\n''')

  # Remove_table Function
        
  def remove_table():
    
    if len(main["table_names"])!=0:

      print("Entered Tables : ",main["table_names"])
      name=input("Enter the Table that you want to Delete : ")

      if name in main["table_names"]:

        del main[name]
        main["table_names"].remove(name)

        # writing in the file

        mode="wb"
        import pickle
        file=open("tables_structure_and_data.dat",mode)
        pickle.dump(main,file)
        file.close()
        
      else:
        print("\n""ERROR : Table ({}) does not Exists.\n".format(name))
    else:
      print("\nERROR : Any Table does not exist in this Program . Create a Table and Then Try Again!!\n")

  #Add_field Function
      
  def add_field():
    
    if len(main["table_names"])!=0:

      print("\nAvailable Tables : ",main["table_names"])
      name=input("\nEnter the name of the Table in which you want to add a New Field : ")

      if name in main["table_names"]:

        print("\n Available Fields in Table ({}) : ".format(name),main[name][2])
        name1=input("\nEnter the name of the New Field : ")
        print("\nWARNING\n")
        print('''Enter (int) if the data that you want to enter\
  into the '{}' is numeric values'''.format(name1))
        print('''Enter (str) if the data that you want\
  to enter into '{}' is collection of Alphabets or mixer of Alphabets and Numbers\n'''.format(name1))
                
        data_type=str(input("Enter the type of data that you want to enter in the (" + name1+ ") field : "))
        print("\n")
        situation=True
        
        while situation:

          if data_type in["int","str"]:

            situation=False

          else:
            
             print("\nERROR : Wrong DataType\n")
             print("WARNING\n")
             print('''Enter (int) if the data that you want to \
enter into the '{}' is numeric values'''.format(name1))
             print('''Enter (str) if the data that you want to enter \
into '{}' is collection of Alphabets or mixer of Alphabets and Numbers\n'''.format(name1))
          
             data_type=str(input("""Enter the type of data that you want to enter in \
the """ + name1+ " field Again : "))
             print("\n")
             situation=True
                 
        if len(main[name][2])!=0:

            print("\n Enter field name if you want your New field after any Existing Field")
            print("\nAvaliable Fields in this Table : ",main[name][2])
            print("\n Enter (END) if you want to insert your New Field at the end")
            print("\n Enter (START) if you want to insert your New Field at the end\n")
    
            field=(str(input("""Enter the name of the Field after\
  which you want your New Field ({}) : """.format(name1))))

            if field in main[name][2]:
              
              main[name][1]+=1
              pos=main[name][2].index(field)
              main[name][2].insert(pos+1,name1)
              main[name][3].insert(pos+1,data_type)
              temp=main[name][4][field]
              main[name][4][name1]=[]
              
              for dat in range(len(temp)):

                  if data_type=="str":

                    main[name][4][name1]+=["NULL"]

                  if data_type=="int":

                    main[name][4][name1]+=[0]

              # writing in the file
                      
              mode="wb"
              import pickle
              file=open("tables_structure_and_data.dat",mode)
              pickle.dump(main,file)
              file.close()

            elif field == "end":
              
                main[name][1]+=1
                main[name][2].insert((len(main[name][2])),name1)
                main[name][3].insert((len(main[name][2])),data_type)
                temp=main[name][2][0]
                temp1=main[name][4][temp]
                main[name][4][name1]=[]

                for dat in range(len(temp1)):

                  if data_type=="str":
                    main[name][4][name1]+=["NULL"]
                  if data_type=="int":
                    main[name][4][name1]+=[0]
                    
                # writing in the file
               
                mode="wb"
                import pickle
                file=open("tables_structure_and_data.dat",mode)
                pickle.dump(main,file)
                file.close()

            elif field == "start":
              
                main[name][1]+=1
                main[name][2].insert(0,name1)
                main[name][3].insert(0,data_type)
                temp=main[name][2][1]
                temp1=main[name][4][temp]
                main[name][4][name1]=[]

                for dat in range(len(temp1)):
                  
                  if data_type=="str":
                    main[name][4][name1]+=["NULL"]
                  if data_type=="int":
                    main[name][4][name1]+=[0]

                # writing in the file  

                mode="wb"
                import pickle
                file=open("tables_structure_and_data.dat",mode)
                pickle.dump(main,file)
                file.close()
                
            else:
                print("\n Invalid Input and You may Enter Wrong Field Name By Mistake. \n")
                
        else:
          
          main[name][1]+=1
          main[name][2]+=name1
          main[name][3]+=data_type
          main[name][4][name1]=[]

          # writing in the file

          mode="wb"
          import pickle
          file=open("tables_structure_and_data.dat",mode)
          pickle.dump(main,file)
          file.close()
          print(main)
      
      else:
        print("\nERROR : Demanded Table does not exist.\n")
     
    else:
      print("\nERROR : Any Table does not exist in this Program . Create a Table and Then Try Again!!!\n")

  def delete_record():
    
    if len(main["table_names"])!=0:
      print("Available Tables : ",main["table_names"])
      name=input("Enter the name of the Table in which you wanna Delete Records : ")
      if name in main["table_names"]:
        fields_list=main[name][2]
        if len(fields_list)!=0:
          if len(main[name][4][fields_list[0]])!=0:
            field=input("Enter the number of the Records which you want to Delete : ")
            field=selector(field,"Enter the number of the Record which you want to Delete : ")
          
            if field<=len(main[name][4][fields_list[0]]):
                
              for b in range(field):
                
                      row=input("Enter the Row number : ")
                      row=selector(row,"Enter the Row number : ")

                      if row < len(main[name][4][fields_list[0]]):
                        for c in fields_list:
                          
                         del main[name][4][c][row]

                        # writing in the file

                        mode="wb"
                        import pickle
                        file=open("tables_structure_and_data.dat",mode)
                        pickle.dump(main,file)
                        file.close()
                        print(main)
                        
                      else:
                        print('''\n ERROR : Entered Number of Rows exceeds \
the existing Number of Records in the Table\n''')
            else:
              
              print('''\nERROR : Number of Records you Entered exceeds \
the Number of Records that is Present in Table ( {} )'''.format(name))
          else:
             print("\nERROR : This Table does not conatin any Record!!")
        else:
          print("\nERROR : This Table Does Not Have Any Field . Add necessary Fields And Then Try Again!!")
      else:
        print("\nERROR : Demanded Table does not exist.\n")    
    else:
      print("""\nERROR :Any Table does not exist in this Program . Cre\
ate a Table and Then Try Again!!\n""")
      

  #Change_name function

  def change_name():

    
    if len(main["table_names"])!=0:
      print("Entered Tables : ",main["table_names"])
      name=input("Enter the name of the Table in which you want to Alter something : ")

      if name in main["table_names"]:
          field=main[name][2]

          if len(field)!=0:
            print("\nAvailable Fields in the Table ({}) : ".format(name),field)
            step1=input("\nEnter the name of the Field from which you wanna Alter Cell Data : ")

            if step1 in main[name][2]:
              row=input("\nEnter the Row Number where the Cell Data that you wanna Alter is Present : ") 
              row=selector(row,"""\nEnter the Row Number where the Cell \
Data that you wanna Alter is Present : """)
              data=main[name][4]


              if row<len(data[field[0]]):
                pos=main[name][2].index(step1)

                if main[name][3][pos]=="int":
                        new=input("\nEnter the New Cell Data : ")
                        new=selector(new,"\nEnter the New Cell Data : ")
                        data[step1][row]=new

                if main[name][3][pos]=="str":
                        new=str(input("\nEnter the New Cell Data : "))
                        data[step1][row]=new
                    
                # writing in the file

                mode="wb"
                import pickle
                file=open("tables_structure_and_data.dat",mode)
                pickle.dump(main,file)
                file.close()

              else:
                print("""\n ERROR : Entered Row Number exceeds the existing Number \
of Records in the Table\n""")
            else:
             print("\nERROR : Entered Field Name does not exist in This Table ({}) ".format(name))
          else:
            print("\nERROR : This Table Does Not Have Any Field.\n")
      else:
        print("\nERROR : Demanded Table does not exist.\n")
    else:
      print("""\nERROR : Any Table does not exist in this Program . Create \
a Table and Then Try Again!!\n""")

            
  # show_tables Function

  def show_tables():
    
    num=len(main["table_names"])

    if num!=0:
      print("This Program contains "+str(num)+" Tables which are : ")

      for a in main["table_names"]:
          print(a+"|",end="")

    else:
      print("This Program contains "+str(num)+" Tables")

  # Structure Function

  def structure():

    if len(main["table_names"])!=0:
      print("Available Tables : ",main["table_names"])
      name=input("Enter the name of the Table")
      
      if name in main["table_names"]:
        print("\n           TABLE ({}) INFORMATION      \n".format(name))
        print("Name of the Table : ",main[name][0])
        print("Number of Fields Present in this Table : ",main[name][1])
        print("Available Fields in this Table : ",main[name][2])
        print("Available Fields Datatype in this Table : ",main[name][3])
        
      else:
        print("Entered Table does not Exists.")
        
    else:
      print("\nERROR : Any Table does not exist in this Program . Create a Table and Then Try Again!!\n")
     
  #------------------------------------------------------------------------------------------------------
  # Condition Variable

  condition=True

  # Main Loop (Choice Loop)
  
  print('''              WARNING : MAKE SURE THAT YOUR FONT MUST BE COURIER NEW.''')

  while condition:
    
    print('''\n\nEnter (0) to start with Zero Tables
  Enter (1) for creating a Table
  Enter (2) for inserting the data in the Table
  Enter (3) for Table Display
  Enter (4) for Deletion of the Field
  Enter (5) for Table Deletion
  Enter (6) for Addition of New Field
  Enter (7) for Deletion of Records
  Enter (8) for Alter Cell Data
  Enter (9) for Showcase of Tables contained by Program
  Enter (10)for Table Structure
  Enter (11) for Exit\n\n''')
      

    # Obtaining the Choices

    choice=input("Enter the choice : ")

    temp_list=[]
    temp=True

    for a in range(12):
        temp_list+=[str(a)]
        
    while temp:
        
      if  choice in temp_list:
        choice=int(choice)
        temp=False
          
      else:
        print("\nERROR : WRONG INPUT\n")
        choice=input("\nEnter the choice Again : ")
      
      if choice==1:
        create()
        
      elif choice==2:
        insert()
        
      elif choice==3:
        
        show()
        
      elif choice==4:
        delete_field()

      elif choice==5:
        remove_table()

      elif choice==6:
        add_field()

      elif choice==7:
        delete_record()

      elif choice==8:
        change_name()

      elif choice==9:
        show_tables()

      elif choice==10:
        structure()

      elif choice == 11:
        condition=False

      elif choice==0:

        import pickle
        file=open("tables_structure_and_data.dat","wb")
        information_of_tables={"table_names":[]}
        pickle.dump(information_of_tables,file)
        file.close()

        mode="rb"
        import pickle
        file=open("tables_structure_and_data.dat",mode)
        try:
          while True:
              main=pickle.load(file)
              print(main)
        except EOFError:
            file.close()

print("""             WARNING :(1) IF YOU ARE RUNNING THIS CODE FOR THE FIRST TIME , THEN ENTER \'FIRST\' IN THE CURRENT STATE .  \n             WARNING :(2) IF YOU ARE NOT RUNNING THIS CODE FOR THE FIRST TIME , THEN ENTER \'NOT FIRST\' IN THE CURRENT STATE . \
\n\n              WARNING : IF YOU ARE NOT RUNNING THIS CODE FOR THE FIRST TIME AND STILL ENTER \'FIRST\' IN THE CURRENT STATE , THEN YOU LOST ALL YOUR SAVED TABLES . \
\n\n\n            IMPORTANT : THIS STEP CREATES THE NECESSARY FILE IN YOUR SYSTEM . """)

opinion=(input("Enter your current state : ")).upper()

if opinion == "FIRST":
  import pickle
  file = open("tables_structure_and_data.dat" , "wb")
  information_of_tables = {"table_names":[]}
  pickle.dump(information_of_tables , file)
  file.close()
  main()

elif opinion == "NOT FIRST":
  main()

else:
  print("Invalid Input")
