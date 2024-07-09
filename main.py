from arcadeApi import ArcadeApi

api = ArcadeApi(user_id="U07BBJR072P", save=True, debug=False)

api.start_session("Test")
# api.load_session("1720511635.084169")
api.pause_session()

# time.sleep(3)
# api.resume_session()

# print(api.get_time_left())
# api.post_reply("link")
# api.end_session()

# print(api.api.post_action("arcade", api.current_session_ts, "end"))
# print(api.api.submit_view("V07B558HGP8"))