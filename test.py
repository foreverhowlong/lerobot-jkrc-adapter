import jkrc

ROBOT_IP = "10.5.5.100"
robot = jkrc.RC(ROBOT_IP)
tool_id = robot.get_tool_id()
print(f"tool id:{tool_id}")
print(robot.get_tool_data(tool_id))