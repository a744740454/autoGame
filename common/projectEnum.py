import enum


# 1.在售 2.训练中 3.是否售出 4.刚刚录入，未走实名 5.未过新手教程

class GameAccountStatusEnum(enum.Enum):
    mailing = '1'  # 在售
    training = '2'  # 训练中
    sold = '3'  # 是否售出
    recently_added = '4'  # 刚刚录入，未走实名
    not_completed_tutorial = '5'  # 未过新手教程

    @classmethod
    def get_status_by_number(cls, number):
        # 通过数字返回中文状态
        status_mapping = {
            '1': '在售',
            '2': '训练中',
            '3': '是否售出',
            '4': '刚刚录入，未走实名',
            '5': '未过新手教程'
        }
        return status_mapping.get(str(number), '未知状态')  # 默认为 '未知状态' 如果没有找到对应的数字


class GameTypeEnum(enum.Enum):
    fate = '0'  # fgo

    @classmethod
    def get_status_by_number(cls, number):
        # 通过数字返回中文状态
        status_mapping = {
            '0': 'fate'
        }
        return status_mapping.get(str(number), '未知游戏')


class IdCardStatusEnum(enum.Enum):
    has_effectiveness = '0'  # 失效
    lose_effectiveness = '1'  # 失效

    @classmethod
    def get_status_by_number(cls, number):
        # 通过数字返回中文状态
        status_mapping = {
            '0': '有效',
            '1': '失效'
        }
        return status_mapping.get(str(number), '未知状态')
