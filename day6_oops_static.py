class Applicant:
    applicant_id_count=1000
    def __init__(self,application_dict,name):
        self.application_dict=application_dict
        self.applicant_id=None
        self.name=name
        self.job_band=None
    def generate_applicant_id(self):
        Applicant.applicant_id_count+=1
        self.applicant_id=Applicant.applicant_id_count
    def apply_for_job(self,job_band):
        c=self.application_dict[job_band]
        if(c<5):
            self.application_dict[job_band]+=1
            self.generate_applicant_id()
            self.job_band=job_band
            print(self.name,self.job_band,self.applicant_id)
        else:
            return -1

a=Applicant({"A":2,"B":4,"C":5},"somali")
a.apply_for_job("A")
a.apply_for_job("A")
a.apply_for_job("A")
a.apply_for_job("A")
