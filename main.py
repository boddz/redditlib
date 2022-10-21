#!/usr/bin/env python3

from src.redditlib.oauth import *
from sys import version_info



def main():
    post = Posting(auth=HeaderUtils.auth_file(),
                   user_agent=HeaderUtils.user_agent())

    # print(HeaderUtils.user_agent())
    
    post.upload_post(content="sr=u_--salad&submit_type=profile&api_type=json&show_error_list=true&title=.&spoiler=false&nsfw=false&kind=self&original_content=false&post_to_twitter=false&sendreplies=true&richtext_json=%7B%22document%22%3A%5B%7B%22e%22%3A%22par%22%2C%22c%22%3A%5B%7B%22e%22%3A%22text%22%2C%22t%22%3A%22.%22%7D%5D%7D%5D%7D&validate_on_submit=true")


if __name__ == "__main__":
    main()
