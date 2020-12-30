# -*- coding: UTF-8 -*-
__author__ = "lmy"

import oss2
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


yourAccessKeyId = os.environ.get('yourAccessKeyId')  # 通过账号获得accessKey
yourAccessKeySecret = os.environ.get('yourAccessKeySecret')  # 通过账号获得secretAccessKey
yourBucketName = "y-home"  # 你的bucket名
endpoint = 'oss-cn-beijing.aliyuncs.com'


def uploadFileBytes(fileName, fileContent):
    """
    :param fileName: 文件名称
    :param fileContent: 文件二进制内容
    :return:
    """
    Folder = "upload"
    auth = oss2.Auth(yourAccessKeyId, yourAccessKeySecret)
    bucket = oss2.Bucket(auth, endpoint, yourBucketName, connect_timeout=30)
    result = bucket.put_object(Folder + '/' + fileName, fileContent)
    print(result)


