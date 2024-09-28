import pickle
import streamlit as st
from datetime import datetime
import math
import re

# Load pre-trained models
loaded_model1 = pickle.load(open('model1_pipe_cv.pkl','rb'))
loaded_model2 = pickle.load(open('model2_pipe_cv.pkl','rb'))
loaded_model3 = pickle.load(open('model3_pipe_cv.pkl','rb'))
loaded_model4 = pickle.load(open('model4_pipe_cv.pkl','rb'))

total_departments = 24  # Total number of departments in the company


# Function to preprocess input for the first model
def preprocess_input_1(duration_hours, start_date, end_date, order_intake_value):
    duration_days = (end_date - start_date).days
    if duration_days == 0:
        # Handle the case where duration_days is zero, maybe by setting a default value or raising an exception
        raise ValueError("Duration cannot be zero.")
    else:
        work_intensity = duration_hours / duration_days
        return [[duration_hours, duration_days, order_intake_value, work_intensity]]


# Function to preprocess input for the second model
def preprocess_input_2(duration_hours, duration_days, order_intake_value, output_1):
    print("duration_hours, duration_days, order_intake_value, output_1",duration_hours, duration_days, order_intake_value, output_1)
    work_intensity = duration_hours / duration_days
    department_diversity = output_1 / total_departments
    average_work_quantity_per_department = duration_hours / output_1
    print("duration_hours, order_intake_value, duration_days, work_intensity, department_diversity, average_work_quantity_per_department, output_1",duration_hours, order_intake_value, duration_days, work_intensity, department_diversity, average_work_quantity_per_department, output_1)
    return [[duration_hours, order_intake_value, duration_days, work_intensity, department_diversity, average_work_quantity_per_department, output_1]]

# Function to preprocess input for the third model
def preprocess_input_3(duration_hours, total_order_intake, duration_days, num_of_departments, predicted_indices):
    print("Output1", num_of_departments)
    work_intensity = duration_hours / duration_days
    department_diversity = num_of_departments / total_departments
    average_work_quantity_per_department = duration_hours / total_order_intake
    input_data = [duration_hours, total_order_intake, duration_days, work_intensity, department_diversity, average_work_quantity_per_department]
    input_data.extend(predicted_indices)  # Append the predicted indices to the input data
    input_data.append(num_of_departments)
    return [input_data]

# Function to preprocess input for the fourth model
def preprocess_input_4(duration_hours, total_order_intake, duration_days, num_of_employees, predicted_indices, num_of_departments):
    print("Output1", num_of_departments)
    work_intensity = duration_hours / duration_days
    average_work_quantity_per_department = duration_hours / total_order_intake
    duration_to_employees_ratio = duration_days / num_of_employees
    department_diversity = num_of_departments / total_departments
    input_data = [duration_hours, total_order_intake, duration_days, num_of_employees,
                duration_to_employees_ratio, work_intensity, department_diversity,
                average_work_quantity_per_department]
    input_data.extend(predicted_indices)  # Append the predicted indices to the input data
    input_data.append(num_of_departments)
    return [input_data]



#####################################################################################################################################################################

# Function to make prediction using the first model
def predict_department_count(input_data):
    return loaded_model1.predict(input_data)[0]

department_columns = ['ARCHITECTURAL', 'COMMERCIAL', 'COMMISSIONING', 'CONSULTING', 'DATA & SECURITY', 'DESIGN MANAGEMENT', 'DEVELOPMENT', 'DOCUMENT CONTROL', 'ELECTRICAL', 'ESTIMATING', 'INDUSTRIAL MAINTENANCE', 'MANAGEMENT', 'MANAGEMENT & ADMIN', 'MANAGEMENT ACCOUNTS', 'MECHANICAL', 'OPERATIVE', 'PLANNING', 'PROCESS', 'PROCUREMENT', 'PROJECT MANAGEMENT', 'QUALITY, SAFETY & ENVIRONMENT', 'SERVICES', 'TECHNICAL', 'VALIDATION & REGULATORY AFFAIRS']

