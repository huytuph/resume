class Edu():
    """Education"""
    def __init__(self, course, institution, status):
        """
        Each object in the Education Class must have the following attributes
        - course
        - institution
        - status
        """
        self.course = course
        self.institution = institution
        self.status = status
    def show(self):
        """prints details of the course taken, where it was taken, and current status"""
        print(
        f"""
        Course: {self.course}
        Institution: {self.institution}
        Date: {self.status}
        """)
thm = Edu(
        "Introduction to Cyber Security, Pre Security",
        "TryHackMe.com",
        "Completed in 2023") 
ewp_boom = Edu(
        "License to operate a boom-type elevating work platform(boom length 11 metres or more)",
        "Start Training",
        "Completed in 2023")
yellow_card = Edu(
        "Operating elevating work platform",
        "Start Training",
        "Completed in 2023")
metro = Edu(
        "Train Track Safety Awareness",
        "Metro Academy",
        "Completed in 2023")
rail = Edu(
        "Safety Working in the Rail Corridor",
        "Rail Academy Newport",
        "Completed in 2023")
inner_range = Edu(
        "Integriti Basic Course",
        "InnerRange.com",
        "Completed in 2023")
white_card = Edu(
        "Vic Contruction Induction White Card",
        "WAM Training",
        "Completed in 2022")
aws_cert = Edu(
        "AWS Cloud Practitioner",
        "aCloudGuru.com",
        "Completed in 2021")
solo_py = Edu(
        "Python for Beginners",
        "SoloLearn.com",
        "Completed 2021")
lvt_admin = Edu(
        "LVTTS Administration - Light Vehicle", 
        "Box Hill Institute of TAFE", 
        "Completed in 2018")
lvt_structural = Edu(
        "LVTTS Structural Awareness", 
        "Box Hill Institute of TAFE", 
        "Completed in 2018")
lvt_inspect = Edu(
        "LVTTS Technical Inspection - Light Vehicle", 
        "Box Hill Institute of TAFE", 
        "Completed in 2018")
auto_cert = Edu(
        "AUR30405 - Certificate III in Automotive Mechanical Technology - Light Vehicle", 
        "VRQA - Victorian Registration and Qualifications Authority", 
        "Completed in 2013")
auto_apprentice = Edu(
        "AUR30405 - Certificate III in Automotive Mechanical Technology",
        "AGA - Apprenticeships Plus",
        "Completed in 2012")
auto_pre = Edu(
        "21560VIC - Ceritificate II in Automotive Technology Studies",
        "Kangan Institute",
        "Finished in 2007")
