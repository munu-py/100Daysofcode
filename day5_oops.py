class Instructor:
    def __init__(self,instructor_name,technology_skill,experience,avg_feedback):
        self.__instructor_name=instructor_name
        self.__technology_skill=technology_skill
        self.__experience=experience
        self.__avg_feedback=avg_feedback

    def set_instructor_name(self,instructor_name):
        self.__instructor_name=instructor_name
    def set_technology_skill(self,technology_skill):
        self.__technology_skill=technology_skill
    def set_experience(self,experience):
        self.__experience=experience
    def set_avg_feedback(self,avg_feedback):
        self.__avg_feedback=avg_feedback

    def check_eligibility(self):
        if(self.__experience>3 and self.__avg_feedback>=4.5):
            print(True)
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            print( True)
        else:
            print(False)
    def allocate_course(self,technology):
        f="False"
        for i in self.__technology_skill:
            if i.upper()==technology.upper():
                f="True"
                break
        print(f)

m=Instructor("bob",["c","java","net"],3,6)
m.check_eligibility()
m.allocate_course("fuck")



