class Work():
    work_list = []
    def __init__(self, job_title, company_name, date, description):
        self.job_title = job_title
        self.company_name = company_name
        self.date = date
        self.description = description
        self.work_list.append(company_name)        
        
    def show(self):
        print(f"""
              I was a {self.job_title} at {self.company_name} between {self.date}.
              Some of my duties & responsibilities were
              {self.description}
              """)
    
s2sec = Work("Trades assistant", 
             "s2 Security", 
             "Apr 2022 - current", 
             """
             - Generating Sales leads
             - Quotations
             - Security System design
             - Cable runs
             - Cable management
             - Equipment fit offs (Access Control, Intrustion Detection Systems< Surveillance)
             - Programming Access Control
             - Troubleshooting & maintenance""")

rbi = Work("Vehicle Inspector", 
           "Redbook Inspect", 
           "Nov 2018 - Apr 2022", 
           """
           - Carry out vehicle safety inspections according to Commercial Passenger Vehicles Victoria standards, Victorian roadworthy standards & Rideshare Standards
           - Training new staff""")

subie_werribee = Work("Subaru Specialist", 
                      "Subaru Experience Store - Werribee", 
                      "Dec 2016 - Nov 2018", """
                      - Keeping the showroom clean & presentable
                      - Generating sales leads
                      - Organizing test drives
                      - Explaining vehicle features to customers
                      - Demonstrating vehicle capabilities
                      - Selling Merchandise""")

subie_interactive = Work("Senior Test driver", 
                         "Subaru Interactive - Docklands", 
                         "Nov 2013 - Nov 2018", 
                         """
                         - Keeping the showroom clean & presentable
                         - Generating sales leads
                         - Organizing test drives
                         - Explaining vehicle features to customers
                         - Demonstrating vehicle capabilities""")

subie_docklands = Work("Light Vehicle Mechanic", 
                       "Subaru Docklands", 
                       "Jul 2012 - Nov 2018", 
                       """
                       - Service and Repair Vehicles
                       - Carry out Roadworthy Inspections
                       - Carry out tyre replacements, wheel rotation and balancing
                       - Carry out brake disc machining
                       - Diagnosing electrical and mechanical faults
                       - Recondition used vehicles
                       - Training apprentices
                       - Workplace Maintenance""")
