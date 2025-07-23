import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from lightgbm import LGBMRegressor

# 1. Load data
df = pd.read_csv("data/transformed_data.csv")
X = df.drop(columns="Delayed")
y = df["Delayed"]
df['Date'] = pd.to_datetime(data['Date'])
df['Month'] = df['Date'].dt.month
df['Hour'] = df['Time'].apply(lambda x: int(x.split(':')[0]))
df['Minute'] = df['Time'].apply(lambda x: int(x.split(':')[1]))
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Delayed'] = df['Min Delay'] > 0

# 2. Define column groups
label_encoders = {} # A Mapping between categorical variables and their encoded values
for column in ['Station', 'Bound', 'Line']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = dict(zip(le.classes_, le.transform(le.classes_)))

print(label_encoders)
print(df.head())

numeric_cols = ["Hour", "DayOfWeek", "Month", "Minute"]
categorical_cols = ["station_id_enc", "line_id_enc"]

# 3. Build transformers
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="constant", fill_value="missing")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_cols),
    ("cat", categorical_pipeline, categorical_cols)
])

# 4. Full pipeline: preprocessing + model
pipeline = Pipeline([
    ("prep", preprocessor),
    ("model", LGBMRegressor(random_state=42))
])

# 5. Time-based cross-validation + grid search
tscv = TimeSeriesSplit(n_splits=5)
param_grid = {
    "model__n_estimators": [100, 300],
    "model__learning_rate": [0.01, 0.05],
    "model__num_leaves": [31, 63]
}

grid = GridSearchCV(
    pipeline,
    param_grid,
    cv=tscv,
    scoring="neg_root_mean_squared_error",
    n_jobs=-1,
    verbose=1
)

# 6. Fit and evaluate
grid.fit(X, y)
print("Best score:", -grid.best_score_)
print("Best params:", grid.best_params_)