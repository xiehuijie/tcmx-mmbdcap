# FileApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUploadTask**](FileApi.md#createUploadTask) | **POST** /file/upload | 创建上传任务 |
| [**getFileDirectLink**](FileApi.md#getFileDirectLink) | **GET** /file/{file_id}/directLink | 获取文件直链 |
| [**getTusConfig**](FileApi.md#getTusConfig) | **OPTIONS** /file/upload | 获取Tus协议配置 |
| [**getUploadInfo**](FileApi.md#getUploadInfo) | **HEAD** /file/upload/{file_id} | 上传文件 |
| [**uploadFileChunk**](FileApi.md#uploadFileChunk) | **PATCH** /file/upload/{file_id} | 上传文件 |
| [**uploadFilePrecheck**](FileApi.md#uploadFilePrecheck) | **POST** /file/upload/precheck | 文件上传预检 |


<a name="createUploadTask"></a>
# **createUploadTask**
> createUploadTask(upload-metadata, upload-length)

创建上传任务

    基于Tus协议，创建一个上传任务

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **upload-metadata** | **String**|  | [default to null] |
| **upload-length** | **Integer**|  | [default to null] |

### Return type

null (empty response body)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getFileDirectLink"></a>
# **getFileDirectLink**
> GetFileDirectLinkSuccessResponse getFileDirectLink(file\_id)

获取文件直链

    获取文件下载直链直链

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file\_id** | **String**|  | [default to null] |

### Return type

[**GetFileDirectLinkSuccessResponse**](../Models/GetFileDirectLinkSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTusConfig"></a>
# **getTusConfig**
> getTusConfig()

获取Tus协议配置

    获取Tus协议配置信息

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUploadInfo"></a>
# **getUploadInfo**
> getUploadInfo(file\_id)

上传文件

    &#x60;Tus协议&#x60;，获取文件头

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file\_id** | **String**|  | [default to null] |

### Return type

null (empty response body)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="uploadFileChunk"></a>
# **uploadFileChunk**
> uploadFileChunk(file\_id, content-length, upload-offset, upload-checksum)

上传文件

    &#x60;Tus协议&#x60;，上传文件分片

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file\_id** | **String**|  | [default to null] |
| **content-length** | **Integer**|  | [default to null] |
| **upload-offset** | **Integer**|  | [default to null] |
| **upload-checksum** | **String**|  | [default to null] |

### Return type

null (empty response body)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="uploadFilePrecheck"></a>
# **uploadFilePrecheck**
> UploadFilePrecheckSuccessResponse uploadFilePrecheck(UploadFilePrecheckBody)

文件上传预检

    文件上传预检，判断文件是否已上传过，或是否能断点续传

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **UploadFilePrecheckBody** | [**UploadFilePrecheckBody**](../Models/UploadFilePrecheckBody.md)|  | |

### Return type

[**UploadFilePrecheckSuccessResponse**](../Models/UploadFilePrecheckSuccessResponse.md)

### Authorization

[SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

