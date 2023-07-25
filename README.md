
<p align="center">
  <img src="https://github.com/gitagogaming/Twitter---TouchPortal/assets/76603653/85b9579c-ed53-4d4e-b702-3f7238cb8b8" alt="twitter_extras" style="width: 75%;">
</p>

# Twitter-Extras
Built for Touch Portal
- [Twitter Extras](#Twitter-Extras)
  - [Description](#description)
  - [Tweet Upload Restrictions](#Tweet-Restrictions)
  - [Actions](#actions)
    - [Main Actions](#gitago.twitter.mainactions)
  - [States](#states)
    - [Twitter Extras](#gitago.twitter.mainstates)
    - [Twitter Extras | Tweets](#gitago.twitter.tweetsstates)
  - [Bugs and Support](#bugs-and-suggestion)

# Description
Do things on your Twitter using Touch Portal

- Send Poll Tweet: Engage your audience with interactive poll tweets.
- Send Tweet: Share your thoughts and updates with a single click.
- Send Tweet with Media: Enhance your tweets with captivating images or videos.
- Change Profile Picture: Easily update your profile image to reflect your personal brand.
- Change Display Name: Customize your display name to make a lasting impression.


# Tweet-Restrictions
 ## Image Upload Recommendations / Restrictions
- Supported image media types: JPG, PNG, GIF, WEBP
- Image size should be less than 5 MB
- Animated GIF size should be less than 15 MB
- Animated GIF Number of frames should be less than 350
- Resolution should be less than 1280x1080 (width x height)


## Video Upload Recommendations / Restrictions
- Video Codec: H264 High Profile
- Frame Rates: 30 FPS, 60 FPS (should be 60 or less)
- Video Resolution: 1280x720 (landscape), 720x1280 (portrait), 720x720 (square)
- Minimum Video Bitrate: 5,000 kbps
- Minimum Audio Bitrate: 128 kbps
- Aspect Ratio: 16:9 (landscape or portrait), 1:1 (square)
- Audio Codec: AAC LC (Recommended)
- File Size: Must not exceed 512 mb
- Duration: must be between 0.5 seconds and 140 seconds

__If you are still having issue uploading a media file, please post the file here and explain what you have tried so far.__

## Actions
<details open id='gitago.twitter.mainactions'><summary><b>Category:</b> Twitter Extras <small><ins>(Click to expand)</ins></small></summary><table>
<tr valign='buttom'><th>Action Name</th><th>Description</th><th>Format</th><th nowrap>Data<br/><div align=left><sub>choices/default (in bold)</th><th>On<br/>Hold</sub></div></th></tr>
<tr valign='top'><td>Send Poll Tweet</td><td> </td><td>Poll Tweet Message:[1] Duration: [2] - Reply Options: [3] - Super Followers Only: [4]  |  Poll Options: Option1:[5]  Option2:[6]  Option3:[7]  Option4:[8]</td><td><details><summary><ins>Click to expand</ins></summary><ol start=1>
<li>Type: text &nbsp; 
Default: <b>Hello World</b></li>
<li>Type: text &nbsp; 
Default: <b>30</b></li>
<li>Type: choice &nbsp; 
Default: <b>everyone</b> Possible choices: ['everyone', 'mentionedUsers', 'following']</li>
<li>Type: choice &nbsp; 
Default: <b>False</b> Possible choices: ['True', 'False']</li>
<li>Type: text &nbsp; 
Default: <b>Yes</b></li>
<li>Type: text &nbsp; 
Default: <b>No</b></li>
<li>Type: text &nbsp; 
Default: <b>Maybe</b></li>
<li>Type: text &nbsp; 
&lt;empty&gt;</li>
</ol></td>
</details><td align=center>No</td>
<tr valign='top'><td>Send Tweet</td><td> </td><td>Tweet Message:[1] - Reply Options: [2] - Super Followers Only: [3]</td><td><ol start=1><li>Type: text &nbsp; 
Default: <b>Hello World</b></li>
<li>Type: choice &nbsp; 
Default: <b>everyone</b> Possible choices: ['everyone', 'mentionedUsers', 'following']</li>
<li>Type: choice &nbsp; 
Default: <b>False</b> Possible choices: ['True', 'False']</li>
</ol></td>
<td align=center>No</td>
<tr valign='top'><td>Send Tweet with Media</td><td> </td><td>Tweet Message:[1] with Media:[4] -  Reply Options: [2] - Super Followers Only: [3]</td><td><details><summary><ins>Click to expand</ins></summary><ol start=1>
<li>Type: text &nbsp; 
Default: <b>Hello World</b></li>
<li>Type: choice &nbsp; 
Default: <b>everyone</b> Possible choices: ['everyone', 'mentionedUsers', 'following']</li>
<li>Type: choice &nbsp; 
Default: <b>False</b> Possible choices: ['True', 'False']</li>
<li>Type: file &nbsp; 
&lt;empty&gt;</li>
</ol></td>
</details><td align=center>No</td>
<tr valign='top'><td>Change Profile Picture</td><td> </td><td>Update Profile Image:[1] </td><td><ol start=1><li>Type: file &nbsp; 
&lt;empty&gt;</li>
</ol></td>
<td align=center>No</td>
<tr valign='top'><td>Change Display Name</td><td> </td><td>New Display Name:[1] </td><td><ol start=1><li>Type: text &nbsp; 
&lt;empty&gt;</li>
</ol></td>
<td align=center>No</td>
</tr></table></details>
<br>

## States
<details id='gitago.twitter.mainstates'><summary><b>Category:</b> Twitter Extras <small><ins>(Click to expand)</ins></small></summary>


| Id | Description | DefaultValue | parentGroup |
| --- | --- | --- | --- |
| .state.Twitter_Status | TW | Twitter Status | Disconnected |   |
| .state.Twitter.Screen_Name | TW | Twitter Screen Name |  |   |
| .state.Twitter.Name | TW | Twitter Name |  |   |
| .state.Twitter.User_ID | TW | Twitter User ID |  |   |
| .state.Twitter.Followers_Count | TW | Twitter Followers Count |  |   |
| .state.Twitter.Friends_Count | TW | Twitter Friends Count |  |   |
| .state.Twitter.ProfilePhoto_ICON | TW | Twitter Profile Photo ICON |  |   |
| .state.Twitter.ProfilePhoto_URL | TW | Twitter Profile Photo URL |  |   |
</details>

<details id='gitago.twitter.tweetsstates'><summary><b>Category:</b> Twitter Extras | Tweets <small><ins>(Click to expand)</ins></small></summary>


| Id | Description | DefaultValue | parentGroup |
| --- | --- | --- | --- |
| .state.Twitter.Last_Tweet_URL | TW | Twitter Last Tweet URL |  |   |
| .state.Twitter.Last_Tweet_ID | TW | Twitter Last Tweet ID |  |   |
| .state.Twitter.Last_TweetPoll_ID | TW | Twitter Last Tweet Poll ID |  |   |
| .state.Twitter.Last_TweetPoll_URL | TW | Twitter Last Tweet Poll URL |  |   |
</details>

<br>

# Bugs and Suggestion
Open an issue on github or join offical [TouchPortal Discord](https://discord.gg/MgxQb8r) for support.



