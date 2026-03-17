import jkrc
import torch
import time

ROBOT_IP = "10.5.5.100"

class JakaLeRobotBridge:
    def __init__(self, ip=ROBOT_IP): 
        print(f"正在连接 JAKA 机器人 (IP: {ip})...")
        self.robot = jkrc.RC(ip)
        self.robot.login()
        self.robot.power_on()
        self.robot.enable_robot()
        print("机器人初始化成功！")

    def get_observation(self):
        """
        读取机器人的当前状态，并打包成 LeRobot 需要的字典格式
        """
        #返回格式：(err code,[q1,q2,q3,q4,q5,q6])
        ret, joint_pos = self.robot.get_joint_position()
        
        if ret == 0: 
                # 把 (j1, j2, j3, j4, j5, j6) 转成 Tensor
                pos_tensor = torch.tensor(joint_pos, dtype=torch.float32)
                return {
                    "observation.state": pos_tensor
                }
        else:
            raise RuntimeError(f"读取机器人数据失败，错误码：{ret}")
    def step(self, action_tensor):
        """
        接收 LeRobot 输出的动作，并让机器人执行
        """
        # 把Tensor转换回普通的Python列表
        # action_tensor应当是包含 6 个目标角度的张量
        target_joints = action_tensor.tolist()
        
        # 调用 Jaka API 执行动作
        """ 
        根据官网文档 joint_move(joint_pos, move_mode, is_block, speed)
        joint_pos: 机器人关节运动目标位置。
        move_mode: 0代表绝对运动，1代表相对运动
        is_block：设置接口是否为阻塞接口，TRUE 为阻塞接口 FALSE 为非阻塞接口。阻塞表示机器人运动完成才会有返回值，非阻塞表示接口调用完成立刻就有返回值。
        speed: 机器人关节运动速度，单位：rad/s
        acc: 关节加速度默认 12.56rad/s^2
        """
        self.robot.joint_move(
            joint_pos=target_joints,
            move_mode=0,
            is_block=False,
            speed=10) 

    def close(self):
        """安全退出"""
        self.robot.disable_robot()
        self.robot.power_off()
        self.robot.logout()
        print("已断开连接。")


if __name__ == "__main__":
    env = JakaLeRobotBridge(ROBOT_IP)
    
    obs = env.get_observation()
    print("喂给 LeRobot 的数据长这样:")
    print(obs)
    

    # time.sleep(1)
    # env.close()