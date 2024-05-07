from langchain_community.document_loaders import YoutubeLoader
loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=Knjc25bPn3w", add_video_info=False
)
loader.load()