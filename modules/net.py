# 官方库
import socket
import select



# 网络库




# 网络管理器
class Net(object):
    ser_socket = None   # 服务器套接字
    inputs = []         # 输入监听列表

    def __init__(self, path, port):
        # 初始化套接字
        serversocket = socket.socket() 
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0.1)
        serversocket.bind((path, port))
        serversocket.listen(5)
        self.ser_socket = serversocket
        self.inputs = [serversocket]
    
    def select(self):
        r_list, _, e_list = select.select(self.inputs, [], self.inputs, 0.5)
        recv_list = []  # 有数据可读取的列表
        err_list = []   # 错误列表
        for sk1_or_conn in r_list:
            # 每一个连接对象
            if sk1_or_conn == self.ser_socket:
                # 表示有新用户来连接
                conn, address = sk1_or_conn.accept()
                self.inputs.append(conn)
            else:
                # 有老用户发消息了
                try:
                    recv_list.append(sk1_or_conn)
                    # data_bytes = sk1_or_conn.recv(1024)
                    # 对数据操作

                except Exception as ex:
                    # 如果用户终止连接
                    self.inputs.remove(sk1_or_conn)
                    err_list.append(sk1_or_conn)

            for sk in e_list:
                self.inputs.remove(sk)
                err_list.append(sk1_or_conn)

        return recv_list,err_list
