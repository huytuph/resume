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
        print(
        f"""
        I was a {self.job_title} at {self.company_name} between {self.date}.
        Some of my duties & responsibilities were:
        {self.description}""")

# Excelcom
excelcom = Work(
        "Security Systems Installer",
        "Excelcom",
        "Nov 2022 - current",
        """
        - configuring network switches & wireless access points
        - structured cabling (cat5e, cat6, cat6e, fibre optics & security cable)
        - cable tray, catenary wire, conduit & ducting installations
        - network cabinet & server rack installations
        - equipment fit offs (Access control, Intrusion Detection systems, Surveillance, network devices, rackmount accessories, telecommunication devices)
        - Security systems install & upgrades
        - programming zones, areas, users & permission groups
        - troubleshooting""")

# s2 Security    
s2sec = Work(
        "Security Technician", 
        "s2 Security", 
        "Apr 2022 - Nov 2022", 
        """
        - cat5e, cat6 & security cable installations
        - cable management
        - conduit & ducting installations
        - equipment fit offs (Access Control, Intrustion Detection systems, Surveillance)
        - generating Sales leads
        - Security System design
        - troubleshooting""")

# Redbook Inspect
rbi = Work(
        "Senior Vehicle Inspector",
        "Redbook Inspect,Carsales.com", 
        "Nov 2018 - Apr 2022", 
        """
        - Mentorship program with SecDevOps Engineer from carsales(6 months)
        - carry out vehicle safety inspections according to Commercial Passenger Vehicles Victoria standards, Victorian Roadworthy standards & Rideshare Standards
        - carry out pre-purchase inspections
        - training staff""")

# Subaru Interactive
subie_interactive = Work(
        "Subaru Specialist", 
        "Subaru Interactive - Docklands/Essendon/Werribee", 
        "Nov 2013 - Nov 2018", 
        """
        - generating sales leads
        - demonstrating & explaining vehicle features & technology
        - selling merchandise""")

# Subaru Docklands
subie_docklands = Work(
        "Senior Automotive Technician",
        "Subaru Docklands/Essendon",
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
