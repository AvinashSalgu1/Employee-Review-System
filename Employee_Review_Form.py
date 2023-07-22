import streamlit as st
import pandas as pd

def main():
    st.set_page_config(initial_sidebar_state="collapsed")
    st.title("Employee Review Form")
    Employee_df = pd.read_csv("cs_Employee.csv")
    Employee_name = st.selectbox("Select your Employee", Employee_df["Name"].tolist())
    Employee_id = Employee_df[Employee_df["Name"] == Employee_name]["EmployeeID"].values[0]
    st.code(f"Designation: {Employee_df[Employee_df['Name'] == Employee_name]['Designation'].values[0]}",
            language="markdown")
    feedback_df = pd.read_csv("cs_feedback.csv")
    review_already_exists = review_already_exists = (feedback_df["EmployeeID"] == Employee_id).any()

    if not review_already_exists:
        st.write("")
        st.write("")
        widget1_placeholder, widget2_placeholder, widget3_placeholder, widget4_placeholder, widget5_placeholder, \
            widget6_placeholder, widget7_placeholder, widget8_placeholder, widget9_placeholder, widget10_placeholder \
            = [st.empty() for _ in range(10)]
        widget_placeholder_list = [widget1_placeholder, widget2_placeholder, widget3_placeholder, widget4_placeholder,
                                   widget5_placeholder, widget6_placeholder, widget7_placeholder, widget8_placeholder,
                                   widget9_placeholder, widget10_placeholder]
        st.write()
        widget1_placeholder.code("Ratings\n1 - Unsatisfactory\n2 - Needs Improvement\n3 - Average\n4 - Good\n5 - "
                                 "Excellent\n", language="markdown")

        r1 = widget2_placeholder.select_slider("Job Peformance", range(1, 6), value=3)
        r2 = widget3_placeholder.select_slider("Skills and Competencies", range(1, 6), value=3)
        r3 = widget4_placeholder.select_slider("Initiative and Innovation", range(1, 6), value=3)
        r4 = widget5_placeholder.select_slider("Reliability and Dependability", range(1, 6), value=3)
        r5 = widget6_placeholder.select_slider("Collaboration and Teamwork", range(1, 6), value=3)
        r6 = widget7_placeholder.select_slider("Professionalism and Ethics", range(1, 6), value=3)
        r7 = widget8_placeholder.select_slider("Continuous Learning and Development", range(1, 6), value=3)
        comment = widget9_placeholder.text_area("comment", label_visibility="hidden",
                                                placeholder="Please share your feedback")
        submit_button = widget10_placeholder.button("SUBMIT")

        if submit_button:
            if comment != "":
                feedback_df = pd.read_csv("cs_feedback.csv")
                feedback_df.loc[len(feedback_df)] = \
                    [Employee_df[Employee_df['Name'] == Employee_name]['EmployeeID'].values[0],
                     comment.replace("\n", " "), r1, r2, r3, r4, r5, r6, r7]
                feedback_df.to_csv("cs_feedback.csv", index=False)

                for widget_placeholder in widget_placeholder_list:
                    widget_placeholder.empty()

                st.info("Review submitted successfully")
                st.experimental_rerun()
            else:
                st.error("Feedback not entered")
    else:
        st.write("")
        st.code("Review submitted", language="markdown")


if __name__ == "__main__":
    main()
