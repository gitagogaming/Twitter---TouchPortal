#  # The app and the corresponding credentials must have the Write permission
#  
#  # Check the App permissions section of the Settings tab of your app, under the
#  # Twitter Developer Portal Projects & Apps page at
#  # https://developer.twitter.com/en/portal/projects-and-apps
#  
#  # Make sure to reauthorize your app / regenerate your access token and secret 
#  # after setting the Write permission
#  
#  
#  ## we can do place ID for location of tweet.. 
#  # media_tagged_user_ids.. so tag a perosn in the image
#  ## delete tweet?  - maybe the last one went out wrong.. so we delete and resend upon user request
#  ## followe user.. mabye streamer wants to easily follower a follower?  the viewer can be like !followme and then the streamer will autofollow?
#  
#
# pyinstaller --onefile main.py --name Twitter_Plugin.exe
# pyinstaller --add-data "plugin_config.txt;." --onefile main.py --name Twitter_Plugin.exe
import ast
import tweepy
import os
import TouchPortalAPI
from TouchPortalAPI import TYPES, Tools
from TouchPortalAPI.logger import Logger
from TPPEntry import TP_PLUGIN_ACTIONS, TP_PLUGIN_STATES, TP_PLUGIN_EVENTS, PLUGIN_ID
import os
import webbrowser
import time
### Local Imports
from update_check import plugin_update_check, GITHUB_PLUGIN_NAME, GITHUB_USER_NAME, PLUGIN_NAME

import sys



class TwitterAPI:
    def __init__(self, 
                 bearer_token=None, consumer_key=None,consumer_secret=None, access_token=None, access_token_secret=None):
        
        self.bearer_token = bearer_token
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.client = None
        self.api = None
        
    def set_auth_credentials(self, 
                             bearer_token, consumer_key, consumer_secret, access_token, access_token_secret):
        
        self.bearer_token = bearer_token
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
        self.client = tweepy.Client(
            bearer_token=self.bearer_token,
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )
        
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)
        return True
    
    def auth_check(self):
        response = self.set_auth_credentials(
            bearer_token         =  plugin.plugin_settings['Bearer Token'],
            consumer_key         =   plugin.plugin_settings['API Key'],
            consumer_secret      =   plugin.plugin_settings['API Secret'],
            access_token         =   plugin.plugin_settings['Access Token'],
            access_token_secret  =  plugin.plugin_settings['Access Token Secret']   
            )
    
        return response


    def verify_credentials(self):
        response = self.api.verify_credentials()
        return response


    def update_user_details(self):
        """ 
        Updates some TouchPortal States with the current user details and profile photo icon
        """
        try:
            response = self.verify_credentials()
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Screen_Name", stateValue=response.screen_name)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Name", stateValue=response.name)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.User_ID", stateValue=response.id_str)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Followers_Count", stateValue=str(response.followers_count))
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Friends_Count", stateValue=str(response.friends_count))

            imageBase64 = Tools.convertImage_to_base64(response.profile_image_url.replace("_normal", ""))
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.ProfilePhoto_ICON", stateValue=imageBase64)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.ProfilePhoto_URL", stateValue=response.profile_image_url)
        except Exception as e:      
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter_Status", stateValue="Bad Auth Data")
            plugin.log.error(f"Error Updating User Details: {e}")



    def set_display_name(self, displayName:str):
        """ 
        Sets the display name of the twitter account
        """
        response = self.api.update_profile(name= displayName, skip_status=True)
        return response
    
    def new_profile_image(self, image:str):
        """
        Updates the profile image to the desired image
        - Image must be a path to the image file
        """
        response = self.api.update_profile_image(image)
        return response


    def create_new_tweet(self, text:str, media:str = None, super_followers_only:bool = False, reply_settings:str = None):
        """
        Creates a new tweet with the desired text and media (image or video)
        - Media must be a path to the media file
        - Super Followers Only: True or False
        - Reply Settings: "mentionedUsers", "following", "everyone"
    
        ## Images = JPG, PNG, 5mb or less
        ## Videos = MP4, MOV, 512mb or less and less than 140 seconds
        """
        chunked_status = False
        if media is not None:
            valid_image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            valid_video_extensions = ['.mp4', '.mov']
            valid_image_size_limit = 5 * 1024 * 1024  # 5mb in bytes
            valid_video_size_limit = 512 * 1024 * 1024  # 512mb in bytes
            file_extension = os.path.splitext(media)[1].lower()

            if file_extension in valid_image_extensions:
                file_size = os.path.getsize(media)
                if file_size <= valid_image_size_limit:
                    if file_extension == ".gif":
                        media_category = "tweet_gif"
                    else:
                        media_category = "tweet_image"
                else:
                    # Compress the image here if needed
                    media_category = "tweet_image"  # Placeholder, update with the compressed image category
                    raise ValueError("Image file size exceeds the limit, Please compress the image.")
            elif file_extension in valid_video_extensions:
                file_size = os.path.getsize(media)
                if file_size <= valid_video_size_limit:
                    media_category = "tweet_video"
                else:
                    raise ValueError("Video file size exceeds the limit.")
            else:
                raise ValueError("Invalid file format. Only JPG, JPEG, PNG, GIF, MP4, and MOV files are supported.")
            
            if media_category == "tweet_gif":
                chunked_status = True
                
            media_upload = self.api.media_upload(media, media_category=media_category, chunked=chunked_status)
            text = ast.literal_eval(f'"{text}"')
            response = self.client.create_tweet(
                text=text,
                media_ids=[media_upload.media_id],
                reply_settings=reply_settings,
                for_super_followers_only=super_followers_only
            )

            self.last_tweet_id = response.data['id']
            return response
        else:
            text = ast.literal_eval(f'"{text}"')
            response = self.client.create_tweet(
                text=text,
                for_super_followers_only=super_followers_only
            )
            return response
    
    
    
    def create_tweet_poll(self, text:str, poll_options:list = ["Yes", "No"], poll_duration:int = 60, super_followers_only:bool = False, reply_settings:str = "everyone"):
        """ 
        Creates a tweet with a poll for the desired time duration
        - User can select between 2 and 4 options
        - User can save the url for this poll and display it live on stream with BrowserSource & Cropping
        """
        response = self.client.create_tweet(
            text=text,
            poll_options=poll_options,
            poll_duration_minutes=poll_duration,
            reply_settings=reply_settings,
            for_super_followers_only=super_followers_only
            )
        self.last_tweet_id = response.data['id']
        return response



    def delete_last_tweet(self):
        """ 
        Deletes the last tweet sent by the user
        """
        response = self.client.delete_tweet(self.last_tweet_id)
        return response




