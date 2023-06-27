# Twitter-Extras | Built for Touch Portal
- [Twitter Extras](#Twitter-Extras)
  - [Description](#description) 
  - [Features](#Features)
    - [Actions](#actions)
        - [Twitter Extras](#gitago.twitter.mainactions)
    - [States](#states)
        - [Twitter Extras](#gitago.twitter.mainstates)
        - [Twitter Extras](#gitago.twitter.tweetsstates)
  - [Bugs and Support](#bugs-and-suggestion)
  - [License](#license)
  
# Description

This documentation generated for Twitter Extras V100 with [Python TouchPortal SDK](https://github.com/KillerBOSS2019/TouchPortal-API).

# Features

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


# License
This plugin is licensed under the [GPL 3.0 License] - see the [LICENSE](LICENSE) file for more information.

