import streamlit as st

# Config
st.set_page_config(layout="wide", page_icon="💬", page_title="DataMingle | Chat-Bot by DataMango 🤖")

# Title
st.markdown(
    """
    <h2 style='text-align: center; color: #FFCD05;'>DataMingle, your data-aware assistant by Datamango 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")

# Description
st.markdown(
    """ 
    <h5 style='text-align:center; color: #000000;'>I'm DataMingle, an intelligent chatbot created by Datamango, combining the strengths of Cutting edge AI model Chatgpt. I use this technology to provide context-sensitive interactions. My goal is to help you better understand your data and make your life simple by analyzing that data for you. I support PDF, TXT, CSV  and more. Let's mingle with your data! 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")

# DataMingle's Pages
st.subheader("🚀 Explore DataMingle's Features")
st.write("""
- **DataMingle-Chat**: Engage in a data-centric conversation (PDF, TXT, CSV) with advanced indexing for responsive user interactions. | Leveraging [vectorstore](https://github.com/facebookresearch/faiss) and [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **DataMingle-Sheet** (beta): Dive into tabular data (CSV) for precise insights. | Empowered by [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for advanced data manipulation and visualization.

""")
st.markdown("---")
# - **DataMingle-Youtube**: Summarize and understand YouTube content effortlessly with our [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html).

# Contributing
st.markdown("### 🎯 Join the DataMingle Journey")
st.markdown("""
**DataMingle is constantly evolving. This is just a POC! Your contributions can help make it the ultimate data companion! Let's innovate together.**
""", unsafe_allow_html=True)


# Contact Information (Optional, Uncomment to Use)
# with st.sidebar.expander("📬 Contact & Credits"):
#     st.write("**Created by DataMango**")
#     st.markdown("Connect with us:")
#     st.write("**GitHub:** [DataMango/DataMingle-chatbot](https://github.com/DataMango/DataMingle-chatbot)")
#     st.write("**Website:** [datamango.com](https://datamango.com)")
