

import lib.actor as ActorMd



# 登录请求
def login_quest(msg):
    account = msg["account"]

    # 验证账号密码
    actor = ActorMd.Actor()
    actor.account_id = account
    actor.actor_id = account
    return True, actor






