# Function to make prediction using the second model
def predict_department_names(input_data):
    predicted_indices = loaded_model2.predict(input_data)
    predicted_names = []
    for prediction in predicted_indices:
        names = [department_columns[i] for i, val in enumerate(prediction) if val == 1]
        predicted_names.extend(names)    
    predicted_names = "\n".join([f"{idx+1}. {name}" for idx, name in enumerate(predicted_names)])
    return predicted_names, predicted_indices

# Function to make prediction using the third model
def predict_total_employees(input_data):
    return loaded_model3.predict(input_data)[0]

# Function to make predictions using the 4th model
def predict_department_employees(input_data):
    predicted_employees = loaded_model4.predict(input_data)
    rounded_employees = [math.ceil(employees) for employees in predicted_employees[0]]
    
    non_zero_departments = [(department_columns[i], rounded_employees[i]) for i in range(len(rounded_employees)) if rounded_employees[i] != 0]
    formatted_output = "\n".join([f"{idx+1}. {department}: {employees}" for idx, (department, employees) in enumerate(non_zero_departments)])
    
    return formatted_output


#####################################################################################################################################################################
def set_background(image_url):
    """
    Sets the background of the app to the specified image.
    
    Parameters:
        image_url (str): The URL or local file path of the image.
    """
    page_bg_img = '''
    <style>
    body {
    background-image: url("%s");
    background-size: cover;
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
# Main function
def main():

    # Set the background image
    set_background('custom_background_image.jpg')
    
    st.title('🏗️ Dynamic Resource Planning Tool for Construction Projects 🏗️')
    st.markdown("---")

    # Input variables
    try:
        with st.container():
            st.write("### Upcoming Project/Client Name")
            project_name = st.text_input('', placeholder="Enter project name")
            if not re.match(r'^[A-Za-z0-9\s-]*$', project_name):
                raise ValueError("Project name can only contain letters, numbers, spaces, and hyphens.")
        
        with st.container():
            st.write("### Order Intake (Cost in '000 EUR)")
            order_intake_value = st.number_input('',value=None, placeholder="Enter order intake value")
            
        with st.container():
            st.write("### Duration (Project Hours)")
            duration_hours = st.number_input('',value=None, placeholder="Enter project duration")
            
        with st.container():
            st.write("### Start Date (YYYY/MM/DD)")
            start_date = st.date_input('',key="start_date")
            
        with st.container():
            st.write("### End Date (YYYY/MM/DD)")
            end_date = st.date_input('',key="end_date")
            
    except ValueError as e:
        st.error(str(e))
        return

        
    # Validate project name
    if project_name and not re.match(r'^[A-Za-z0-9\s]*$', project_name):
        st.error("Project name can only contain alphabets, numbers, and spaces.")
        return

    # Convert number inputs to float
    order_intake_value = float(order_intake_value) if order_intake_value is not None else None
    duration_hours = float(duration_hours) if duration_hours is not None else None
    
    if duration_hours is None or order_intake_value is None or start_date is None or end_date is None:
        st.error('Please fill in all the input fields.')
        return
    
    if duration_hours <= 0 or order_intake_value <= 0:
        st.error('Duration and Order Intake value must be greater than zero.')
        return
    
    if start_date >= end_date:
        st.error('Start date must be before the end date.')
        return
    
    try:
        input_data_1 = preprocess_input_1(duration_hours, start_date, end_date, order_intake_value)
    except ValueError as e:
        st.error(str(e))
        return
    
    output_1 = predict_department_count(input_data_1)
    
    input_data_2 = preprocess_input_2(duration_hours, input_data_1[0][1], order_intake_value, output_1)
    print("input_data_2: ", input_data_2)
    predicted_names, predicted_indices = predict_department_names(input_data_2)
    print("predicted_names: ", predicted_names)
    print("predicted_indices: ", predicted_indices)
    
    input_data_3 = preprocess_input_3(duration_hours, order_intake_value, input_data_1[0][1], output_1, predicted_indices[0])
    total_employees = predict_total_employees(input_data_3)
    
    input_data_4 = preprocess_input_4(duration_hours, order_intake_value, input_data_1[0][1],total_employees, predicted_indices[0],output_1)
    department_employees = predict_department_employees(input_data_4)
    
    # Create a container to hold the buttons and outputs
    buttons_container = st.container()

    # Predict department count
    with buttons_container:
        st.markdown('<style>div.stButton > button:first-child { width: 100% !important; background: linear-gradient(to right, #000000, #333333, #000000); color: #FFFFFF; font-size: 16px; font-weight: bold; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; transition: background 0.3s; }</style>', unsafe_allow_html=True)
        if st.button('Predict Department Count'):
            st.success('Number of predicted departments for the project are {}'.format(output_1))

    # Predict department names
    with buttons_container:
        st.markdown('<style>div.stButton > button:first-child { width: 100% !important; background: linear-gradient(to right, #000000, #333333, #000000); color: #FFFFFF; font-size: 16px; font-weight: bold; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; transition: background 0.3s; }</style>', unsafe_allow_html=True)
        if st.button('Predict Department Names'):
            if output_1 is None:
                st.error('Please predict department count first.')
            else:
                st.success('Predicted department names are: \n{}'.format(predicted_names))
                if output_1 > len(predicted_names.split('\n')):
                    st.warning('**Attention:** The model is only classifying the minimum predicted number of employees per department. This minimum value results from significant data imbalances across departments. To improve the accuracy and generalization of predictions, additional departmental data is required.')

    # Predict Total Number of Employees for the new project
    with buttons_container:
        st.markdown('<style>div.stButton > button:first-child { width: 100% !important; background: linear-gradient(to right, #000000, #333333, #000000); color: #FFFFFF; font-size: 16px; font-weight: bold; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; transition: background 0.3s; }</style>', unsafe_allow_html=True)
        if st.button('Predict Total Number of Employees for the new project'):
            total_employees_rounded = round(total_employees)
            st.success('Total number of predicted employees for the new project are {}'.format(total_employees_rounded))

    # Predict Number of Employees in Each Department
    with buttons_container:
        st.markdown('<style>div.stButton > button:first-child { width: 100% !important; background: linear-gradient(to right, #000000, #333333, #000000); color: #FFFFFF; font-size: 16px; font-weight: bold; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; transition: background 0.3s; }</style>', unsafe_allow_html=True)
        if st.button('Predict Number of Employees in Each Department'):
            st.success('Predicted number of employees in each department of the New Project:\n{}'.format(department_employees))
            if len(department_employees.split('\n')) > total_departments:
                st.warning('**Attention:** The model is only classifying the minimum predicted number of employees per department. This minimum value results from significant data imbalances across departments. To improve the accuracy and generalization of predictions, additional departmental data is required.')

    # Important Note Dialog Box
    st.warning('**Attention:** The model predictions are based on the minimum predicted number of employees per department. This minimum value results from significant data imbalances across departments. To improve the accuracy and generalization of predictions, additional departmental data is required')

            
    # Resource Planning Summary Button
    with buttons_container:
        st.markdown('<style>div.stButton > button:first-child { width: 100% !important; background: linear-gradient(to right, #000000, #333333, #000000); color: #FFFFFF; font-size: 16px; font-weight: bold; padding: 14px 20px; margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; transition: background 0.3s; }</style>', unsafe_allow_html=True)
        if st.button('Resource Planning Summary for {}'.format(project_name)):
            # Generate resource planning summary
            summary = f"Project Name: {project_name}\n"
            summary += f"\nNumber of predicted departments: \n{output_1}\n"
            summary += f"\nPredicted department names:\n{predicted_names}\n"
            summary += f"\nTotal number of predicted employees: {int(total_employees)}\n"
            summary += f"\nPredicted number of employees in each department:\n{department_employees}"
            st.info(summary)


if __name__ == '__main__':
    main()