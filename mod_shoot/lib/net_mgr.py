# 官方库
import msgpack

# 框架库
import modules.net as Net

# 项目模块
import mod_shoot.config.net as NetCfg


# 网络对象
class NetActor():
    # 玩家id
    actor_id = 0
    # 是否完成登录
    is_login = False
    def __init__(self):
       self.actor_id = 0 
       self.is_login = False
        


# 网络管理器
class NetMgr():
    # 网络管理
    net = None
    # 已完成登录的链接
    actor_map = {}
    # 角色管理器
    actor_mgr = None

    def __init__(self, actor_mgr):
        # 网络
        self.net = Net.Net(NetCfg.path, NetCfg.port)
        self.actor_map = {}
        self.actor_mgr = actor_mgr
        
    # 跑一个循环
    def run(self):
        recv_list,err_list = self.net.select()
        # 关闭错误的对象
        for item in err_list:
            if item in self.actor_map:
                self.close_actor(item)
        # 读取协议
        for item in recv_list:
            ret,msg = self.recv_msg(item)
            if not ret:
                # 失败，关闭对象
                self.close_actor(item)
            else:
                # 创建网络对象
                if item not in self.actor_map:
                    net_actor = NetActor()
                    self.actor_map[item] = net_actor
                # 处理协议
                self.actor_mgr.do_msg(self.actor_map[item], msg)
    
    # 关闭网络对象
    def close_actor(self, key):
        net_actor = self.actor_map[key]
        self.actor_mgr.close_actor(net_actor)
        del self.actor_map[key]

    # 读取协议
    def recv_msg(self, s):
        # 先接受包大小
        msg = s.recv(4)
        # 字节转int
        msg_len = int.from_bytes(msg, byteorder='big')
        self.get_recv_len(msg_len)

    # 接受指定数量字节
    def get_recv_len(s, recv_len):
        try:
            one_len = 2048
            get_len = 0
            msg = b''
            while True:
                if recv_len - get_len > one_len:
                    get_len += one_len
                    msg += s.recv(one_len)
                else:
                    msg += s.recv(recv_len - get_len)
                    get_len += (recv_len - get_len)
                    break
            # 解包
            msg = msgpack.unpackb(msg)
            return True,msg
        except Exception as err:
            print(err)
            return False,""
        
















