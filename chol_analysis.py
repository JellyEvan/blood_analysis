def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return 'Nromal'
    elif 40 <= HDL_level < 60:
        return 'Borderline low'
    else :
        return 'Low'

def LDL_analysis(LDL_level):
    if LDL_level <= 130:
        return 'Nromal'
    elif 130 < LDL_level <= 159:
        return 'Borderline high'
    elif 160 <= LDL_level <189 :
        return 'High'
    elif 190 <= LDL_level:
        return 'Very high'

def TOT_analysis(TOT_level):
    if TOT_level < 200:
        return 'Nromal'
    elif 200 <= TOT_level <= 239:
        return 'Borderline high'
    elif 240 <= TOT_level:
        return 'High'

def cholesterol_analysis():
    print("Cholesterol Analysis")
    HDLinput = input("Enter test result: ")
    test_info = HDLinput.split("=")
    if test_info[0] == "HDL":
        HDL_analysis()
    if test_info[0] == "LDL":
        LDL_analysis()



def interface():
    while True:
        print("Cholesterol Calculator")
        print("Options: ")
        print("  1 - Cholesterol Analysis")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()



if __name__ == "__main__":
    interface()
    print('Hello')
    print('First')
