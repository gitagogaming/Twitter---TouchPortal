PLUGIN_ID = "gitago.twitter"

PLUGIN_FOLDER = "Twitter_Extras"
PLUGIN_NAME = "Twitter_Extras"
PLUGIN_ICON = "Twitter_Logo_26px.png"

TP_PLUGIN_INFO = {
    "sdk": 6,
    "version": 103,
    "name": "Twitter Extras",
    "id": PLUGIN_ID,
    "plugin_start_cmd_windows": f"%TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}\\{PLUGIN_NAME}.exe",
    "plugin_start_cmd_linux": f"sh %TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}//start.sh {PLUGIN_NAME}",
    "plugin_start_cmd_mac": f"sh %TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}//start.sh {PLUGIN_NAME}",
    "configuration": {
        "colorDark": "#222423",
        "colorLight": "#1D9BF0"
    },
}







TP_PLUGIN_SETTINGS = {
    "1": {
        "name": "API Key",
        "default": "https://developer.twitter.com/en/portal/projects/",
        "type": "text",
        "isPassword": True,
    },
    "2": {
        "name": "API Secret",
        "default": "",
        "type": "text",
        "isPassword": True
    },
    "3": {
        "name": "Bearer Token",
        "default": "",
        "type": "text",
        "isPassword": True
    },
    "4": {
        "name": "Access Token",
        "default": "",
        "type": "text",
        "isPassword": True
    },
    "5": {
        "name": "Access Token Secret",
        "default": "",
        "type": "text",
        "isPassword": True
    },
    "6": {
        "name": "Debug Mode",
        "default": "Off",
        "type": "text",
    }

}

TP_PLUGIN_CATEGORIES = {
    "main": {
        "id": PLUGIN_ID + ".main",
        "name": "Twitter Extras",
        "imagepath": f"%TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}\\{PLUGIN_ICON}"
    },
    "tweets": {
        "id": PLUGIN_ID + ".tweets",
        "name": "Twitter Extras | Tweets",
        "imagepath": f"%TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}\\{PLUGIN_ICON}"
    }
}

TP_PLUGIN_CONNECTORS = {}

TP_PLUGIN_ACTIONS = {
    "1": {
        "id": PLUGIN_ID + ".act.new_poll",
        "name": "Send Poll Tweet",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Make a Poll Tweet",
        "format": "Poll Tweet Message:$[1] Duration: $[2] - Reply Options: $[3] - Super Followers Only: $[4]  |  Poll Options: Option1:$[5]  Option2:$[6]  Option3:$[7]  Option4:$[8]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.new_poll.message",
                "type": "text",
                "label": "The Tweet Message",
                "default": "Hello World"
            },
            "2": {
                "id": PLUGIN_ID + ".act.new_poll.duration",
                "type": "text",
                "label": "The Tweet Poll Duration (minutes)",
                "default": "30"
            },
            "3": {
                "id": PLUGIN_ID + ".act.new_poll.reply_options",
                "type": "choice",
                "label": "Whom is able to reply",
                "default": "everyone",
                "valueChoices": ["everyone", "mentionedUsers", "following"]
            },
            "4": {
                "id": PLUGIN_ID + ".act.new_poll.super_followers_only",
                "type": "choice",
                "label": "For Super Followers Only",
                "default": "False",
                "valueChoices": ["True", "False"]
            },
            "5": {
                "id": PLUGIN_ID + ".act.new_poll.option1",
                "type": "text",
                "label": "Whom is able to reply",
                "default": "Yes",
            },
            "6": {
                "id": PLUGIN_ID + ".act.new_poll.option2",
                "type": "text",
                "label": "Whom is able to reply",
                "default": "No",
            },
            "7": {
                "id": PLUGIN_ID + ".act.new_poll.option3",
                "type": "text",
                "label": "Whom is able to reply",
                "default": "Maybe",
            },
            "8": {
                "id": PLUGIN_ID + ".act.new_poll.option4",
                "type": "text",
                "label": "Whom is able to reply",
                "default": "",
            }
        },
        "category": "main"
    },
  
    "2": {
        "id": PLUGIN_ID + ".act.new_tweet",
        "name": "Send Tweet",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Make a Tweet",
        "format": "Tweet Message:$[1] - Reply Options: $[2] - Super Followers Only: $[3]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.new_tweet.message",
                "type": "text",
                "label": "The Tweet Message",
                "default": "Hello World"
            },
            "2": {
                "id": PLUGIN_ID + ".act.new_tweet.reply_options",
                "type": "choice",
                "label": "Whom is able to reply",
                "default": "everyone",
                "valueChoices": ["everyone", "mentionedUsers", "following"]
            },
            "3": {
                "id": PLUGIN_ID + ".act.new_tweet.super_followers_only",
                "type": "choice",
                "label": "For Super Followers Only",
                "default": "False",
                "valueChoices": ["True", "False"]
            },
        },
        "category": "main"
    },
    "3": {
        "id": PLUGIN_ID + ".act.new_tweet_w_media",
        "name": "Send Tweet with Media",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Make a Tweet with an Image or Video - Image should be less than 5mb and Video should be less than 400mb",
        "format": "Tweet Message:$[1] with Media:$[4] -  Reply Options: $[2] - Super Followers Only: $[3]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.message",
                "type": "text",
                "label": "The Tweet Message",
                "default": "Hello World"
            },
            "2": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.reply_options",
                "type": "choice",
                "label": "Whom is able to reply",
                "default": "everyone",
                "valueChoices": ["everyone", "mentionedUsers", "following"]
            },
            "3": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.super_followers_only",
                "type": "choice",
                "label": "For Super Followers Only",
                "default": "False",
                "valueChoices": ["True", "False"]
            },
            "4": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.message.media",
                "type": "file",
                "extensions": ["*.jpg", "*.png", "*.jpeg", "*.mov", "*.mp4", "*.gif"],
                "label": "The Media File Location",
                "default": ""
            }, 
        },
        "category": "main"
    },

    "4": {
        "id": PLUGIN_ID + ".act.update_profile_image",
        "name": "Change Profile Picture",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Submit a New Profile Image",
        "format": "Update Profile Image:$[1] ",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.update_profile_image.media",
                "type": "file",
                "extensions": ["*.jpg", "*.png", "*.jpeg"],
                "label": "The Media File Location",
                "default": ""
            }, 
        },
        "category": "main"
    },

    "5": {
        "id": PLUGIN_ID + ".act.update_display_name",
        "name": "Change Display Name",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Change your Display Name",
        "format": "New Display Name:$[1] ",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.update_display_name.name",
                "type": "text",
                "label": "New Display Name",
                "default": ""
            }, 
        },
        "category": "main"
    },
        "6": {
        "id": PLUGIN_ID + ".act.delete_tweet",
        "name": "Delete Last Tweet",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Delete Last Tweet",
        "format": "Delete the last tweet sent ",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.delete_tweet_data",
                "type": "text",
                "label": "last tweet id",
                "default": ""
            }, 

        },
        "category": "main"
    },
}

