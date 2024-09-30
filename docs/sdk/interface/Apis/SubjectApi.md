# SubjectApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSubject**](SubjectApi.md#createSubject) | **PUT** /subject | 创建受试者 |
| [**deleteSubject**](SubjectApi.md#deleteSubject) | **DELETE** /subject/{subject_id} | 删除受试者 |
| [**getSubjectBriefList**](SubjectApi.md#getSubjectBriefList) | **GET** /subject/list | 获取受试者摘要列表 |
| [**getSubjectDetail**](SubjectApi.md#getSubjectDetail) | **GET** /subject/{subject_id} | 获取受试者详情 |
| [**searchsubjectRecord**](SubjectApi.md#searchsubjectRecord) | **POST** /subject/search | 搜索受试者 |
| [**updateSubject**](SubjectApi.md#updateSubject) | **PATCH** /subject/{subject_id} | 更新受试者 |


<a name="createSubject"></a>
# **createSubject**
> CreateSubjectSuccessResponse createSubject(CreateSubjectBody)

创建受试者

    创建受试者

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateSubjectBody** | [**CreateSubjectBody**](../Models/CreateSubjectBody.md)|  | |

### Return type

[**CreateSubjectSuccessResponse**](../Models/CreateSubjectSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="deleteSubject"></a>
# **deleteSubject**
> DeleteSubjectSuccessResponse deleteSubject(subject\_id)

删除受试者

    删除受试者

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subject\_id** | **String**|  | [default to null] |

### Return type

[**DeleteSubjectSuccessResponse**](../Models/DeleteSubjectSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSubjectBriefList"></a>
# **getSubjectBriefList**
> GetSubjectBriefListSuccessResponse getSubjectBriefList(page\_number, page\_size, filter\_id)

获取受试者摘要列表

    获取受试者摘要列表

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page\_number** | **Integer**|  | [default to null] |
| **page\_size** | **Integer**|  | [default to null] |
| **filter\_id** | **String**|  | [optional] [default to null] |

### Return type

[**GetSubjectBriefListSuccessResponse**](../Models/GetSubjectBriefListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSubjectDetail"></a>
# **getSubjectDetail**
> GetSubjectDetailSuccessResponse getSubjectDetail(subject\_id)

获取受试者详情

    获取受试者详情

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subject\_id** | **String**|  | [default to null] |

### Return type

[**GetSubjectDetailSuccessResponse**](../Models/GetSubjectDetailSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="searchsubjectRecord"></a>
# **searchsubjectRecord**
> SearchsubjectRecordSuccessResponse searchsubjectRecord(mode, SearchsubjectRecordSubjectSearchSchema, force)

搜索受试者

    搜索评测记录，根据搜索条件，返回一个过滤器ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | **String**|  | [default to null] [enum: and, or] |
| **SearchsubjectRecordSubjectSearchSchema** | [**SearchsubjectRecordSubjectSearchSchema**](../Models/SearchsubjectRecordSubjectSearchSchema.md)|  | |
| **force** | **Boolean**| 是否忽略搜索缓存 | [optional] [default to false] |

### Return type

[**SearchsubjectRecordSuccessResponse**](../Models/SearchsubjectRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="updateSubject"></a>
# **updateSubject**
> UpdateSubjectSuccessResponse updateSubject(subject\_id, UpdateSubjectBody)

更新受试者

    更新受试者

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subject\_id** | **String**|  | [default to null] |
| **UpdateSubjectBody** | [**UpdateSubjectBody**](../Models/UpdateSubjectBody.md)|  | |

### Return type

[**UpdateSubjectSuccessResponse**](../Models/UpdateSubjectSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

