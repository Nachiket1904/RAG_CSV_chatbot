import streamlit as st
import fpdf
from io import BytesIO


class Layout:
    
    def show_header(self, types_files):
        """
        Displays the header of the app
        """
        st.markdown(
            f"""
            <h1 style='text-align: center;'> Ask Datamingle about your {types_files} files ! 😁</h1>
            """,
            unsafe_allow_html=True,
        )

    def show_api_key_missing(self):
        """
        Displays a message if the user has not entered an API key
        """
        st.markdown(
            """
            <div style='text-align: center;'>
                <h4>Enter your <a href="https://platform.openai.com/account/api-keys" target="_blank">OpenAI API key</a> to start chatting</h4>
            </div>
            """,
            unsafe_allow_html=True,
        )

    
    def prompt_form(self):
        """
        Displays the prompt form
        """
        with st.form(key="my_form", clear_on_submit=True):
            user_input = st.text_area(
                "Query:",
                placeholder="Ask me anything about the document...",
                key="input",
                label_visibility="collapsed",
            )
            submit_button = st.form_submit_button(label="Send")
            
            is_ready = submit_button and user_input
        return is_ready, user_input
    

    def export_assistant_replies_to_pdf(self, assistant_msgs, filename="RecentAssistantReplies.pdf"):
        """
        Exports the most recent assistant message to a PDF document in memory
        and allows direct download within the Streamlit app.
        """

        pdf = fpdf.FPDF()
        try:
            # Attempt to embed DejaVuSans font (if available)
            pdf.add_font('DejaVuSans', '', 'DejaVuSans.ttf', uni=True)
            pdf.set_font("DejaVuSans", size=12)
        except OSError:
            # Handle font not found error
            st.error("DejaVuSans.ttf font not found. Using Helvetica (may not support emojis).")
            pdf.set_font("helvetica", size=12)

        pdf.add_page()
        pdf.cell(0, 10, ln=2)

        # Get the most recent assistant message (assuming assistant_msgs is a list)
        recent_msg = assistant_msgs[-1]  # Access the last element

        pdf.write(5, recent_msg)

        # Create a BytesIO object to store the PDF in memory
        pdf_output = BytesIO()
        pdf.output(pdf_output)

        # Download the PDF directly within Streamlit
        st.download_button(label="Download Recent Assistant Reply",
                          data=pdf_output.getvalue(),
                          file_name=filename,
                          mime="application/pdf")

