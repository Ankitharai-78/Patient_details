from flask import Flask,request,jsonify

app=Flask(__name__)

patients_list=[
              {
                        "id":0,
                        "name":"Shilpa",
                        "age":34,
                        "disease":"Malaria",
                        "admission_date":"21/07/2020",

              },
              {
                        "id":1,
                        "name":"Rahul",
                        "age":26,
                        "disease":"Typhoid",
                        "admission_date":"2/07/2020",

              },
              {

                       "id":2,
                       "name":"John",
                       "age":"18",
                       "disease":"Dengue",
                       "admission_date":"14/07/2020",

              },
              {

                       "id":3,
                       "name":"Divya",
                       "age":32,
                       "disease":"Typhoid",
                       "admission_date":"12/08/2020",

              },
              {
                       "id":4,
                       "name":"Dafney",
                       "age":16,
                       "disease":"Malaria",
                       "admission_date":"16/08/2020",

              },
              {
                       "id":5,
                       "name":"Suresh",
                       "age":52,
                       "disease":"Dengue",
                       "admission_date":"9/07/2020",

             },
             {
                       "id":6,
                       "name":"Rajesh",
                       "age":39,
                       "disease":"Malaria",
                       "admission_date":"11/08/2020",

             },
             {
                       "id":7,
                       "name":"Priya",
                       "age":21,
                       "disease":"Typhoid",
                       "admission_date":"26/07/2020",

             },
             {
                       "id":8,
                       "name":"Elsa",
                       "age":44,
                       "disease":"Dengue",
                       "admission_date":"16/08/2020",

             },
             {
                       "id":9,
                       "name":"Sizuka",
                       "age":15,
                       "disease":"Malaria",
                       "admission_date":"13/08/2020",

             },
             {
                      "id":10,
                       "name":"Henry",
                       "age":24,
                       "disease":"ViralFever",
                       "admission_date":"14/08/2020",

             },
           ]
@app.route('/patients',methods=['GET','POST'])
def patients():
    if request.method=='GET':
        if len(patients_list)>0:
            return jsonify(patients_list)
        else:
            'Nothing Found',404
    if request.method=='POST':
            new_name=request.form['name']
            new_disease=request.form['disease']
            new_admissiondate=request.form['admission_date']
            iD=patients_list[-1]['id']+1
            if new_disease=="corona":
                return "We Do not take Corona patients here.So please go to Corona hospital."

            new_obj={
                 'id':iD,
                 'name':new_name,
                 'disease':new_disease,

                 'admission_date':new_admissiondate,

            }
            patients_list.append(new_obj)
            return jsonify(patients_list),201
@app.route('/patients/<int:id>',methods=['GET','PUT','DELETE'])
def single_patient(id):
        if request.method=='GET':
             for patient in patients_list:
                if patient['id']==id:
                    return jsonify(patient)
                pass
        if request.method=='PUT':
             for patient in patients_list:
                if patient['id']==id:
                    patient['name']=request.form['name']
                    patient['age']=request.form['age']
                    patient['disease']=request.form['disease']
                    patient['admission_date']=request.form['admission_date']
                    updated_patient={
                       'id':id,
                        'name':patient['name'],
                        'age': patient['age'],
                        'disease': patient['disease'],
                        'admission_date': patient['admission_date'],

                    }
                    return jsonify(updated_patient)
        if request.method=='DELETE':
             for index,patient in enumerate(patients_list):
                if patient['id']==id:
                   patients_list.pop(index)
                   return jsonify(patients_list)
if __name__=='__main__':
    app.run()
            
