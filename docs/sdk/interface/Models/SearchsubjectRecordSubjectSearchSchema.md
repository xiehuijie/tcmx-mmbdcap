# SearchsubjectRecordSubjectSearchSchema
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **filter\_id** | **String** | 保存了过滤条件的对应ID，一般由&#x60;search&#x60;类接口创建，并在后续的&#x60;list&#x60;类接口中使用 | [optional] [default to null] |
| **group** | **String** | 受试者的分组 | [optional] [default to null] |
| **source** | **String** | 受试者的来源 | [optional] [default to null] |
| **name** | **String** | 受试者的姓名 | [optional] [default to null] |
| **gender** | **String** | 受试者的性别 | [optional] [default to null] |
| **birthday** | [**List**](SearchsubjectRecordSubjectSearchSchema_birthday_inner.md) | 用于搜索的受试者的出生日期范围 | [optional] [default to null] |
| **create\_user** | **String** | 一个由16位十六进制字符构成的字符串，代表一名用户在该系统内的唯一标识 | [optional] [default to null] |
| **exact\_birthday** | **Boolean** | 受试者的出生日期是否精确 | [optional] [default to null] |
| **create\_time** | [**List**](SearchEvaluationRecordSearchSchema_create_time_inner.md) | 用于搜索的创建时间范围 | [optional] [default to null] |
| **update\_time** | [**List**](SearchEvaluationRecordSearchSchema_update_time_inner.md) | 用于搜索的更新时间范围 | [optional] [default to null] |
| **tag** | **String** | 用于搜索的标签信息 | [optional] [default to null] |
| **marker** | **List** | 用于搜索的标记信息，长度为2的数组，第一个元素为标记名称，第二个元素为标记值 | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