"""

        "3": {
        "id": PLUGIN_ID + ".act.new_tweet_w_media",
        "name": "Send Tweet with Media",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "description": "Make a Tweet with an Image or Video - Image should be less than 5mb and Video should be less than 400mb",
        "format": "Tweet Message:$[1] with Media:$[4] - Reply Options: $[2] - Super Followers Only: $[3]   Test Switch:$[5]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.message",
                "type": "text",
                "label": "The Tweet Message",
                "default": "Hello World"
            },
            "2": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.reply_options",
                "type": "choice",
                "label": "Whom is able to reply",
                "default": "Everyone",
                "valueChoices": ["Everyone", "mentionedUsers", "following"]
            },
            "3": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.super_followers_only",
                "type": "choice",
                "label": "For Super Followers Only",
                "default": "False",
                "valueChoices": ["True", "False"]
            },
            "4": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.message.media",
                "type": "file",
                "label": "The Media File Location",
                "default": ""
            },
            "5": {
                "id": PLUGIN_ID + ".act.new_tweet_w_media.message.switch",
                "type": "switch",
                "label": "The Media File Location",
                "default": ""
            }    

        },
        "category": "main"
    }
"""
TP_PLUGIN_STATES = {
    "0": {
        "id": PLUGIN_ID + ".state.Twitter_Status",
        "type": "text",
        "desc": "TW | Twitter Status",
        "default": "Disconnected",
        "category": "main"
    },
    "1": {
        "id": PLUGIN_ID + ".state.Twitter.Screen_Name",
        "type": "text",
        "desc": "TW | Twitter Screen Name",
        "default": "",
        "category": "main"
    },
    "2": {
        "id": PLUGIN_ID + ".state.Twitter.Name",
        "type": "text",
        "desc": "TW | Twitter Name",
        "default": "",
        "category": "main"
    },
    "3": {
        "id": PLUGIN_ID + ".state.Twitter.User_ID",
        "type": "text",
        "desc": "TW | Twitter User ID",
        "default": "",
        "category": "main"
    },
    "4": {
        "id": PLUGIN_ID + ".state.Twitter.Followers_Count",
        "type": "text",
        "desc": "TW | Twitter Followers Count",
        "default": "",
        "category": "main"
    },
    "5": {
        "id": PLUGIN_ID + ".state.Twitter.Friends_Count",
        "type": "text",
        "desc": "TW | Twitter Friends Count",
        "default": "",
        "category": "main"
    },
    "6": { 
        "id": PLUGIN_ID + ".state.Twitter.Last_Tweet_URL",
        "type": "text",
        "desc": "TW | Twitter Last Tweet URL",
        "default": "",
        "category": "tweets"
    },
    "7": {
        "id": PLUGIN_ID + ".state.Twitter.Last_Tweet_ID",
        "type": "text",
        "desc": "TW | Twitter Last Tweet ID",
        "default": "",
        "category": "tweets"
    },
    "8": {
        "id": PLUGIN_ID + ".state.Twitter.Last_TweetPoll_ID",
        "type": "text",
        "desc": "TW | Twitter Last Tweet Poll ID",
        "default": "",
        "category": "tweets"
    },
    "9": {
        "id": PLUGIN_ID + ".state.Twitter.Last_TweetPoll_URL",
        "type": "text",
        "desc": "TW | Twitter Last Tweet Poll URL",
        "default": "",
        "category": "tweets"
    },


    "10": {
        "id": PLUGIN_ID + ".state.Twitter.ProfilePhoto_ICON",
        "type": "text",
        "desc": "TW | Twitter Profile Photo ICON",
        "default": "",
        "category": "main"
    },
    "11": {
        "id": PLUGIN_ID + ".state.Twitter.ProfilePhoto_URL",
        "type": "text",
        "desc": "TW | Twitter Profile Photo URL",
        "default": "",
        "category": "main"
    },


}




TP_PLUGIN_EVENTS = {}


