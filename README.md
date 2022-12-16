# thread-keeper-automator
Automated Twitter URL processing for the excellent [thread-keeper](https://github.com/harvard-lil/thread-keeper)

1. Deploy the thread-keeper to your server
2. Download an [archive of your twitter account](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive)
3. Change the extension `.js` => `.json` and validate and the `/twitter-2009-2022/data/tweets.js` file
4. Extract the `tweet.id` and the `.tweet.created_at` from all the tweets:

```
  {
    "tweet" : {
      "edit_info" : {
        "initial" : {
          "editTweetIds" : [
            "1593006617125326848"
          ],
          "editableUntil" : "2022-11-16T22:52:28.811Z",
          "editsRemaining" : "5",
          "isEditEligible" : false
        }
      },
      "retweeted" : false,
      "source" : "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
      "entities" : {
        "hashtags" : [ ],
        "symbols" : [ ],
        "user_mentions" : [
          {
            "name" : "CRKN RCDR",
            "screen_name" : "CRKN_RCDR",
            "indices" : [
              "3",
              "13"
            ],
            "id_str" : "813991658",
            "id" : "813991658"
          },
          {
            "name" : "McGill Library",
            "screen_name" : "McGillLib",
            "indices" : [
              "36",
              "46"
            ],
            "id_str" : "21223663",
            "id" : "21223663"
          }
        ],
        "urls" : [ ]
      },
      "display_text_range" : [
        "0",
        "140"
      ],
      "favorite_count" : "0",
      "id_str" : "1593006617125326848",
      "truncated" : false,
      "retweet_count" : "0",
      "id" : "1593006617125326848",
      "created_at" : "Wed Nov 16 22:22:28 +0000 2022",
      "favorited" : false,
      "full_text" : "RT @CRKN_RCDR: 🗺In partnership with @McGillLib, we have added approximately 22,000 digitized Canadian maps to the Canadiana Collection. It’…",
      "lang" : "en"
    }
  },
  ```
  Extract example using [JQ](https://stedolan.github.io/jq/): 
  
  `cat tweets.json | jq '.[].tweet.id' > tweetsID.json`
 
  `cat tweets.json | jq '.[].tweet.created_at' > tweetsdates.json`
  
  and dump in a csv . . . 

6. Clean up the .csv (see example and sort by date) - I split the csv into multiple sheets and pulled tweets by year.

7. Put the the `.csv` in the same directory as the python script

8. Execute 

9. Combine pdfs - ghostscript 


