# nba-simple-dashboard-python

Here with a python project that displays a simple nba dashboard in the local host 8080. It covers three views:
1. Team stats : given a divison it fetches the team stats from nab_py and diplays in the UI. For now, it displays just 6 columns from the api. The columns maynot be appropriate. 
2. Leading point scorer: on the page load, the top 20 leading point scorrers are displayed, highlighting the LEADER
3. Assist leader: on page load, displayes the to 20 Assist leaders highlighting the top 20 ones.

A Demo for this app:
https://screencast.com/t/z9eWz2HA 


Note: There was an issue fetching data from nba through nba_py. To overcome this, 
I have taken nba_py in local and modified the header in the __init__ file. The new header looks like the this:
HEADERS = {
    'user-agent': ('customheader'),  # noqa: E501
    'Dnt': ('1'),
    'Accept-Encoding': ('gzip, deflate, sdch'),
    'Accept-Language': ('en'),
    'origin': ('http://stats.nba.com')
    }:

NOTE: Pands is required else nba_py returns json instead of dataframe which is not handled by this app

# Dependencies:

Flask 1.0.2 preferred
Jinja2 2.10 preffered 
marshmallow 2.16.3 preferred
nba-py pip istalled from local with headers modified from originals
requests 2.21.0 preferred
