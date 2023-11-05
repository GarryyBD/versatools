config = {
    "AdScraper": {
        "ad_format": "vertical",
        "max_generations": 20,
        "use_proxy": False,
        "max_workers": None
    },
    "AssetsDownloader": {
        "remove_trademark": True,
        "//sorts": ["relevance", "favouritedalltime", "favouritedallweek", "favouritedallday", "bestsellingalltime", "bestsellingweek", "bestsellingday", "recentlycreated", "pricehightolow", "pricelowtohigh"],
        "sort": "relevance",
        "keyword": "red",
        "asset_type": "shirt",
        "max_generations": 20,
        "use_proxy": False,
        "max_workers": None
    },
    "AssetsUploader": {
        "cookie": "_|WARNING:",
        "robux_price": 5,
        "description": "Made by a goat (me)",
        "group_id": 0,
        "use_proxy": False,
        "max_workers": None,
        "timeout": 45
    },
    "CommentBot": {
        "asset_id": 0,
        "max_generations": 1000,
        "captcha_solver": "capbypass",
        "use_proxy": True,
        "max_workers": 50
    },
    "CookieChecker": {
        "delete_invalid_cookies": False,
        "use_proxy": True,
        "max_workers": None
    },
    "CookieGenerator": {
        "max_generations": 1000,
        "captcha_solver": "capbypass",
        "use_proxy": True,
        "max_workers": 50
    },
    "CookieRefresher": {
        "use_proxy": True,
        "max_workers": None
    },
    "CookieVerifier": {
        "use_proxy": True,
        "max_workers": None
    },
    "DisplayNameChanger": {
        "new_display_name": "VersatoolsBEST",
        "use_proxy": True,
        "max_workers": None
    },
    "FavoriteBot": {
        "asset_id": 0,
        "unfavorite": False,
        "max_generations": 500,
        "use_proxy": True,
        "max_workers": 50,
        "timeout": 0
    },
    "FollowBot": {
        "user_id": 1,
        "max_generations": 100,
        "captcha_solver": "capbypass",
        "use_proxy": True,
        "max_workers": 50
    },
    "FriendRequestBot": {
        "user_id": 1,
        "max_generations": 1000,
        "use_proxy": True,
        "max_workers": None
    },
    "FunCaptchaSolvers": {
        "//solvers_name": [
            "anti-captcha",
            "2captcha",
            "capsolver",
            "capbypass"
        ],
        "anti-captcha_token": "xx",
        "2captcha_token": "xx",
        "capsolver_token": "xx",
        "capbypass": "xx"
    },
    "GameVote": {
        "game_id": 0,
        "dislike": False,
        "max_generations": 100,
        "use_proxy": True,
        "max_workers": None
    },
    "Gen2018Acc": {
        "use_proxy": False
    },
    "GroupJoinBot": {
        "group_id": 0,
        "max_generations": 100,
        "captcha_solver": "capbypass",
        "use_proxy": True,
        "max_workers": 50
    },
    "MessageBot": {
        "recipient_id": 1,
        "subject": "Hello",
        "body": "Hey there! I'm a bot :D\n\nCan you please follow me?",
        "max_generations": 100,
        "use_proxy": True,
        "max_workers": None
    },
    "ModelSales": {
        "asset_id": 0,
		"max_generations": 100,
		"use_proxy": True,
		"max_workers": None
	},
    "ModelVote": {
        "model_id": 0,
        "dislike": False,
        "max_generations": 100,
        "use_proxy": True,
        "max_workers": None
    },
    "ProxyChecker": {
        "delete_failed_proxies": True,
        "timeout": 2,
        "max_workers": None
    },
    "StatusChanger": {
        "new_status": "Hello I'm a bot :D",
        "use_proxy": True,
        "max_workers": None
    },
    "T-ShirtGenerator": {
        "query": "elon musk",
        "//image_search_api_url": "https://rapidapi.com/emailmatteoutile/api/image-search-api2",
        "image_search_api_key": "xx"
    }
}