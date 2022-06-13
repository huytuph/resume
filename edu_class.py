class Edu():
    def __init__(self, course, institution, status):
        self.course = course
        self.institution = institution
        self.status = status
    
    def show(self):
        print(f"""
              Course: {self.course}
              Institution: {self.institution}
              Date: {self.status}
              """)
        

lvt_admin = Edu("LVTTS Administration - Light Vehicle", 
                "Box Hill Institute of TAFE", 
                "Completed in 2018")

lvt_structural = Edu("LVTTS Structural Awareness", 
                     "Box Hill Institute of TAFE", 
                     "Completed in 2018")

lvt_inspect = Edu("LVTTS Technical Inspection - Light Vehicle", 
                  "Box Hill Institute of TAFE", 
                  "Completed in 2018")

auto_cert = Edu("AUR30405 - Certificate III in Automotive Mechanical Technology - Light Vehicle", 
           "VRQA - Victorian Registration and Qualifications Authority", 
           "Completed in 2013")

auto_apprentice = Edu("AUR30405 - Certificate III in Automotive Mechanical Technology",
                      "AGA - Apprenticeships Plus",
                      "Completed in 2012")

auto_pre = Edu("21560VIC - Ceritificate II in Automotive Technology Studies",
               "Kangan Institute",
               "Finished in 2007")
