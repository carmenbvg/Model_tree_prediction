def predict_diabetes(pregnancies=None,
                     glucose=None,
                     blood_pressure=None,
                     skinfold=None,
                     insulin=None,
                     bmi=None,
                     diabetes_pedigree=None,
                     age=None):
    """ Predictor for Diabetes from model/61bdc0afaba2df45470014e8

        Dataset created from a study of diabetes in females 21 years or older and of Pima Indian heritage. 
        Pima Indians are an interesting population to study for diabetes because they have a higher incidence of diabetes than the general U.S. population.
        Source
        Pima Indians Diabetes Data Set[*] 
        Bache, K. & Lichman, M. (2013). UCI Machine Learning Repository[*]. Irvine, CA: University of California, School of Information and Computer Science.
        
        [*]Pima Indians Diabetes Data Set: http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes
        [*]UCI Machine Learning Repository: http://archive.ics.uci.edu/ml
    """
    if (glucose is None):
        return u'False'
    if (glucose > 153):
        if (glucose > 166):
            if (skinfold is None):
                return u'True'
            if (skinfold > 31):
                return u'True'
            if (skinfold <= 31):
                if (glucose > 178):
                    if (bmi is None):
                        return u'True'
                    if (bmi > 35.3):
                        if (blood_pressure is None):
                            return u'True'
                        if (blood_pressure > 93):
                            return u'False'
                        if (blood_pressure <= 93):
                            return u'True'
                    if (bmi <= 35.3):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.6635):
                            return u'True'
                        if (diabetes_pedigree <= 0.6635):
                            if (skinfold > 27):
                                if (bmi > 34.15):
                                    return u'False'
                                if (bmi <= 34.15):
                                    return u'True'
                            if (skinfold <= 27):
                                return u'False'
                if (glucose <= 178):
                    return u'True'
        if (glucose <= 166):
            if (skinfold is None):
                return u'True'
            if (skinfold > 42):
                return u'False'
            if (skinfold <= 42):
                if (glucose > 154):
                    if (age is None):
                        return u'True'
                    if (age > 53):
                        return u'False'
                    if (age <= 53):
                        if (blood_pressure is None):
                            return u'True'
                        if (blood_pressure > 75):
                            return u'True'
                        if (blood_pressure <= 75):
                            if (diabetes_pedigree is None):
                                return u'True'
                            if (diabetes_pedigree > 0.3105):
                                if (glucose > 164):
                                    if (bmi is None):
                                        return u'False'
                                    if (bmi > 29.7):
                                        return u'False'
                                    if (bmi <= 29.7):
                                        return u'True'
                                if (glucose <= 164):
                                    return u'True'
                            if (diabetes_pedigree <= 0.3105):
                                if (blood_pressure > 63):
                                    return u'False'
                                if (blood_pressure <= 63):
                                    return u'True'
                if (glucose <= 154):
                    return u'False'
    if (glucose <= 153):
        if (age is None):
            return u'False'
        if (age > 28):
            if (glucose > 100):
                if (bmi is None):
                    return u'False'
                if (bmi > 26.89821):
                    if (bmi > 43.06667):
                        return u'True'
                    if (bmi <= 43.06667):
                        if (diabetes_pedigree is None):
                            return u'True'
                        if (diabetes_pedigree > 0.5091):
                            if (blood_pressure is None):
                                return u'True'
                            if (blood_pressure > 69):
                                if (diabetes_pedigree > 1.381):
                                    return u'False'
                                if (diabetes_pedigree <= 1.381):
                                    if (glucose > 123):
                                        return u'True'
                                    if (glucose <= 123):
                                        if (bmi > 35.95):
                                            return u'False'
                                        if (bmi <= 35.95):
                                            if (glucose > 119):
                                                return u'False'
                                            if (glucose <= 119):
                                                return u'True'
                            if (blood_pressure <= 69):
                                if (bmi > 31.7):
                                    if (skinfold is None):
                                        return u'True'
                                    if (skinfold > 37):
                                        return u'False'
                                    if (skinfold <= 37):
                                        return u'True'
                                if (bmi <= 31.7):
                                    if (bmi > 27.2):
                                        return u'False'
                                    if (bmi <= 27.2):
                                        return u'True'
                        if (diabetes_pedigree <= 0.5091):
                            if (blood_pressure is None):
                                return u'False'
                            if (blood_pressure > 84):
                                if (insulin is None):
                                    return u'False'
                                if (insulin > 124):
                                    if (bmi > 32.6):
                                        return u'True'
                                    if (bmi <= 32.6):
                                        return u'False'
                                if (insulin <= 124):
                                    return u'False'
                            if (blood_pressure <= 84):
                                if (blood_pressure > 59):
                                    if (skinfold is None):
                                        return u'True'
                                    if (skinfold > 42):
                                        return u'False'
                                    if (skinfold <= 42):
                                        if (age > 58):
                                            return u'False'
                                        if (age <= 58):
                                            if (diabetes_pedigree > 0.3825):
                                                if (age > 36):
                                                    return u'True'
                                                if (age <= 36):
                                                    return u'False'
                                            if (diabetes_pedigree <= 0.3825):
                                                if (diabetes_pedigree > 0.333):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.333):
                                                    if (insulin is None):
                                                        return u'True'
                                                    if (insulin > 184):
                                                        return u'False'
                                                    if (insulin <= 184):
                                                        if (glucose > 134):
                                                            return u'True'
                                                        if (glucose <= 134):
                                                            if (diabetes_pedigree > 0.2525):
                                                                if (pregnancies is None):
                                                                    return u'True'
                                                                if (pregnancies > 9):
                                                                    if (blood_pressure > 67):
                                                                        return u'False'
                                                                    if (blood_pressure <= 67):
                                                                        return u'True'
                                                                if (pregnancies <= 9):
                                                                    if (bmi > 38.65):
                                                                        if (blood_pressure > 78):
                                                                            return u'False'
                                                                        if (blood_pressure <= 78):
                                                                            return u'True'
                                                                    if (bmi <= 38.65):
                                                                        return u'True'
                                                            if (diabetes_pedigree <= 0.2525):
                                                                if (diabetes_pedigree > 0.2035):
                                                                    return u'False'
                                                                if (diabetes_pedigree <= 0.2035):
                                                                    if (pregnancies is None):
                                                                        return u'False'
                                                                    if (pregnancies > 5):
                                                                        return u'True'
                                                                    if (pregnancies <= 5):
                                                                        if (diabetes_pedigree > 0.178):
                                                                            return u'True'
                                                                        if (diabetes_pedigree <= 0.178):
                                                                            return u'False'
                                if (blood_pressure <= 59):
                                    return u'False'
                if (bmi <= 26.89821):
                    if (blood_pressure is None):
                        return u'False'
                    if (blood_pressure > 73):
                        return u'False'
                    if (blood_pressure <= 73):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.478):
                            return u'False'
                        if (diabetes_pedigree <= 0.478):
                            if (diabetes_pedigree > 0.263):
                                return u'True'
                            if (diabetes_pedigree <= 0.263):
                                return u'False'
            if (glucose <= 100):
                if (blood_pressure is None):
                    return u'False'
                if (blood_pressure > 71):
                    if (insulin is None):
                        return u'False'
                    if (insulin > 145):
                        return u'True'
                    if (insulin <= 145):
                        if (blood_pressure > 77):
                            return u'False'
                        if (blood_pressure <= 77):
                            if (skinfold is None):
                                return u'False'
                            if (skinfold > 20):
                                if (bmi is None):
                                    return u'False'
                                if (bmi > 30.85):
                                    if (blood_pressure > 75):
                                        return u'True'
                                    if (blood_pressure <= 75):
                                        return u'False'
                                if (bmi <= 30.85):
                                    return u'True'
                            if (skinfold <= 20):
                                return u'False'
                if (blood_pressure <= 71):
                    return u'False'
        if (age <= 28):
            if (bmi is None):
                return u'False'
            if (bmi > 31.15208):
                if (bmi > 41.81667):
                    if (bmi > 45.4):
                        if (diabetes_pedigree is None):
                            return u'True'
                        if (diabetes_pedigree > 0.688):
                            return u'False'
                        if (diabetes_pedigree <= 0.688):
                            return u'True'
                    if (bmi <= 45.4):
                        if (glucose > 117):
                            if (age > 25):
                                return u'False'
                            if (age <= 25):
                                if (skinfold is None):
                                    return u'True'
                                if (skinfold > 48):
                                    return u'False'
                                if (skinfold <= 48):
                                    return u'True'
                        if (glucose <= 117):
                            return u'False'
                if (bmi <= 41.81667):
                    if (bmi > 38.26667):
                        return u'False'
                    if (bmi <= 38.26667):
                        if (diabetes_pedigree is None):
                            return u'False'
                        if (diabetes_pedigree > 0.48974):
                            if (skinfold is None):
                                return u'False'
                            if (skinfold > 39):
                                return u'True'
                            if (skinfold <= 39):
                                if (bmi > 31.4):
                                    if (bmi > 32.25):
                                        if (bmi > 34.3):
                                            if (bmi > 36.45):
                                                if (diabetes_pedigree > 0.6515):
                                                    return u'True'
                                                if (diabetes_pedigree <= 0.6515):
                                                    return u'False'
                                            if (bmi <= 36.45):
                                                return u'False'
                                        if (bmi <= 34.3):
                                            if (diabetes_pedigree > 0.57):
                                                if (bmi > 33.75):
                                                    return u'True'
                                                if (bmi <= 33.75):
                                                    return u'False'
                                            if (diabetes_pedigree <= 0.57):
                                                return u'True'
                                    if (bmi <= 32.25):
                                        return u'False'
                                if (bmi <= 31.4):
                                    return u'True'
                        if (diabetes_pedigree <= 0.48974):
                            if (glucose > 142):
                                if (diabetes_pedigree > 0.295):
                                    return u'True'
                                if (diabetes_pedigree <= 0.295):
                                    return u'False'
                            if (glucose <= 142):
                                if (insulin is None):
                                    return u'False'
                                if (insulin > 36):
                                    return u'False'
                                if (insulin <= 36):
                                    if (glucose > 94):
                                        if (bmi > 33.25):
                                            if (age > 25):
                                                return u'False'
                                            if (age <= 25):
                                                if (pregnancies is None):
                                                    return u'True'
                                                if (pregnancies > 1):
                                                    if (bmi > 35.85):
                                                        return u'True'
                                                    if (bmi <= 35.85):
                                                        return u'False'
                                                if (pregnancies <= 1):
                                                    return u'True'
                                        if (bmi <= 33.25):
                                            return u'False'
                                    if (glucose <= 94):
                                        return u'False'
            if (bmi <= 31.15208):
                if (pregnancies is None):
                    return u'False'
                if (pregnancies > 2):
                    if (glucose > 118):
                        if (bmi > 28.5):
                            return u'False'
                        if (bmi <= 28.5):
                            return u'True'
                    if (glucose <= 118):
                        if (bmi > 30.95):
                            return u'True'
                        if (bmi <= 30.95):
                            if (diabetes_pedigree is None):
                                return u'False'
                            if (diabetes_pedigree > 0.652):
                                if (bmi > 25.25):
                                    return u'False'
                                if (bmi <= 25.25):
                                    return u'True'
                            if (diabetes_pedigree <= 0.652):
                                return u'False'
                if (pregnancies <= 2):
                    if (glucose > 132):
                        if (bmi > 28.8):
                            if (bmi > 29.5):
                                return u'False'
                            if (bmi <= 29.5):
                                return u'True'
                        if (bmi <= 28.8):
                            return u'False'
                    if (glucose <= 132):
                        return u'False'
