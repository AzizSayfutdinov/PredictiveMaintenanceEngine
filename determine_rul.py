#remain useful lifetime calculation
import numpy as np

def determine_rul(y_pred, y_test, X_test, test, period):
    id_test = np.reshape(np.array(test['id']),((X_test.shape[0],1)))
    Y_pred_id = np.hstack((id_test, np.reshape(np.array(y_pred),((y_test.shape[0],1))))) #add id to prediction
    rul_pred = np.zeros((Y_pred_id.shape[0]))
    rul_akt = period #Remain useful lifetime start
    for i in range (1, Y_pred_id.shape[0]-1):
        if Y_pred_id[i, 0] > Y_pred_id[i-1,0] :
            rul_akt = period
        else:
            rul_akt = rul_akt - Y_pred_id[i, 1]
        rul_pred[i] = rul_akt

    # get rul for the last element of id cycle
    list_periods = []
    for i in range(0, len(test)):
        if i + 1 < len(test):
            if test['cycle'][i] > test['cycle'][i + 1]:
                list_periods.append(test['cycle'][i])
        else:
            list_periods.append(test['cycle'][i])

    index = 0
    rul_pred_list = []
    for i in range(0, len(list_periods)):
        index = index + list_periods[i]
        rul_pred_list.append(rul_pred[index - 1])
    
    return rul_pred_list