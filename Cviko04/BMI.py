def get_BMI(weight:float,height:float) ->float:
    height_m=height/100
    bmi=weight/(height_m**2)
    return bmi

def get_eval(bmi: float)->str:
    if bmi < 16.5:
        return "TEZKA PODVYZIVA"
    if bmi <18.5:
        return "NADVAHA"
    if bmi < 25:
        return "IDEALNI VAHA"
    if bmi < 30:
        return "NADVAHA"
    return "OBEZITA"

print(get_eval(get_BMI(175,187)))