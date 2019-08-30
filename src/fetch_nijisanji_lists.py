from src.tweepy_wrapper import api

screen_name = "nijisanji_app"
for twilist in api.lists_all(screen_name=screen_name):
    print("slug=" + twilist.slug)
    print("name=" + twilist.name)

# slug=list
# name=【公式】にじさんじ統合以降
# slug=list1
# name=【公式・全体】にじさんじ
# slug=seeds1
# name=【公式】にじさんじSEEDs出身
# slug=list2
# name=【公式】にじさんじゲーマーズ出身
# slug=1-21
# name=【公式】にじさんじ1・2期出身
