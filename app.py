import streamlit as st
import pandas as pd

# Load sample data
df = pd.read_csv('survey_data_with_discrepancies.csv')

# Show only flagged responses
flagged_df = df[df['Flagged']]

# Dashboard title
st.title("NPS Score and Comment Discrepancy Dashboard")

# Display flagged responses
st.subheader("Flagged Responses for Review")
st.write(flagged_df)

# Allow user to correct flagged responses
st.subheader("Correct the NPS Scores")

# Create a form to correct flagged responses
for index, row in flagged_df.iterrows():
    new_score = st.slider(f"Correct NPS for Comment: '{row['Comment']}'", 0, 10, int(row['NPS_Score']))
    if new_score != row['NPS_Score']:
        flagged_df.at[index, 'NPS_Score'] = new_score
        st.write(f"Updated NPS Score for '{row['Comment']}' to {new_score}")

# Save the corrected data
if st.button("Save Corrections"):
    df.update(flagged_df)
    df.to_csv('corrected_survey_data.csv', index=False)
    st.success("Corrections saved successfully!")

# Display corrected data
st.subheader("Corrected Data")
st.write(df)
# End