class ClientInterface(TouchPortalAPI.Client):
    def __init__(self):
        super().__init__(self)
        
        
        self.pluginId = PLUGIN_ID
        # TP connection settings - These can be left at default
        self.TPHOST = "127.0.0.1"
        self.TPPORT = 12136
        self.RCV_BUFFER_SZ = 4096 
        self.SND_BUFFER_SZ = 1048576

        # Log settings
        self.logLevel = "INFO"
        self.setLogFile("Twitter_Extras.log")
    
        # Register events
        self.add_listener(TYPES.onConnect, self.onConnect)
        self.add_listener(TYPES.onAction, self.onAction)
        self.add_listener(TYPES.onShutdown, self.onShutdown)
        self.add_listener(TYPES.onListChange, self.onListChange)
        self.add_listener(TYPES.onNotificationOptionClicked, self.onNoticationClicked)
        self.add_listener(TYPES.onSettingUpdate, self.onSettings)


    """
    Custom Method/Functions
    """
    def settingsToDict(self, settings):
        """ 
        Convert a list of settings to a dictionary
        """
        return { list(settings[i])[0] : list(settings[i].values())[0] for i in range(len(settings)) }



    """
    Events
    """
    def onConnect(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
        self.log.debug(f"Connection: {data}")
        plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter_Status", stateValue="Disconnected")


        ## Checking for Updates
        try:
            github_check, message = plugin_update_check(str(data['pluginVersion']))
            if github_check == True:
                plugin.showNotification(
                    notificationId= f"{PLUGIN_ID}.TP.Plugins.Update_Check",
                    title=f"{PLUGIN_NAME} {github_check} is available",
                    msg=f"A new version of {PLUGIN_NAME} is available and ready to Download.\nThis may include Bug Fixes and or New Features\n\nPatch Notes\n{message} ",
                    options= [{
                    "id":f"{PLUGIN_ID}.tp.update.download",
                    "title":"Click to Update!"
                }])
        except: 
            self.log.error("Error Checking for Updates")

        
        self.plugin_settings = self.settingsToDict(data["settings"])
        if self.plugin_settings['Debug Mode'].lower() == "on":
            self.log.setLogLevel("DEBUG")
            self.log.info("set log level to debug")
        else:
            self.log.setLogLevel("INFO")
            self.log.info("set log level to info")

       # print(self.settingsToDict(data["settings"]))
        twitter.auth_check()
        twitter.update_user_details()


    def onSettings(self, data):
        self.log.debug(f"Connection: {data}")
        ## pushing settings chagned to the plugin_settings variable
        self.plugin_settings = self.settingsToDict(data['values'])
        if self.plugin_settings['Debug Mode'].lower() == "on":
            self.setLogLevel("DEBUG")
            print("set log level to debug")
        else:
            self.setLogLevel("INFO")
            print("set log level to info")


        response = twitter.auth_check()
        if response == True:
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter_Status", stateValue="Connected")
        else:
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter_Status", stateValue="Bad Auth Data")


    def onAction(self, data):
        self.log.debug(f"Connection: {data}")
        G_LOG.debug(f"Action: {data}")

        action_data = data.get('data')
        aid = data.get('actionId')
        if not action_data or not aid:
            return
        
        if aid == f"{PLUGIN_ID}.act.delete_tweet":
            response = twitter.delete_last_tweet()
            self.log.debug(f"Delete Tweet Response: {response}")

      ### Get The Cells Value
        if aid == f"{PLUGIN_ID}.act.new_tweet":
            if data['data'][2]['value'] == "True":
                 super_followers_only = True
            else:
                 super_followers_only = False

            response = twitter.create_new_tweet(data['data'][0]['value'], reply_settings=data['data'][1]['value'], super_followers_only=super_followers_only)

            ## make a catch here for any current uploads of tweet so a person doesnt get impatient with the upload time on videos and then tweet again
            
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_Tweet_ID", stateValue=response.data['id'])
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_Tweet_URL", stateValue=f"https://twitter.com/user/status/{response.data['id']}")

            self.log.debug(f"New Tweet URL: https://twitter.com/user/status/{response.data['id']}")


        if aid == f"{PLUGIN_ID}.act.new_tweet_w_media":
            if data['data'][2]['value'] == "True":
                 super_followers_only = True
            else:
                 super_followers_only = False

            if data['data'][1]['value'] == "everyone":
                reply_settings = None
            else:
                reply_settings = data['data'][2]['value']
            

            response = twitter.create_new_tweet(data['data'][0]['value'], media=data['data'][3]['value'], reply_settings=reply_settings , super_followers_only=super_followers_only)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_Tweet_ID", stateValue=response.data['id'])
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_Tweet_URL", stateValue=f"https://twitter.com/user/status/{response.data['id']}")

            self.log.debug(f"New Tweet Media URL: https://twitter.com/user/status/{response.data['id']}")


        if aid == f"{PLUGIN_ID}.act.new_poll":
            
            if data['data'][2]['value'] == "everyone":
                reply_settings = None
            else:
                reply_settings = data['data'][2]['value']
            if data['data'][3]['value'] == "True":
                 super_followers_only = True
            else:
                 super_followers_only = False

            poll_values = []
            for item in data['data'][-4:]:
                checkvalue = item.get('value')
                if checkvalue and checkvalue.strip():
                    poll_values.append(checkvalue)

            response = twitter.create_tweet_poll(data['data'][0]['value'],
                                                poll_options=poll_values,
                                                poll_duration=int(data['data'][1]['value']),
                                                reply_settings=reply_settings, 
                                                super_followers_only=super_followers_only)
            
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_TweetPoll_ID", stateValue=response.data['id'])
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Last_TweetPoll_URL", stateValue=f"https://twitter.com/user/status/{response.data['id']}")
            self.log.debug(f"New Tweet Poll URL: https://twitter.com/user/status/{response.data['id']}")


        if aid == f"{PLUGIN_ID}.act.update_display_name":
            response = twitter.set_display_name(data['data'][0]['value'])

            if response:
                plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Name", stateValue=response.name)
                plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Followers_Count", stateValue=str(response.followers_count))
                plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Friends_Count", stateValue=str(response.friends_count))

        if aid == f"{PLUGIN_ID}.act.update_profile_image":
            response = twitter.new_profile_image(data['data'][0]['value'])
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Name", stateValue=response.name)
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Followers_Count", stateValue=str(response.followers_count))
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.Friends_Count", stateValue=str(response.friends_count))
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.ProfilePhoto_URL", stateValue=response.profile_image_url)


            imageBase64 = Tools.convertImage_to_base64(response.profile_image_url.replace("_normal", ""))
            plugin.stateUpdate(stateId=PLUGIN_ID + ".state.Twitter.ProfilePhoto_ICON", stateValue=imageBase64)
           # print(response)


    def onNoticationClicked(data):
        if data['optionId'] == f'{PLUGIN_ID}.tp.update.download':
            github_check = TouchPortalAPI.Tools.updateCheck(GITHUB_USER_NAME, GITHUB_PLUGIN_NAME)
            url = f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_PLUGIN_NAME}/releases/tag/{github_check}"
            webbrowser.open(url, new=0, autoraise=True)

    ## When a Choice List is Changed in a Button Action
    def onListChange(self, data):
        self.log.info(f"Connection: {data}")

    def onShutdown(self, data):
        self.log.info('Received shutdown event from TP Client.')
        self.disconnect()
        
  #  def onError(self, data):
  #      self.error(f'Error in TP Client event handler: {repr(data)}')



if __name__ == "__main__":
    G_LOG = Logger(name = PLUGIN_ID)
    plugin = ClientInterface()
    twitter = TwitterAPI()
    ret = 0
    try:
        plugin.connect()
    except KeyboardInterrupt:
        plugin.log.warning("Caught keyboard interrupt, exiting.")
    except Exception:
        from traceback import format_exc
        plugin.log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        plugin.disconnect()
        del plugin
        sys.exit(ret)






