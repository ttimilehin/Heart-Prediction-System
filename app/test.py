review = []
from collections import OrderedDict

def parseData():
    data = dict(OrderedDict({

        'trestbps':3,
        'chol':1,
        'thalach':2,
        'oldpeal':2,
        'sex':'male',
        'chestpain':'cp_0',
        'fbs':'True',
        'R_ECG':'R_ECG_2',
        'angina':'True',
        'slope':'slope_0',
        'ca':'ca_0',
        'thal':'thal_0',
        'age':'75 - 80',

    }))

    sexList = list()
    cpList = list()
    fbsList = list()
    R_ECGList = list()
    anginaList = list()
    slopeList = list()
    caList = list()
    thalList = list()
    ageList= list()

    sex = {'female':0, 'male':0}
    cp = {'cp_0':0,'cp_1':0,'cp_2':0,'cp_3':0}
    fbs = {'true':0,'false':0}
    R_ECG = {'R_ECG_0':0,'R_ECG_1':0,'R_ECG_2':0}
    angina = {'true':0,'false':0}
    slope = {'slope_0':0,'slope_1':0,'slope_2':0}
    ca = {'ca_0':0,'ca_1':0,'ca_2':0,'ca_3':0}
    thal = {'thal_0':0,'thal_1':0,'thal_2':0,'thal_3':0}
    age = {'25 - 30':0, '30 - 35' :0, '35 - 40':0, '45 - 50':0, '50 - 55':0, '55 - 60':0, '60 - 65':0, '65 - 70':0, '70 - 75':0, '75 - 80': 0}

    for entry in data:

        if entry == 'trestbps':
            review.append(data['trestbps'])
        if entry == 'chol':
            review.append(data['chol'])
        if entry == 'thalach':
            review.append(data['thalach'])
        if entry == 'oldpeal':
            review.append(data['oldpeal'])
            
        if entry == 'sex':
            sex[data['sex']] = 1
            for i in sex.values(): sexList.append(i)

        if entry == 'chestpain':
            cp[data['chestpain']] = 1
            for i in cp.values(): cpList.append(i)

        if entry == 'fbs':
            fbs[data['fbs']] = 1
            for i in fbs.values(): fbsList.append(i)
        
        if entry == 'R_ECG':
            R_ECG[data['R_ECG']] = 1
            for i in R_ECG.values(): R_ECGList.append(i)
        
        if entry == 'angina':
           
            angina[data['angina']] = 1
            for i in angina.values(): anginaList.append(i)

        if entry == 'slope':
            slope[data['slope']] = 1
            for i in slope.values(): slopeList.append(i)
        
        if entry == 'ca':
            ca[data['ca']] = 1
            for i in ca.values(): caList.append(i)
        
        if entry == 'thal':
            
            thal[data['thal']] = 1
            for i in thal.values(): thalList.append(i)

        if entry == 'age':
            age[data['age']] = 1
            for i in age.values(): ageList.append(i)
        
    return review+sexList+cpList+fbsList+R_ECGList+anginaList+slopeList+caList+thalList+ageList


if __name__ == "__main__":
    print(parseData())





