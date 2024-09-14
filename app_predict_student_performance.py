# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:37:30 2024

@author: kingy
"""

#Libraries import pickle
import pickle
import streamlit as st

#Load the trained Randon Forest Regressor model 
pickle_in = open("RFR.pkl","rb")
RFR = pickle.load(pickle_in)

#Define a function to predict student performance

def predict_studentPerformance(G2, absences, age, famrel, health,
                               Mjob, reason, G1, studytime, Fedu,
                               schoolsup, activities, failures,
                               romantic, sex, nursery, internet):
    
    
    prediction=RFR.predict([[G2, absences, age, famrel, health,
                               Mjob, reason, G1, studytime, Fedu,
                               schoolsup, activities, failures,
                               romantic, sex, nursery, internet]]) 
    #print (prediction)
    return prediction

#Main application code
def main():

    # Application's background, color, title
    html_temp = """
    <div style="background-color:#c0f8a8 ;padding:10px">
    <h2 style="color:white; text-align:center;">Student Performance Prediction App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Allow the user to enter input
    sex_options = ["Male", "Female"]
    sex = st.selectbox("Sex", sex_options, index=sex_options.index("Male"))
    
    age = st.number_input("Age", min_value=15, max_value=22, value=18, step=1)
    
    Fedu_options = ["none",
                   "primary education (4th grade)",
                   "5th to 9th grade",
                   "secondary education",
                   "higner education"]
    Fedu = st.selectbox("Father's Education:", Fedu_options, index=Fedu_options.index("none"))
    
    Mjob_options = ["teacher", "health", "services", "at_home", "other"]
    Mjob = st.selectbox("Mother's job", Mjob_options, index=Mjob_options.index("at_home"))
    
    reason_options = ['home', 'reputation', 'course' , 'other']
    reason = st.selectbox("Reason To Choose This School", reason_options, index=reason_options.index("home"))
    
    studytime = st.number_input("Weekly Study Time", min_value=1, max_value=4, value=1, step=1)
    
    failures = st.number_input("Number Of Past Class Failures", min_value=1, max_value=4, value=1, step=1)
    
    schoolsup_options = ['yes', 'no']
    schoolsup = st.selectbox("Having Extra Educational Support", schoolsup_options, index=schoolsup_options.index("yes"))
                             
    activities_options = ['yes', 'no']
    activities = st.selectbox("Having Extra-Curricular Activities", activities_options, index=activities_options.index("yes"))
    
    nursery_options = ['yes', 'no']
    nursery = st.selectbox("Attended Nursery School ", nursery_options, index=nursery_options.index("yes"))
                        
    internet_options = ['yes', 'no']
    internet = st.selectbox("Internet Access At Home", internet_options, index=internet_options.index("yes"))

    romantic_options = ['yes', 'no']
    romantic = st.selectbox("Been With A Romantic Relationship", romantic_options, index=romantic_options.index("yes"))
    
    famrel = st.number_input("Family Relationship", min_value=1, max_value=5, value=1, step=1)
    
    health = st.number_input("Current Health Level", min_value=1, max_value=5, value=1, step=1)
                          
    absences = st.number_input("Number Of School Absences", min_value=0, max_value=93, value=0, step=1)

    G1 = st.number_input("Performance At First Period Grade", min_value=0, max_value=20, value=0, step=1)                    
    
    G2 = st.number_input("Performance At Second Period Grade", min_value=0, max_value=20, value=0, step=1)
    
    # Initialize the result string
    result_str = ""
    
    # Button (if true then next line)
    if st.button("Predict"):
        
        #Convert user choices from selectbox to numeric values
        sex =   sex_options.index(sex)
        
        Fedu = Fedu_options.index(Fedu)
        
        Mjob = Mjob_options.index(Mjob)
        
        reason =  reason_options.index(reason)
        
        schoolsup = schoolsup_options.index(schoolsup)
        
        activities =  activities_options.index(activities)
        
        nursery = nursery_options.index(nursery)
        
        internet = internet_options.index(internet)
        
        romantic = romantic_options.index(romantic)

    
        #Call function and assign to variable result
        result = predict_studentPerformance(G2, absences, age, famrel, health,
                                            Mjob, reason, G1, studytime, Fedu,
                                            schoolsup, activities, failures,
                                            romantic, sex, nursery, internet)
    
        # Convert the result to a string and remove square brackets
        result_str = str(result).strip('/')

    # Output dsplay result
    st.write('The performace of the student  at third period grade is ${}. '.format(result_str))
    
    
if __name__== '__main__':
    main()
