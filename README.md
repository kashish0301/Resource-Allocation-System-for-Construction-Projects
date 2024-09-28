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

### Models and Performance:

| Model                              | Training Accuracy | Test Accuracy | F1 Score  |
|-------------------------------------|-------------------|---------------|-----------|
| **Model 1**: Number of Departments  | 97.92%            | 91.66%        | 0.91      |
| **Model 2**: Department Names       | 100%              | 92%           | 0.99      |
| **Model 4**: Department-wise Staff  | 100%              | 99.5%         | 0.95      |

## Results

- **Resource Allocation Accuracy**: Improved by **20%**.
- **Overallocation Reduction**: Decreased by **15%**.
- **Project Delivery Timelines**: Enhanced by **10%**.
- **Planning Time and Cost**: Reduced by **20%**.

### Streamlit Application
The project has been deployed using **Streamlit** for interactive user access. Users can input project details to forecast department count, staff names, and employee allocations.

### Screenshots

Add screenshots of the Streamlit app or prediction results here to make the project more visual.

---

## Project Structure

```
P18_Equans_Code_Repository/
│
├── main_code/                    # Main code for the application
│   ├── stremlitapi.py            # Streamlit application script
│   ├── model1_pipe_cv.pkl        # Model 1 (Number of Departments)
│   ├── model2_pipe_cv.pkl        # Model 2 (Department Names)
│   ├── model3_pipe_cv.pkl        # Model 3 (Placeholder)
│   ├── model4_pipe_cv.pkl        # Model 4 (Department-wise Staff)
│   └── optuna_study_model2.pkl   # Optuna study model
│
├── data/                         # Data files (if applicable)
│   ├── orders_data.xlsx          # Orders data
│   └── timesheet_data.xlsx       # Timesheet data
│
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
└── LICENSE                        # License file
```

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

## Disclaimer

This repository is publicly available for recruiters to review my project work. The content is proprietary, and no one is permitted to use, copy, or modify the code for any other purpose.

---

## License

```
This project is licensed for review and reference only. No permission is granted to copy, use, or modify the code.
```
