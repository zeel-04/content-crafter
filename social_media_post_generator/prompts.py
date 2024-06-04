hook_prompt = """
Transform mundane YouTube transcripts into viral LinkedIn sensations with a single line hook that electrifies your audience and leaves them craving more. Let your creativity soar as you craft irresistible sparks of connection that ignite conversations and set the platform on fire! Use emojis tastefully to amplify your message and keep your audience intrigued. (Note: Avoid adding any extra stuff other than hook")

Here is the youtube transcript:
<youtube_transcript>
{youtube_transcript}
</youtube_transcript>
"""

hashtag_prompt = """
Transform mundane YouTube transcripts into viral LinkedIn sensations with hashtags that electrifies your audience and leaves them craving more. Let your creativity soar as you craft irresistible sparks of connection that ignite conversations and set the platform on fire!  (Note: Avoid adding any extra stuff other than hashtags")

Here is the youtube transcript:
<youtube_transcript>
{youtube_transcript}
</youtube_transcript>
"""

content_prompt = """

As an accomplished LinkedIn content specialist, with demonstrated success in creating viral technical LinkedIn posts, 
your task is to dissect a YouTube transcript and distil it into an engaging LinkedIn post. 
Your post should weave together key insights in a digestible narrative that is bound to spark the curiosity of the AI/ML technical community.

Kick-start your post by a concise story-style sentence to provide context. 
Make sure to inject your technical prowess into your post by incorporating relevant AI/ML terminologies. 
Use emojis tastefully to amplify your message and keep your audience intrigued. 

Steer clear from naming the YouTube channel or sharing any Personally Identifiable Information (PII). 

(Note: Only write the posts main content by avoiding the opening statement/hook/heading and avoid adding hashtags as well")

<youtube_transcript>
{youtube_transcript}
</youtube_transcript>

Your task commences here. Good luck, and let the creative juices flow!

"""