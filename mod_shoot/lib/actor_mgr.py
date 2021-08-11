# 框架库


# 项目模块
import config.proto as ProtoCfg
import proto.login as LoginMd


all_proto = {
    "login" : LoginMd
}



# 角色管理器
class ActorMgr():
    # 角色对象map
    actor_map = {}

    def __init__(self):
        # 角色对象map
        self.actor_map = {}
        
    # 处理协议
    def do_msg(self, net_actor, msg):
        try:
            proto_id = msg["proto_id"]
            msg_id = msg["msg_id"]
            # 获取模块，函数
            proto = ProtoCfg[proto_id]["proto"]
            fun_name = ProtoCfg[proto_id][msg_id]["fun"]
            f = getattr(all_proto[proto], fun_name)
            # 未登录，要先登录
            if not net_actor.is_login:
                if proto_id != 1 or msg_id != 1:
                    return False, "请先登录"
                # 登录
                ret,Actor = f(msg)
                if ret:
                    self.actor_map[Actor.actor_id] = Actor
                    net_actor.actor_id = Actor.actor_id
                    net_actor.is_login = True
            else:
                # 正常走协议流程
                f(net_actor, msg)
            return True, ""
        except Exception as err:
            print(err)
            return True, ""
        
    # 关闭角色
    def close_actor(self, net_actor):
        # 未登录直接退出
        if not net_actor.is_login:
            if net_actor.actor_id not in self.actor_map:
                return
            else:
                # 关闭后删除对象
                actor = self.actor_map[net_actor.actor_id]
                actor.close()
                del self.actor_map[net_actor.actor_id]

        
















