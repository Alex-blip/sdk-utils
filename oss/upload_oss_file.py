# encoding=utf-8
__author__ = "lmy"

import oss2

yourAccessKeyId = "yourAccessKeyId"  # 通过账号获得accessKey
yourAccessKeySecret = "yourAccessKeySecret"  # 通过账号获得secretAccessKey
yourBucketName = "yourBucketName"  # 你的bucket名
yourObjectName = "yourObjectName"


def upload_oss_file(key):
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'

    auth = oss2.Auth(yourAccessKeyId, yourAccessKeySecret)
    bucket = oss2.Bucket(auth, endpoint, yourBucketName)
    current_fold = time.strftime('%Y-%m-%d', time.localtime())
    current_file_path = yourObjectName + key
    file_path = '你的项目路径' + key
    # 上传
    bucket.put_object_from_file(current_file_path, file_path)


key = '文件名'
upload_oss_file(key)
