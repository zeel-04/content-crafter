import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import GoogleGenerativeAI
from social_media_post_generator import prompts
from dotenv import load_dotenv
import os
load_dotenv()

st.title("LinkedIn Post Generator")

with st.container(border=True):
    st.subheader("Generate from Youtube video")
    link = st.text_input("Youtube link")
    submit = st.button("Generate")

    if submit:
        loader = YoutubeLoader.from_youtube_url(
            link, 
            add_video_info=True
        )

        document = loader.load()

        youtube_transcript = document[0].page_content

        llm = GoogleGenerativeAI(
            model="models/gemini-1.5-pro-latest",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0
        )

        hook = llm.invoke(prompts.hook_prompt.format(youtube_transcript=youtube_transcript))
        content = llm.invoke(prompts.content_prompt.format(youtube_transcript=youtube_transcript))
        hashtags = llm.invoke(prompts.hashtag_prompt.format(youtube_transcript=youtube_transcript))

        hook = hook.replace("*", "")
        hook = hook.replace("#", "")

        content = content.replace("*","")
        content = content.replace("#","")

        st.code(f"{hook}\n\n{content}\n\n{hashtags}\n\n")