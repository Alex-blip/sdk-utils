# -*- coding: UTF-8 -*-
__author__ = "lmy"

from qcloudsms_py import SmsMultiSender, SmsSingleSender

appId = "appId"  # 自己应用ID
appKey = "appKey"  # 自己应用Key
sms_sign = "sms_sign"  # 你的签名名称
tpl_id = "tpl_id"  # 模板id


def send_sms_single(phone_num,  template_param_list):
    """
    单条发送短信
    :param phone_num: 手机号
    :param template_param_list: 短信模板所需参数列表，例如:[123456,543210]
    :return:
    """
    sender = SmsSingleSender(appId, appKey)
    response = sender.send_with_param(86, phone_num, tpl_id, template_param_list, sign=sms_sign)
    return response


if __name__ == '__main__':
    send_sms_single(18790334713, ["123456"])
