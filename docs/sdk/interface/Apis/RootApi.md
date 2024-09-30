# RootApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ping**](RootApi.md#ping) | **GET** /ping | 网络测试 |
| [**redirect**](RootApi.md#redirect) | **GET** /r/{target} | 重定向 |
| [**root**](RootApi.md#root) | **GET** / | 根路由 |


<a name="ping"></a>
# **ping**
> PingSuccessResponse ping()

网络测试

    测试网络连通性，无需登录与签名校验

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingSuccessResponse**](../Models/PingSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="redirect"></a>
# **redirect**
> redirect(target)

重定向

    对请求重定向，一般用于长链转短链

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **target** | **String**|  | [default to null] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json

<a name="root"></a>
# **root**
> RootSuccessResponse root()

根路由

    根路由接口

### Parameters
This endpoint does not need any parameter.

### Return type

[**RootSuccessResponse**](../Models/RootSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

