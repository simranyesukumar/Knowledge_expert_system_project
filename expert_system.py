from experta import *
diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

def preprocess():
	global diseases_list,diseases_symptoms,symptom_map,d_desc_map,d_treatment_map
	diseases = open("list_of_diseases.txt",encoding="utf8")
	diseases_t = diseases.read()
	diseases_list = diseases_t.split("\n")
	diseases.close()
	for disease in diseases_list:
		file_disease = open("information/symptoms/" + disease + ".txt",encoding="utf8")
		disease_data = file_disease.read()
		s_list = disease_data.split("\n")
		diseases_symptoms.append(s_list)
		symptom_map[str(s_list)] = disease
		file_disease.close()
		file_disease = open("information/descriptions/" + disease + ".txt",encoding="utf8")
		disease_data = file_disease.read()
		d_desc_map[disease] = disease_data
		file_disease.close()
		file_disease = open("information/treatments/" + disease + ".txt",encoding="utf8")
		disease_data = file_disease.read()
		d_treatment_map[disease] = disease_data
		file_disease.close()
	

def identify_disease(*arguments):
	list_of_symptoms = []
	for symptom in arguments:
		list_of_symptoms.append(symptom)
	# Handle key error
	return symptom_map[str(list_of_symptoms)]

def get_details(disease):
	return d_desc_map[disease]

def get_treatments(disease):
	return d_treatment_map[disease]

def if_not_matched(disease):
		print("")
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("")
		print("The disease can be %s\n" %(id_disease))
		print("Description of the disease :\n")
		print(disease_details+"\n")
		print("Medications suggested maybe : \n")
		print(treatments+"\n")

