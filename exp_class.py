class Work():
    """
    A Class for places of work
    """
    
    # a list of places of work
    work_list = []
    
    def __init__(self, job_title, company_name, date, description):
        """
        Each object in the Experience Class must have the follwing attributes
        - job title
        - company name
        - date
        - description
        """
        self.job_title = job_title
        self.company_name = company_name
        self.date = date
        self.description = description
        
        # adds the company name to the work list 
        self.work_list.append(company_name)        
        
    def show(self):
        """
        Prints a string describing what my job title was, where i worked and the dates i worked
        """
        print(f"""
              I was a {self.job_title} at {self.company_name} between {self.date}.
              Some of my duties & responsibilities were
              {self.description}
              """)

# s2 Security    
s2sec = Work("Security Technician", 
             "s2 Security", 
             "Apr 2022 - current", 
             """
             - Generating Sales leads
             - Quotations
             - Security System design
             - Cable runs
             - Cable management
             - Electrical Conduit building
             - Equipment fit offs (Access Control, Intrustion Detection Systems< Surveillance)
             - Wiring Security Systems
             - Troubleshooting & maintenance""")

# Redbook Inspect
rbi = Work("Vehicle Inspector", 
           "Redbook Inspect", 
           "Nov 2018 - Apr 2022", 
           """
           - Carry out vehicle safety inspections according to Commercial Passenger Vehicles Victoria standards, Victorian roadworthy standards & Rideshare Standards
           - Training new staff""")

# Subaru Werribee
subie_werribee = Work("Subaru Specialist", 
                      "Subaru Experience Store - Werribee", 
                      "Dec 2016 - Nov 2018", """
                      - Keeping the showroom clean & presentable
                      - Generating sales leads
                      - Organizing test drives
                      - Explaining vehicle features to customers
                      - Demonstrating vehicle capabilities
                      - Selling Merchandise""")

# Subaru Interactive Docklands
subie_interactive = Work("Senior Test driver", 
                         "Subaru Interactive - Docklands", 
                         "Nov 2013 - Nov 2018", 
                         """
                         - Keeping the showroom clean & presentable
                         - Generating sales leads
                         - Organizing test drives
                         - Explaining vehicle features to customers
                         - Demonstrating vehicle capabilities""")

# Subaru Docklands
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
