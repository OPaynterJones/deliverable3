import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
import numpy as np

def train():
    data_file = 'data.csv'
    try:
        #check if file is accessible
        print(f"data.csv file found: {os.path.isfile(data_file)}")
        data = pd.read_csv(data_file)
    except Exception as e:
        return (f"file not found, error: \n {e}")
        
    
    interest_groups_col = data.iloc[:,-1]
    interest_list = ["ABACUS","Badminton","Basketball","Bath City FC soc","Boxing","Computer Science soc","Cricket","Cue sports","Cycling","Dance","Data science","Debate","Drum and Bass","Fashion","Finance","Fine art","Gin soc","Golf","Green Party","Hockey","Jiu Jitsu","Lacrosse","Left Union","Model UN","Music soc","Netball","Poker","Politics","Powerlifting","Rowing","Rugby union","Sailing","Salsa","Squash","Student Theatre","Swimming","Table Tennis","Triathlon","Urban Dance","Water polo"]
    # Remove the first column
    X = data.iloc[:, 1:]
    X = X.iloc[:, :70]

    #X[X <= 5] = 1
    #X[X > 5] = 10

    #last_row = data.iloc[-1, 1:71]  # Exclude the first column (assuming it's not needed for prediction)
    #last_row = last_row.values.reshape(1, -1)


    cleaned_data = []
    for interest_groups_entry in interest_groups_col:
        interests = [x.strip() for x in interest_groups_entry.split(',')]  # Assuming interests are comma-separated
        new_data = np.zeros(len(interest_list))
        for interest in interests:
            if interest in interest_list:
                new_data[interest_list.index(interest)] = 1
        cleaned_data.append(new_data)

    print(X.iloc[0])



    base_regressor = RandomForestRegressor()
    multi_output_regressor = MultiOutputRegressor(base_regressor)
    multi_output_regressor.fit(X, cleaned_data)

    """
    interests_vector = Take user interests from database
    predicted_societies = multi_output_regressor.predict(interests_vector)
    """
    interest_vector = np.array([[7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4, 6, 3, 8, 1, 5, 10, 3, 7, 2, 9, 4]])
    
    np.reshape(interest_vector, (-1,1))
    print(interest_vector.shape)
    predicted_societies = multi_output_regressor.predict(interest_vector)

    predictions = [(interest_list[i], val) for i, val in enumerate(predicted_societies[0])]
    predictions.sort(key=lambda x: x[1], reverse=True)

    print(predictions)

    #last_row = data.iloc[-1, 1:71].values.reshape(1, -1)
    #last_row[last_row <= 5] = 3
    #last_row[last_row > 5] = 8

    #predicted_interests = multi_output_regressor.predict(last_row)

    # Format the predictions
    #last_row_predictions = [(interest_list[i], val) for i, val in enumerate(predicted_interests[0])]
    #last_row_predictions.sort(key=lambda x: x[1], reverse=True)

    #print("Predicted interest groups for the last row:")
    #print(last_row_predictions)
print(train())