class Greetings(KnowledgeEngine):
	@DefFacts()
	def _initial_action(self):
		print("Any of the following symptoms?")
		print("")
		yield Fact(action="find_disease")


	@Rule(Fact(action='find_disease'), NOT(Fact(headache=W())),salience = 1)
	def symptom_0(self):
		self.declare(Fact(headache=input("headache: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(back_pain=W())),salience = 1)
	def symptom_1(self):
		self.declare(Fact(back_pain=input("back pain: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(chest_pain=W())),salience = 1)
	def symptom_2(self):
		self.declare(Fact(chest_pain=input("chest pain: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(cough=W())),salience = 1)
	def symptom_3(self):
		self.declare(Fact(cough=input("cough: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(fainting=W())),salience = 1)
	def symptom_4(self):
		self.declare(Fact(fainting=input("fainting: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(fatigue=W())),salience = 1)
	def symptom_5(self):
		self.declare(Fact(fatigue=input("fatigue: ")))
	 
	@Rule(Fact(action='find_disease'), NOT(Fact(sunken_eyes=W())),salience = 1)
	def symptom_6(self):
		self.declare(Fact(sunken_eyes=input("sunken eyes: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(low_body_temp=W())),salience = 1)
	def symptom_7(self):
		self.declare(Fact(low_body_temp=input("low body temperature: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(restlessness=W())),salience = 1)
	def symptom_8(self):
		self.declare(Fact(restlessness=input("restlessness: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(sore_throat=W())),salience = 1)
	def symptom_9(self):
		self.declare(Fact(sore_throat=input("sore throat: ")))
	
	@Rule(Fact(action='find_disease'), NOT(Fact(fever=W())),salience = 1)
	def symptom_10(self):
		self.declare(Fact(fever=input("fever: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(nausea=W())),salience = 1)
	def symptom_11(self):
		self.declare(Fact(nausea=input("Nausea: ")))

	@Rule(Fact(action='find_disease'), NOT(Fact(blurred_vision=W())),salience = 1)
	def symptom_12(self):
		self.declare(Fact(blurred_vision=input("blurred_vision: ")))

	#Simran rules
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Typhoid"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="vitamin deficiency"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Vitamin B deficiency"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Calcium deficiency"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Lupus"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Tetanus"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Measles"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="pertussis"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="poliomyelitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Hypoglycaemia"))
	#end of simran's rules
		
	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Jaundice"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_1(self):
		self.declare(Fact(disease="Alzheimers"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_2(self):
		self.declare(Fact(disease="Arthritis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_3(self):
		self.declare(Fact(disease="Tuberculosis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_4(self):
		self.declare(Fact(disease="Asthma"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_5(self):
		self.declare(Fact(disease="Sinusitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_6(self):
		self.declare(Fact(disease="Epilepsy"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_7(self):
		self.declare(Fact(disease="Heart Disease"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_8(self):
		self.declare(Fact(disease="Diabetes"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_9(self):
		self.declare(Fact(disease="Glaucoma"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_10(self):
		self.declare(Fact(disease="Hyperthyroidism"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_11(self):
		self.declare(Fact(disease="Heat Stroke"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_12(self):
		self.declare(Fact(disease="Hypothermia"))

	#Simran2 rules
	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="GERD"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Laryngeal Cancer"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Salivary Gland Diseases"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Sore Throat"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Strep Throat"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Swallowing Disorders"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Tonsillitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Voice Disorder"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Croup"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Laryngitis"))
	#end of simran2's rules
		
	#Riya rules
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Maxillary sinuses"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Deviated Septums"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Chronic Sinusitis without Polyps"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="no"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Chronic Sinustis with Polyps"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="no"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Cerebral Spinal Fluid"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Allergic Rhinitis"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Alpha 1"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="yes"),Fact(sore_throat="yes"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Fatty Liver Disease"))

	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="no"),Fact(sunken_eyes="yes"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Hepatitis A"))

	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="yes"),Fact(cough="no"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Bile Duct Disease"))
	#end of Riya's rules

	#Leela rules
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="no"))
	def disease_0(self):
		self.declare(Fact(disease="Influenza"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Small pox"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="yes"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="yes"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Chicken pox"))

	        
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="yes"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Common cold"))

	 
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Mumps"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="no"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="German measles"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="yes"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="AIDS"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="no"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="no"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Yellow fever"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="yes"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Ebola"))

	
	@Rule(Fact(action='find_disease'),Fact(headache="yes"),Fact(back_pain="no"),Fact(chest_pain="no"),Fact(cough="yes"),Fact(fainting="no"),Fact(sore_throat="yes"),Fact(fatigue="no"),Fact(restlessness="no"),Fact(low_body_temp="no"),Fact(fever="yes"),Fact(sunken_eyes="no"),Fact(nausea="yes"),Fact(blurred_vision="yes"))
	def disease_0(self):
		self.declare(Fact(disease="Zika"))

	@Rule(Fact(action='find_disease'),Fact(disease=MATCH.disease),salience = -998)
	def disease(self, disease):
		id_disease = disease
		disease_details = get_details(id_disease)
		treatments = get_treatments(id_disease)
		print("The disease can be %s\n" %(id_disease))
		print("Description of the disease :\n")
		print(disease_details+"\n")
		print("Medications suggested maybe : \n")
		print(treatments+"\n")

	@Rule(Fact(action='find_disease'),
		  Fact(headache=MATCH.headache),
		  Fact(back_pain=MATCH.back_pain),
		  Fact(chest_pain=MATCH.chest_pain),
		  Fact(cough=MATCH.cough),
		  Fact(fainting=MATCH.fainting),
		  Fact(sore_throat=MATCH.sore_throat),
		  Fact(fatigue=MATCH.fatigue),
		  Fact(low_body_temp=MATCH.low_body_temp),
		  Fact(restlessness=MATCH.restlessness),
		  Fact(fever=MATCH.fever),
		  Fact(sunken_eyes=MATCH.sunken_eyes),
		  Fact(nausea=MATCH.nausea),
		  Fact(blurred_vision=MATCH.blurred_vision),NOT(Fact(disease=MATCH.disease)),salience = -999)

	def not_matched(self,headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision):
		print("\nDid not find any disease that matches your exact symptoms")
		lis = [headache, back_pain, chest_pain, cough, fainting, sore_throat, fatigue, restlessness,low_body_temp ,fever ,sunken_eyes ,nausea ,blurred_vision]
		max_count = 0
		max_disease = ""
		for key,val in symptom_map.items():
			count = 0
			temp_list = eval(key)
			for j in range(0,len(lis)):
				if(temp_list[j] == lis[j] and lis[j] == "yes"):
					count = count + 1
			if count > max_count:
				max_count = count
				max_disease = val
		if_not_matched(max_disease)


if __name__ == "__main__":
	preprocess()
	engine = Greetings()
	while(1):
		engine.reset()  
		engine.run()  
		print("Any other symptoms?")
		if input() == "no":
			exit()
		#print(engine.facts)
