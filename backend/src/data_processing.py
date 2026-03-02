from sklearn.datasets import fetch_california_housing   
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 

def load_data():
    # This set is already cleaned, no need to do anything but load
    # Features: ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    dataset = fetch_california_housing(as_frame=True)
    df = dataset.frame 
    return df

def scale_features(X_train, X_test):
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler

def split_data(df):
    x = df.drop("MedHouseVal", axis=1)
    y = df["MedHouseVal"]

    return train_test_split(
            x, y, 
            test_size=0.2,
            random_state=42
            )

def preprocess_data():
    '''
    Load and split the data into test and training sets
    '''
    df = load_data()

    X_train, X_test, y_train, y_test = split_data(df)
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train,X_test)

    return X_train_scaled, X_test_scaled, y_train.values, y_test.values, scaler
