# Resource Planning for Construction Projects

This project is a collaboration with **EQUANS**, a leading construction company, to develop a **Human Resource Allocation Management System**. The project aims to predict and optimize staffing resources for construction projects in the UK, using machine learning models. This system helps improve resource allocation accuracy, reduce over-allocation, and enhance project efficiency.

## Project Overview

This project involves the application of machine learning techniques to solve the problem of resource planning in construction. The developed tool forecasts the resource needs for different roles (e.g., engineers, project managers, mechanical supervisors) and automates planning tasks, leading to significant savings in time and cost.

**Key Features:**
- **Resource Optimization**: Predicts staffing requirements to improve resource allocation and efficiency.
- **Real-time Adjustment**: Flexible adjustment of predictions based on the latest project data.
- **Decision Support**: Provides decision-makers with actionable insights into staffing and resource allocation.

## Data Overview

| Feature                          | Description                                           |
|-----------------------------------|-------------------------------------------------------|
| `Duration_hours`                  | Total hours allocated to a project.                   |
| `Total_order_intake`              | Total value or volume of orders received.             |
| `Num_of_Departments`              | Number of departments involved in a project.          |
| `Duration_days`                   | Total duration from start to project completion.      |
| `Number_of_JobTitles`             | Count of distinct job titles in the project.          |
| `Num_of_Employees`                | Total number of employees allocated.                  |
| `Work_Intensity`                  | Intensity of work per day.                            |
| `Average_Work_Quantity_per_Task`  | Average hours expected for each task.                 |

## Methodology

Several machine learning models were used for prediction and classification tasks, including Random Forest Classifier and Multi-Output Classifiers. Oversampling was applied to handle data imbalances, and hyperparameter tuning improved the model's performance.

The methodology for this project included:

1. **Data Collection and Pre-processing**
   - Merged employee timesheet and customer order datasets.
   - Handled duplicates and performed feature engineering to enhance data quality.
   - Used random oversampling to address data imbalance.

2. **Exploratory Data Analysis (EDA)**
   - Analyzed data distributions and relationships to identify key features influencing resource allocation.

3. **Model Development**
   - **Model 1:** Random Forest for predicting department counts, achieving 94.44% testing accuracy.
   - **Model 2:** Multi-output classifier for department name classification, with a test accuracy of 92%.
   - **Model 3:** Total staff count prediction using Random Forest, reaching an F1 score of 99%.
   - **Model 4:** Department-wise staff allocation prediction, obtaining an R-squared value of 0.99.

4. **Model Deployment**
   - Developed an interactive resource planning tool using Streamlit for user-friendly access to predictions.

5. **Validation and Performance Evaluation**
   - Evaluated model performance with metrics like accuracy, F1 score, and R-squared to ensure reliability.


## Results & Outcomes
- Achieved high accuracy in department count and staff allocation predictions.
- Developed a user-friendly resource planning tool using Streamlit for model deployment.

- **Resource Allocation Accuracy**: Improved by **20%**.
- **Overallocation Reduction**: Decreased by **15%**.
- **Project Delivery Timelines**: Enhanced by **10%**.
- **Planning Time and Cost**: Reduced by **20%**.

## Project Structure
```
P18_Equans_Code_Repository/
│
├── main_code.ipynb       # Main code for data analysis and modeling
├── model1_pipe_cv.pkl     # Pickle file for Model 1
├── model2_pipe_cv.pkl     # Pickle file for Model 2
├── model3_pipe_cv.pkl     # Pickle file for Model 3
├── model4_pipe_cv.pkl     # Pickle file for Model 4
├── optuna_study_model2.pkl # Optuna study results for Model 2
├── streamlitapi           # Streamlit application for resource planning
├── study.pkl              # Study-related data
├── study_model4.pkl       # Pickle file for Model 4 study
└── 2021-2023 Orders Report_Client Level.xlsx # Client-level orders report
└── requirements.txt # necessary dependencies
  ```
---
## Streamlit Application
The project has been deployed using **Streamlit** for interactive user access. Users can input project details to forecast department count, staff names, and employee allocations.

## Screenshots of Stremlit Application
![image](https://github.com/user-attachments/assets/df362b55-7a7b-4286-bb55-6172f38a82cb)

![image](https://github.com/user-attachments/assets/f18a85a8-7dc8-4e7b-9e2c-50fd749d512b)




---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resource-planning-equans.git
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run stremlitapi.py
   ```

## Acknowledgments
- Equans for the opportunity to work on this innovative project.

## License

```
This project is licensed for review and reference only. No permission is granted to copy, use, or modify the code.
```
