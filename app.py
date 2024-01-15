import streamlit as st
import pandas as pd
from PIL import Image
import time
from bs4 import BeautifulSoup
import requests
import html.parser
# page settings
st.set_page_config(page_title="Job Searches",page_icon="random",initial_sidebar_state='expanded',menu_items={
    'Get Help':'mailto:chuckyjucky1963@gmail.com',
    'report a bug':'mailto:chuckyjucky1963@gmail.com',
    "About":"This is website is created by Peter Rogendo to show the job scraps",
    # "setting":"", 
    
})

st.header("Job Portal")

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation="
response = requests.get(url)
# print(response)

# html = response.text.strip()
html = response.text
# print(html)
soup = BeautifulSoup(html,"html.parser")



jobs=soup.find_all("li",class_="clearfix job-bx wht-shd-bx")
# len(jobs)

@st.cache_data
def main():
    pass


# sidebar filtering
st.sidebar.header("Please Select Job Category :")
# category=st.sidebar.multiselect(
#     "Select year :",
#     options=df["year"].unique(),
#     default=None
    
# )


master_list=[]
dat_dict = {}
for job in jobs:
    publish_date=job.find("span", class_="sim-posted").text.strip()
    if publish_date != "Posted few days ago":
        continue
    job_post = job.find("h1",class_="jd-job-title")
    company_name = job.find("h3" ,class_="joblist-comp-name")
    company_name=company_name.text.strip()
    skillset = job.find("span", class_="srp-skills").text.strip().replace('','')
    more_info = job.header.h2.a['href']

    dat_dict['job_post'] = job_post
    dat_dict['company_name'] = company_name
    dat_dict['publish_date'] = publish_date
    dat_dict['skillset'] = skillset
    dat_dict['more_info'] = more_info
    master_list.append(dat_dict)
    # print(len(dat_dict))
    # print(master_list)    # df = pd.DataFrame(master_list)

    

    # column_1=st.columns(1)
    # with column_1:
    st.markdown("---")
    st.subheader(job_post)
    st.subheader(company_name)
    st.link_button("More Info",more_info,type="primary")

    st.write("SKILLS REQUIRED")
    st.write(skillset)


    st.write(publish_date)

   


    st.markdown("---")