# ScaleApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createScale**](ScaleApi.md#createScale) | **PUT** /scale | 创建量表 |
| [**getScaleDetail**](ScaleApi.md#getScaleDetail) | **GET** /scale/{scale_id} | 获取量表信息 |
| [**getScaleList**](ScaleApi.md#getScaleList) | **GET** /scale/list | 获取量表列表 |


<a name="createScale"></a>
# **createScale**
> CreateScaleSuccessResponse createScale()

创建量表

    创建量表，仅系统管理员可执行此操作

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateScaleSuccessResponse**](../Models/CreateScaleSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getScaleDetail"></a>
# **getScaleDetail**
> GetScaleDetailSuccessResponse getScaleDetail(scale\_id)

获取量表信息

    获取量表信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scale\_id** | **String**|  | [default to null] |

### Return type

[**GetScaleDetailSuccessResponse**](../Models/GetScaleDetailSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getScaleList"></a>
# **getScaleList**
> GetScaleListSuccessResponse getScaleList()

获取量表列表

    获取量表列表

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetScaleListSuccessResponse**](../Models/GetScaleListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

