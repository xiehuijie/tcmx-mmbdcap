# UnitApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRegistrationCode**](UnitApi.md#createRegistrationCode) | **PUT** /unit/{unit_id}/registration_code | 生成注册码 |
| [**createUnit**](UnitApi.md#createUnit) | **PUT** /unit | 创建单位 |
| [**deleteRegistrationCode**](UnitApi.md#deleteRegistrationCode) | **DELETE** /unit/{unit_id}/registration_code/{code} | 删除注册码 |
| [**deleteUnit**](UnitApi.md#deleteUnit) | **DELETE** /unit/{unit_id} | 移除单位 |
| [**getRegistrationCodeList**](UnitApi.md#getRegistrationCodeList) | **GET** /unit/{unit_id}/registration_code/list | 获取注册码列表 |
| [**getUnitConfig**](UnitApi.md#getUnitConfig) | **GET** /unit/{unit_id}/config | 获取单位配置 |
| [**getUnitDetail**](UnitApi.md#getUnitDetail) | **GET** /unit/{unit_id} | 获取单位详细信息 |
| [**getUnitDeviceList**](UnitApi.md#getUnitDeviceList) | **GET** /unit/{unit_id}/device_list | 获取单位下设备摘要 |
| [**getUnitList**](UnitApi.md#getUnitList) | **GET** /unit/list | 获取单位列表 |
| [**getUnitUserList**](UnitApi.md#getUnitUserList) | **GET** /unit/{unit_id}/user_list | 获取单位下用户摘要 |
| [**updateUnitConfig**](UnitApi.md#updateUnitConfig) | **PATCH** /unit/{unit_id}/config | 更新单位配置 |
| [**updateUnitInfo**](UnitApi.md#updateUnitInfo) | **PATCH** /unit/{unit_id} | 更新单位信息 |


<a name="createRegistrationCode"></a>
# **createRegistrationCode**
> CreateRegistrationCodeSuccessResponse createRegistrationCode(unit\_id)

生成注册码

    生成注册码，该接口只有单位管理员才有权限调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**CreateRegistrationCodeSuccessResponse**](../Models/CreateRegistrationCodeSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="createUnit"></a>
# **createUnit**
> CreateUnitSuccessResponse createUnit(CreateUnitBody)

创建单位

    创建单位，该接口仅有系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateUnitBody** | [**CreateUnitBody**](../Models/CreateUnitBody.md)|  | |

### Return type

[**CreateUnitSuccessResponse**](../Models/CreateUnitSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="deleteRegistrationCode"></a>
# **deleteRegistrationCode**
> DeleteRegistrationCodeSuccessResponse deleteRegistrationCode(unit\_id, code)

删除注册码

    删除注册码，该接口只有单位管理员才有权限调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |
| **code** | **String**|  | [default to null] |

### Return type

[**DeleteRegistrationCodeSuccessResponse**](../Models/DeleteRegistrationCodeSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="deleteUnit"></a>
# **deleteUnit**
> DeleteUnitSuccessResponse deleteUnit(unit\_id)

移除单位

    移除单位，该接口仅有系统管理员才可调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**DeleteUnitSuccessResponse**](../Models/DeleteUnitSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRegistrationCodeList"></a>
# **getRegistrationCodeList**
> GetRegistrationCodeListSuccessResponse getRegistrationCodeList(unit\_id)

获取注册码列表

    获取注册码列表，该接口只有单位管理员才有权限调用

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**GetRegistrationCodeListSuccessResponse**](../Models/GetRegistrationCodeListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUnitConfig"></a>
# **getUnitConfig**
> GetUnitConfigSuccessResponse getUnitConfig(unit\_id)

获取单位配置

    获取单位配置

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**GetUnitConfigSuccessResponse**](../Models/GetUnitConfigSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUnitDetail"></a>
# **getUnitDetail**
> GetUnitDetailSuccessResponse getUnitDetail(unit\_id)

获取单位详细信息

    获取单位信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**GetUnitDetailSuccessResponse**](../Models/GetUnitDetailSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUnitDeviceList"></a>
# **getUnitDeviceList**
> GetUnitDeviceListSuccessResponse getUnitDeviceList(unit\_id)

获取单位下设备摘要

    获取单位信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**GetUnitDeviceListSuccessResponse**](../Models/GetUnitDeviceListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUnitList"></a>
# **getUnitList**
> GetUnitListSuccessResponse getUnitList(force)

获取单位列表

    获取单位摘要列表。若为系统管理员，则能获取全部的，否则仅能获取用户所在的

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **force** | **Boolean**| 是否忽略未启用的单位 | [optional] [default to false] |

### Return type

[**GetUnitListSuccessResponse**](../Models/GetUnitListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUnitUserList"></a>
# **getUnitUserList**
> GetUnitUserListSuccessResponse getUnitUserList(unit\_id)

获取单位下用户摘要

    获取单位信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**GetUnitUserListSuccessResponse**](../Models/GetUnitUserListSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="updateUnitConfig"></a>
# **updateUnitConfig**
> UpdateUnitConfigSuccessResponse updateUnitConfig(unit\_id)

更新单位配置

    更新单位配置

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |

### Return type

[**UpdateUnitConfigSuccessResponse**](../Models/UpdateUnitConfigSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="updateUnitInfo"></a>
# **updateUnitInfo**
> UpdateUnitInfoSuccessResponse updateUnitInfo(unit\_id, UpdateUnitInfoBody)

更新单位信息

    更新单位信息

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **unit\_id** | **String**|  | [default to null] |
| **UpdateUnitInfoBody** | [**UpdateUnitInfoBody**](../Models/UpdateUnitInfoBody.md)|  | |

### Return type

[**UpdateUnitInfoSuccessResponse**](../Models/UpdateUnitInfoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

