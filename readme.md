# Coronary Artery Disease (CAD) Prediction Model

Welcome to the Coronary Artery Disease (CAD) Prediction Model repository. This project leverages tree-based ensemble learning methods to develop a predictive model for CAD and provides a user-friendly web application for clinicians to easily input patient data and obtain CAD predictions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Clinical Application](#clinical-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

The study developed a predictive model for angiographic Coronary Artery Disease (CAD) using an extensive dataset from the IEEE Data Port. Tree-based ensemble learning methods, including Random Forest, Gradient Boosting Machine (GBM), Extreme Gradient Boosting Machine (XGBM), Light Gradient Boosting Machine (LGBM), AdaBoost, and CatBoost, were compared using repeated random train-test splits to ensure consistency. A meta-model was created by combining these models using the stacking method, and a web application was developed using Streamlit.

## Features

- Multiple tree-based ensemble learning methods.
- Stacking ensemble model for improved predictive performance.
- User-friendly web application for clinicians to input patient data and obtain CAD predictions.
- Immediate visual feedback on the predicted likelihood of CAD.
- Potential cost-effective alternative to traditional diagnostic methods such as angiography.

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CAD-Prediction-Model.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CAD-Prediction-Model
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit application in your web browser.
2. Provide the necessary patient data inputs in the provided fields.
3. Click the "Predict" button to obtain the CAD prediction and confidence level.

## Model

The predictive model utilizes the following tree-based ensemble learning methods:

- Random Forest
- Gradient Boosting Machine (GBM)
- Extreme Gradient Boosting Machine (XGBM)
- Light Gradient Boosting Machine (LGBM)
- AdaBoost
- CatBoost

The stacking ensemble model combines these methods for improved performance. The model was evaluated using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC curve.

## Clinical Application

The development of a user-friendly web application using Streamlit enabled clinicians to input patient data and obtain CAD predictions easily. The web application’s interface allows for the seamless entry of clinical parameters and provides immediate visual feedback on the predicted likelihood of CAD. This tool significantly aids clinicians in the decision-making process, potentially offering a cost-effective alternative to traditional diagnostic methods such as angiography.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features or improvements.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact [marunkumar1601@gmail.com].

