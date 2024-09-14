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

#Define a function to predict diamond prices

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
    
    age = st.number_input("age", min_value=15, max_value=22, value=18, step=1)
    
    Fedu_options = ["none",
                   "primary education (4th grade)",
                   "5th to 9th grade",
                   "secondary education",
                   "higner education"]
    Fedu = st.selectbox("Fedu", Fedu_options, index=Fedu_options.index("none"))
    
    Mjob_options = ["teacher", "health", "services", "at_home", "other"]
    Mjob = st.selectbox("Mjob", Mjob_options, index=Mjob_options.index("at_home"))
    
    reason_options = ['home', 'reputation', 'course' , 'other']
    reason = st.selectbox("reason", reason_options, index=reason_options.index("home"))
    
    studytime_options = ["<2 hours", "2 to 5 hours"," 5 to 10 hours", ">10 hours"]
    studytime = st.selectbox("studytime", studytime_options, index=studytime_options.index("<2 hours"))
    
    failures = st.number_input("failures", min_value=1, max_value=4, value=1, step=1)
    
    studytime
    
    schoolsup_options = ['yes', 'no']
    schoolsup = st.selectbox("schoolsup", schoolsup_options, index=schoolsup_options.index("yes"))
                             
    activities_options = ['yes', 'no']
    activities = st.selectbox("activities", activities_options, index=activities_options.index("yes"))
    
    nursery_options = ['yes', 'no']
    nursery = st.selectbox("nursery", nursery_options, index=nursery_options.index("yes"))
                        
    internet_options = ['yes', 'no']
    internet = st.selectbox("internet", internet_options, index=internet_options.index("yes"))

    romantic_options = ['yes', 'no']
    romantic = st.selectbox("romantic", romantic_options, index=romantic_options.index("yes"))
      
    famrel_options = ['very bad', 'bad', 'normal', 'good', 'excellent']
    famrel = st.selectbox("famrel", famrel_options, index=famrel_options.index("normal"))
    
    health_options = ['very bad', 'bad', 'normal', 'good', 'very good']
    health = st.selectbox("famrel", health_options, index=health_options.index("normal"))
                          
    absences = st.number_input("absences", min_value=0, max_value=93, value=0, step=1)

    G1 = st.number_input("G1", min_value=0, max_value=20, value=0, step=1)                    
    
    G2 = st.number_input("G2", min_value=0, max_value=20, value=0, step=1)
    
    # Initialize the result string
    result_str = ""
    
    # Button (if true then next line)
    if st.button("Predict"):
        
        #Convert user choices from selectbox to numeric values
        sex =   sex_options.index( sex)
        
        Fedu = Fedu_options.index(Fedu)
        
        Mjob = Mjob_options.index(Mjob)
        
        reason =  reason_options.index(reason)
        
        studytime = studytime_options.index(studytime)
        studytime = studytime+1
        
        schoolsup = schoolsup_options.index(schoolsup)
        
        activities =  activities_options.index(activities)
        
        nursery = nursery_options.index(nursery)
        
        internet = internet_options.index(internet)
        
        romantic = romantic_options.index(romantic)
        
        famrel =  famrel_options.index(famrel)
        famrel = famrel+1
        
        health = health_options.index(health)
        health = health+1

    
        #Call function and assign to variable result
        result = predict_studentPerformance(G2, absences, age, famrel, health,
                                            Mjob, reason, G1, studytime, Fedu,
                                            schoolsup, activities, failures,
                                            romantic, sex, nursery, internet)
    
        # Convert the result to a string and remove square brackets
        result_str = str(result).strip('/')

    # Output dsplay result
    st.write('The performace of the student is ${}. '.format(result_str))
    
    
if __name__== '__main__':
    main()