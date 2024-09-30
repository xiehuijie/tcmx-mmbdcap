# EvaluationApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEvaluation**](EvaluationApi.md#createEvaluation) | **PUT** /evaluation | 创建评测项 |
| [**createEvaluationRecord**](EvaluationApi.md#createEvaluationRecord) | **PUT** /evaluation/record | 创建评测记录 |
| [**createEvaluationRelease**](EvaluationApi.md#createEvaluationRelease) | **PUT** /evaluation/{evaluation_id}/release | 创建评测项发布版本 |
| [**deleteEvaluation**](EvaluationApi.md#deleteEvaluation) | **DELETE** /evaluation/{evaluation_id} | 删除评测项 |
| [**deleteEvaluationRecord**](EvaluationApi.md#deleteEvaluationRecord) | **DELETE** /evaluation/record/{evaluation_record_id} | 删除评测记录 |
| [**deleteEvaluationRelease**](EvaluationApi.md#deleteEvaluationRelease) | **DELETE** /evaluation/release/{release_id} | 删除评测项发布版本 |
| [**getEvaluationAnalyzer**](EvaluationApi.md#getEvaluationAnalyzer) | **GET** /evaluation/analyzer/{analyzer_id} | 获取评测记录分析器详情 |
| [**getEvaluationAnalyzerList**](EvaluationApi.md#getEvaluationAnalyzerList) | **GET** /evaluation/release/{release_id}/analyzer | 获取适用的分析器摘要列表 |
| [**getEvaluationDetail**](EvaluationApi.md#getEvaluationDetail) | **GET** /evaluation/{evaluation_id} | 获取评测项详情 |
| [**getEvaluationList**](EvaluationApi.md#getEvaluationList) | **GET** /evaluation/list | 获取评测项列表 |
| [**getEvaluationRecord**](EvaluationApi.md#getEvaluationRecord) | **GET** /evaluation/record/{evaluation_record_id} | 获取评测记录 |
| [**getEvaluationRecordBriefList**](EvaluationApi.md#getEvaluationRecordBriefList) | **GET** /evaluation/record/list | 获取评测记录列表 |
| [**getEvaluationReleaseAnalyzerList**](EvaluationApi.md#getEvaluationReleaseAnalyzerList) | **GET** /evaluation/release/{release_id}/python | 获取评测发布项Python文件 |
| [**getEvaluationReleaseList**](EvaluationApi.md#getEvaluationReleaseList) | **GET** /evaluation/{evaluation_id}/release/list | 获取评测项发布版本列表 |
| [**getEvaluationReleaseProto**](EvaluationApi.md#getEvaluationReleaseProto) | **GET** /evaluation/release/{release_id}/proto | 获取评测发布项Proto文件 |
| [**searchEvaluationRecord**](EvaluationApi.md#searchEvaluationRecord) | **POST** /evaluation/record/search | 搜索评测记录 |
| [**updateEvaluation**](EvaluationApi.md#updateEvaluation) | **PATCH** /evaluation/{evaluation_id} | 更新评测项 |
| [**updateEvaluationRelease**](EvaluationApi.md#updateEvaluationRelease) | **PATCH** /evaluation/release/{release_id} | 更新评测项发布版本 |
| [**uploadEvaluationRecord**](EvaluationApi.md#uploadEvaluationRecord) | **PATCH** /evaluation/record/{evaluation_record_id} | 更新评测记录 |


<a name="createEvaluation"></a>
# **createEvaluation**
> CreateEvaluationSuccessResponse createEvaluation(CreateEvaluationBody)

创建评测项

    创建评测项，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateEvaluationBody** | [**CreateEvaluationBody**](../Models/CreateEvaluationBody.md)|  | |

### Return type

[**CreateEvaluationSuccessResponse**](../Models/CreateEvaluationSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createEvaluationRecord"></a>
# **createEvaluationRecord**
> CreateEvaluationRecordSuccessResponse createEvaluationRecord(CreateEvaluationRecordBody)

创建评测记录

    创建评测记录

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateEvaluationRecordBody** | [**CreateEvaluationRecordBody**](../Models/CreateEvaluationRecordBody.md)|  | |

### Return type

[**CreateEvaluationRecordSuccessResponse**](../Models/CreateEvaluationRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createEvaluationRelease"></a>
# **createEvaluationRelease**
> CreateEvaluationReleaseSuccessResponse createEvaluationRelease(evaluation\_id, CreateEvaluationReleaseBody)

创建评测项发布版本

    创建评测项发布版本，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_id** | **String**|  | [default to null] |
| **CreateEvaluationReleaseBody** | [**CreateEvaluationReleaseBody**](../Models/CreateEvaluationReleaseBody.md)|  | |

### Return type

[**CreateEvaluationReleaseSuccessResponse**](../Models/CreateEvaluationReleaseSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="deleteEvaluation"></a>
# **deleteEvaluation**
> DeleteEvaluationSuccessResponse deleteEvaluation(evaluation\_id)

删除评测项

    删除评测项，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_id** | **String**|  | [default to null] |

### Return type

[**DeleteEvaluationSuccessResponse**](../Models/DeleteEvaluationSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="deleteEvaluationRecord"></a>
# **deleteEvaluationRecord**
> DeleteEvaluationRecordSuccessResponse deleteEvaluationRecord(evaluation\_record\_id)

删除评测记录

    删除评测记录

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_record\_id** | **String**|  | [default to null] |

### Return type

[**DeleteEvaluationRecordSuccessResponse**](../Models/DeleteEvaluationRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="deleteEvaluationRelease"></a>
# **deleteEvaluationRelease**
> DeleteEvaluationReleaseSuccessResponse deleteEvaluationRelease(release\_id)

删除评测项发布版本

    删除评测项发布版本，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **release\_id** | **String**|  | [default to null] |

### Return type

[**DeleteEvaluationReleaseSuccessResponse**](../Models/DeleteEvaluationReleaseSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationAnalyzer"></a>
# **getEvaluationAnalyzer**
> GetEvaluationAnalyzerSuccessResponse getEvaluationAnalyzer(analyzer\_id)

获取评测记录分析器详情

    获取评测分析器

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **analyzer\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationAnalyzerSuccessResponse**](../Models/GetEvaluationAnalyzerSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationAnalyzerList"></a>
# **getEvaluationAnalyzerList**
> GetEvaluationAnalyzerListSuccessResponse getEvaluationAnalyzerList(release\_id)

获取适用的分析器摘要列表

    获取适用于该评测发布版本的评测记录分析器

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **release\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationAnalyzerListSuccessResponse**](../Models/GetEvaluationAnalyzerListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationDetail"></a>
# **getEvaluationDetail**
> GetEvaluationDetailSuccessResponse getEvaluationDetail(evaluation\_id)

获取评测项详情

    获取评测项详情

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationDetailSuccessResponse**](../Models/GetEvaluationDetailSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationList"></a>
# **getEvaluationList**
> GetEvaluationListSuccessResponse getEvaluationList(page\_number, page\_size)

获取评测项列表

    获取评测项列表

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page\_number** | **Integer**|  | [default to null] |
| **page\_size** | **Integer**|  | [default to null] |

### Return type

[**GetEvaluationListSuccessResponse**](../Models/GetEvaluationListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationRecord"></a>
# **getEvaluationRecord**
> GetEvaluationRecordSuccessResponse getEvaluationRecord(evaluation\_record\_id)

获取评测记录

    获取评测记录

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_record\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationRecordSuccessResponse**](../Models/GetEvaluationRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationRecordBriefList"></a>
# **getEvaluationRecordBriefList**
> GetEvaluationRecordBriefListSuccessResponse getEvaluationRecordBriefList(page\_number, page\_size, filter\_id, order\_by, sort\_mode)

获取评测记录列表

    获取评测记录列表，支持传入一个&#x60;fliter_id&#x60;作为筛选条件，详见[&#x60;搜索评测记录&#x60;](/dr?m&#x3D;evaluation&amp;i&#x3D;SearchEvaluationRecord)接口

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page\_number** | **Integer**|  | [optional] [default to 1] |
| **page\_size** | **Integer**|  | [optional] [default to 20] |
| **filter\_id** | **String**|  | [optional] [default to null] |
| **order\_by** | **String**|  | [optional] [default to update_time] [enum: create_time, update_time] |
| **sort\_mode** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**GetEvaluationRecordBriefListSuccessResponse**](../Models/GetEvaluationRecordBriefListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationReleaseAnalyzerList"></a>
# **getEvaluationReleaseAnalyzerList**
> GetEvaluationReleaseAnalyzerListSuccessResponse getEvaluationReleaseAnalyzerList(release\_id)

获取评测发布项Python文件

    获取评测项发布版本的python文件

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **release\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationReleaseAnalyzerListSuccessResponse**](../Models/GetEvaluationReleaseAnalyzerListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationReleaseList"></a>
# **getEvaluationReleaseList**
> GetEvaluationReleaseListSuccessResponse getEvaluationReleaseList(evaluation\_id)

获取评测项发布版本列表

    获取评测项发布版本列表

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationReleaseListSuccessResponse**](../Models/GetEvaluationReleaseListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getEvaluationReleaseProto"></a>
# **getEvaluationReleaseProto**
> GetEvaluationReleaseProtoSuccessResponse getEvaluationReleaseProto(release\_id)

获取评测发布项Proto文件

    获取评测项发布版本的protobuf文件

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **release\_id** | **String**|  | [default to null] |

### Return type

[**GetEvaluationReleaseProtoSuccessResponse**](../Models/GetEvaluationReleaseProtoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="searchEvaluationRecord"></a>
# **searchEvaluationRecord**
> SearchEvaluationRecordSuccessResponse searchEvaluationRecord(mode, SearchEvaluationRecordSearchSchema, force)

搜索评测记录

    搜索评测记录，根据搜索条件，返回一个过滤器ID

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | **String**|  | [default to null] [enum: and, or] |
| **SearchEvaluationRecordSearchSchema** | [**SearchEvaluationRecordSearchSchema**](../Models/SearchEvaluationRecordSearchSchema.md)|  | |
| **force** | **Boolean**| 是否忽略搜索缓存 | [optional] [default to false] |

### Return type

[**SearchEvaluationRecordSuccessResponse**](../Models/SearchEvaluationRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="updateEvaluation"></a>
# **updateEvaluation**
> UpdateEvaluationSuccessResponse updateEvaluation(evaluation\_id, UpdateEvaluationBody)

更新评测项

    更新评测项，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_id** | **String**|  | [default to null] |
| **UpdateEvaluationBody** | [**UpdateEvaluationBody**](../Models/UpdateEvaluationBody.md)|  | |

### Return type

[**UpdateEvaluationSuccessResponse**](../Models/UpdateEvaluationSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="updateEvaluationRelease"></a>
# **updateEvaluationRelease**
> UpdateEvaluationReleaseSuccessResponse updateEvaluationRelease(release\_id, UpdateEvaluationReleaseBody)

更新评测项发布版本

    更新评测项发布版本，该接口仅系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **release\_id** | **String**|  | [default to null] |
| **UpdateEvaluationReleaseBody** | [**UpdateEvaluationReleaseBody**](../Models/UpdateEvaluationReleaseBody.md)|  | |

### Return type

[**UpdateEvaluationReleaseSuccessResponse**](../Models/UpdateEvaluationReleaseSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="uploadEvaluationRecord"></a>
# **uploadEvaluationRecord**
> UploadEvaluationRecordSuccessResponse uploadEvaluationRecord(evaluation\_record\_id, UploadEvaluationRecordBody)

更新评测记录

    更新评测记录

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **evaluation\_record\_id** | **String**|  | [default to null] |
| **UploadEvaluationRecordBody** | [**UploadEvaluationRecordBody**](../Models/UploadEvaluationRecordBody.md)|  | |

### Return type

[**UploadEvaluationRecordSuccessResponse**](../Models/UploadEvaluationRecordSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

