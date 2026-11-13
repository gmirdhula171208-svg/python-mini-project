patients = {
    101: {"name": "diya", "age": 18, "dieases": "fever"},
    102: {"name": "miru", "age": 17, "dieases": "heart problem"},
    103: {"name": "priya", "age": 17, "dieases": "teeth pain"},
    104: {"name": "pradhi", "age": 19, "dieases": "cold"}
    }

doctors = {
    201: {"name": "dr.ravi", "specialization": "general"},
    202: {"name": "dr.ram", "specialization": "cardiologist"},
    203: {"name": "dr.vaishu", "specialization": "dentist"},
    204: {"name": "dr.indu", "specialization": "general"}
    }


patients[101]["doctor"] = "dr.ravi"
patients[102]["doctor"] = "dr.ram"
patients[103]["doctor"] = "dr.vaishu"
patients[104]["doctor"] = "dr.indu"

appointments = {
    101: "13-11-26",
    102: "14-12-26",
    103: "15-11-26",
    104: "16-01-27"
    }

print("patients details")
for pid, details in patients.items():
    print("patient id", pid)
    print("Details:", details)

print("doctors details") 
for did, details in doctors.items():
    print("doctor id", did)
    print("Details:", details)

print("appointments details")
for pid, date in appointments.items():
    print("patient id:", pid)
    print("appointments date:", date)

print("Hospital Management System completed")


