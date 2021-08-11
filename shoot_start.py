





# 项目模块
import mod_shoot.lib.net_mgr as NetMgr
import mod_shoot.lib.actor_mgr as ActorMgr


def run():
    # 服务器初始化
    # 初始化角色管理器
    actor_mgr = ActorMgr.ActorMgr()
    # 初始化网络管理器
    net_mgr = NetMgr.NetMgr(actor_mgr)

    # 循环
    while(1):
        # 网络循环
        net_mgr.run()

        # 系统功能跑一个循环

        pass

    pass


# 服务器运行
run()








