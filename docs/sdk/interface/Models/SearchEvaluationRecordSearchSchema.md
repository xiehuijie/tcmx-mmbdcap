# SearchEvaluationRecordSearchSchema
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **filter\_id** | **String** | 保存了过滤条件的对应ID，一般由&#x60;search&#x60;类接口创建，并在后续的&#x60;list&#x60;类接口中使用 | [optional] [default to null] |
| **name** | **String** | 评测项名称 | [optional] [default to null] |
| **subject** | **String** | 一个由16位十六进制字符构成的字符串，代表一名受试者在该系统内的唯一标识 | [optional] [default to null] |
| **evaluation** | **String** | 评测项ID | [optional] [default to null] |
| **release** | **String** | 一个由16位十六进制字符构成的字符串，代项评测发布版本在该系统内的唯一标识 | [optional] [default to null] |
| **unit** | **String** | 一个由16位十六进制字符构成的字符串，代表一个组织机构在该系统内的唯一标识 | [optional] [default to null] |
| **user** | **String** | 一个由16位十六进制字符构成的字符串，代表一名用户在该系统内的唯一标识 | [optional] [default to null] |
| **device** | **String** | 一个由16位十六进制字符构成的字符串，代表一台设备在该系统内的唯一标识 | [optional] [default to null] |
| **create\_time** | [**List**](SearchEvaluationRecordSearchSchema_create_time_inner.md) | 用于搜索的创建时间范围 | [optional] [default to null] |
| **update\_time** | [**List**](SearchEvaluationRecordSearchSchema_update_time_inner.md) | 用于搜索的更新时间范围 | [optional] [default to null] |
| **tag** | **String** | 用于搜索的标签信息 | [optional] [default to null] |
| **indicator** | **List** | 用于搜索的指标信息，长度为2的数组，第一个元素为指标名称，第二个元素为指标值 | [optional] [default to null] |
| **marker** | **List** | 用于搜索的标记信息，长度为2的数组，第一个元素为标记名称，第二个元素为标记值 | [optional] [default to null] |
| **client\_version** | **String** | 客户端版本号 | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

