import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

"""
Simulation based on Hultman, Kathman, and Shannon (2014), Beyond Keeping
Peace: United Nations Effectiveness in the Midst of Fighting. Inputs
for battle-related deaths, number of PKO troops deployed per month, total
PKO troops deployed, and the length of the PKO in months simulates the
predicted time until battle-related deaths hits 0.
""" 

st.write("""
# See how the deployment of PKO troops can decrease battle-related deaths.
""")

st.sidebar.header('User Input Parameters')


def user_input_features():
    """
    Define the variables that a user can adjust on the sidebar. Integers
    reflect the minimum, starting, and maximum values respectively
    """
    starting_brds = st.sidebar.slider("How many BRDs a currently \
                                      occuring per month? ", 25, 10000, 100)
    troop_rate = st.sidebar.slider("How many troops will be deployed \
                                   per month? ", 1, 1000, 1000)
    total_troops = st.sidebar.slider("How many total troops will be \
                                     deployed? ", 1, 1000000, 100000)
    num_months = st.sidebar.slider("How many months will the opperation \
                                   last? ", 1, 500, 100)
    data = {'starting_brds': starting_brds,
            'troop_rate': troop_rate,
            'total_troops': total_troops,
            'num_months': num_months}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


def deploy_pko_troops(df_input):
    """Defing the relationship between the values to be simulated"""
    starting_brds = int(df_input['starting_brds'])
    troop_rate = int(df_input['troop_rate'])
    total_troops = int(df_input['total_troops'])
    num_months = int(df_input['num_months'])
    brds = []
    months = 0
    month_array = []
    for i in range(num_months):
        num_troops = i * troop_rate
        if num_troops < total_troops and starting_brds > 0:
            # Hultman, Kathman, and Shannon find 10,000 troop reduce
            # BRDs by 6 per month
            effect_of_pko = num_troops * .0006
            starting_brds -= effect_of_pko
            months += 1
            brds.append(starting_brds)
            month_array.append(months)
            
        if num_troops >= total_troops and starting_brds > 0:
            effect_of_pko = total_troops * .0006
            starting_brds -= effect_of_pko
            months += 1
            brds.append(starting_brds)
            month_array.append(months)
            
        if starting_brds <= 0:
            print("\nBy deploying", str(troop_rate), "troops a month",
                  "\nuntil a total of", str(total_troops),
                  "troops are deployed, \nbattle-related deaths hit 0 after", 
                  str(months), "months")
            fig = plt.plot(month_array, brds)
            return months
     

def deploy_pko_troops_plot(df_input):
    """
    Create the plot to vizualize the predicted change in
    battle-related deaths over time
    """
    starting_brds = int(df_input['starting_brds'])
    troop_rate = int(df_input['troop_rate'])
    total_troops = int(df_input['total_troops'])
    num_months = int(df_input['num_months'])
    brds = []
    months = 0
    month_array = []
    for i in range(num_months):
        num_troops = i * troop_rate
        if num_troops < total_troops and starting_brds > 0:
            # Hultman, Kathman, and Shannon find 10,000 troop reduce
            # BRDs by 6 per month
            effect_of_pko = num_troops * .0006
            starting_brds -= effect_of_pko
            months += 1
            brds.append(starting_brds)
            month_array.append(months)
            
        if num_troops >= total_troops and starting_brds > 0:
            effect_of_pko = total_troops * .0006
            starting_brds -= effect_of_pko
            months += 1
            brds.append(starting_brds)
            month_array.append(months)
            
        if starting_brds <= 0:
            print("\nBy deploying", str(troop_rate), "troops a month",
                  "\nuntil a total of", str(total_troops),
                  "troops are deployed, \nbattle-related deaths hit 0 after", 
                  str(months), "months")
            return month_array, brds

prediction = deploy_pko_troops(df)

st.subheader('Prediction')
st.write("With these parameters, it will take", prediction,
         " months to reach 0 battle-related deaths")

brds_chart = deploy_pko_troops_plot(df)
st.line_chart(brds_chart[1])

# to run, open terminal and input `streamlit run app.py`
