def all_patient_page():
    all_patient_frame = tk.Frame(main_frame)


    search_frame= Frame(all_patient_frame,bg='#D1EAF0',)
    search_frame.grid(ipady=20,ipadx=700,padx=1)

    search= Label(search_frame,text="Search of patient report",bg='#D1EAF0', fg='#02808A', font=("Inter,bold", 12))
    search.grid(ipadx=1,ipady=20)

    search_entry = customtkinter.CTkEntry(master=search_frame,
                                          font=('Inter', 20),
                                          text_color='#000000',
                                          width=200,
                                          height=40,
                                          placeholder_text="Search",
                                          # border_width=0,
                                          corner_radius=10,
                                          fg_color="#c7ebed",
                                          bg_color="#c7ebed",
                                          border_color="#02808A",

                                          )
    search_entry.grid(padx= 10, pady= 22,row=0,column= 2,ipadx=25,ipady=5)
    search_button1 = customtkinter.CTkButton(master=search_frame,
                                           text="Search",
                                           font=('Inter', 20),
                                             text_color='#FFFFFF',
                                             # command=button_event,
                                             width=120,
                                             height=30,
                                             # border_width=0,
                                             corner_radius=8,
                                             fg_color="#02808A",
                                             bg_color="#c7ebed",
                                             border_color="#02808A",

                                             )
    search_button1.grid(padx= 20, pady= 22,row=0,column= 3,ipadx=10,ipady=5)

    detail_frame= Frame(all_patient_frame,bg="#F2F4F4")
    detail_frame.grid(ipady=600,ipadx=1000)


    scroll_x= Scrollbar(detail_frame,orient=HORIZONTAL)
    scroll_y= Scrollbar(detail_frame,orient=VERTICAL)

    patient_table= ttk.Treeview(detail_frame)
    columns= ('Patient_Name','Patient_id','Hospital_id','Patient_phone','Birth_date','Surgery_date','sex',)
    xscrollcommand = scroll_x.set
    yscrollcommand= scroll_y.set
    patient_table.place(x=0,y=1,width=1040,height=560)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=LEFT,fill=Y)
    scroll_x.config(command=patient_table.xview)
    scroll_y.config(command=patient_table.yview)

    patient_table['show']='headings'
    patient_table.heading("Patient_Name",text='PatientName')
    patient_table.heading("Patient_Id",text='PatientId')
    patient_table.heading("Hospital_id",text='HospitalId')
    patient_table.heading("Patient_phone",text='Phone')
    patient_table.heading("Birth_date",text='BirthDate')
    patient_table.heading("Surgery_date",text='SurgeryDate')
    patient_table.heading("sex",text='Sex')

    patient_table.column('Patient_Name',width=100)
    patient_table.column('Patient_Id',width=20)
    patient_table.column('Hospital_id',width=20)
    patient_table.column('Patient_phone',width=100)
    patient_table.column('Birth_date',width=80)
    patient_table.column('Surgery_date',width=80)
    patient_table.column('sex',width=50)