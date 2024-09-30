# CreateEvaluationRecordBody
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **subject\_id** | **String** | 一个由16位十六进制字符构成的字符串，代表一名受试者在该系统内的唯一标识 | [default to null] |
| **device\_id** | **String** | 内部存储的设备ID | [default to null] |
| **release\_id** | **String** | 一个由16位十六进制字符构成的字符串，代项评测发布版本在该系统内的唯一标识 | [default to null] |
| **client\_version** | **String** | 客户端版本号 | [default to null] |
| **name** | **String** | 评测记录名称 | [default to null] |
| **data** | **String** | 评测记录数据，以Base64编码的表达，源二进制数据为&#x60;protobuf&#x60;编码的评测记录数据 | [default to null] |
| **create\_user** | **String** | 内部存储的用户ID | [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

