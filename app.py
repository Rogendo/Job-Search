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

st.header("Developer Job Portal")

# javascript
def javascript():
    javascript_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Javascript&txtLocation="
    response = requests.get(javascript_url)

    html_js = response.text
    soup_js = BeautifulSoup(html_js,"html.parser")



    jobs=soup_js.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        publish_date=job.find("span", class_="sim-posted").text.strip()
        if publish_date != "Posted few days ago":
            continue
        job_title = job.header.h2.text
        # job_post  =  job.find_all("h2").text

        company_name = job.find("h3" ,class_="joblist-comp-name")
        company_name=company_name.text.strip()
        skillset = job.find("span", class_="srp-skills").text.strip().replace('','')
        more_info = job.header.h2.a['href']

        st.markdown("---")
        st.subheader(job_title)
        st.subheader(company_name)
        st.link_button("More Info",more_info,type="primary")

        st.write("SKILLS REQUIRED")
        st.write(skillset)
        st.write(publish_date)
        st.markdown("---")

# python
def python():
    py_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation="
    response = requests.get(py_url)
    
    html_py = response.text
    soup_py = BeautifulSoup(html_py,"html.parser")

    jobs=soup_py.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        publish_date=job.find("span", class_="sim-posted").text.strip()
        if publish_date != "Posted few days ago":
            continue
        job_title = job.header.h2.text
        # job_post  =  job.find_all("h2").text

        company_name = job.find("h3" ,class_="joblist-comp-name")
        company_name=company_name.text.strip()
        skillset = job.find("span", class_="srp-skills").text.strip().replace('','')
        more_info = job.header.h2.a['href']

        st.markdown("---")
        st.subheader(job_title)
        st.subheader(company_name)
        st.link_button("More Info",more_info,type="primary")

        st.write("SKILLS REQUIRED")
        st.write(skillset)
        st.write(publish_date)
        st.markdown("---")

# java
def java():
    java_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=java&txtLocation="
    response = requests.get(java_url)
   
    html_java = response.text
    soup_java = BeautifulSoup(html_java,"html.parser")

    jobs=soup_java.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        publish_date=job.find("span", class_="sim-posted").text.strip()
        if publish_date != "Posted few days ago":
            continue
        job_title = job.header.h2.text
        # job_post  =  job.find_all("h2").text

        company_name = job.find("h3" ,class_="joblist-comp-name")
        company_name=company_name.text.strip()
        skillset = job.find("span", class_="srp-skills").text.strip().replace('','')
        more_info = job.header.h2.a['href']

        st.markdown("---")
        st.subheader(job_title)
        st.subheader(company_name)
        st.link_button("More Info",more_info,type="primary")

        st.write("SKILLS REQUIRED")
        st.write(skillset)
        st.write(publish_date)
        st.markdown("---")
# c++
def cpp():
    cpp_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=c%2B%2B&txtLocation="
    response = requests.get(cpp_url)
   
   
    cpp_java = response.text
    soup_cpp = BeautifulSoup(cpp_java,"html.parser")

    jobs=soup_cpp.find_all("li",class_="clearfix job-bx wht-shd-bx")
    for job in jobs:
        publish_date=job.find("span", class_="sim-posted").text.strip()
        if publish_date != "Posted few days ago":
            continue
        job_title = job.header.h2.text
        # job_post  =  job.find_all("h2").text

        company_name = job.find("h3" ,class_="joblist-comp-name")
        company_name=company_name.text.strip()
        skillset = job.find("span", class_="srp-skills").text.strip().replace('','')
        more_info = job.header.h2.a['href']

       
        st.markdown("---")
        st.subheader(job_title)
        st.subheader(company_name)
        st.link_button("More Info",more_info,type="primary")
        st.write("SKILLS REQUIRED")
        st.write(skillset)
        st.write(publish_date)
        st.markdown("---")


# sidebar filtering
st.sidebar.header("Base Programming Language :")
lang=st.sidebar.selectbox('Select language',["java","python","c++","javascript"])

if(lang == "javascript"):
    javascript()

elif lang=="java":
    java()
elif(lang=="python"):
    python()

elif(lang == "c++"):
    cpp()
                                                                                 