# UserApi

All URIs are relative to *https://api.klab.ltd*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bindWechatConfirm**](UserApi.md#bindWechatConfirm) | **PATCH** /user/self/wechat | 确认微信账号绑定结果 |
| [**createUser**](UserApi.md#createUser) | **PUT** /user | 创建用户 |
| [**deleteUser**](UserApi.md#deleteUser) | **DELETE** /user/{user_id} | 删除用户 |
| [**generateOTP**](UserApi.md#generateOTP) | **POST** /user/self/otp | Generate Otp |
| [**getPermission**](UserApi.md#getPermission) | **GET** /user/{user_id}/permission | 获取其他用户的权限信息 |
| [**getSelfPermission**](UserApi.md#getSelfPermission) | **GET** /user/self/permission | 获取自己的权限信息 |
| [**getSelfinfo**](UserApi.md#getSelfinfo) | **GET** /user/self/userinfo | 获取自己的用户信息 |
| [**getUserConfig**](UserApi.md#getUserConfig) | **GET** /user/{user_id}/config | 获取用户配置 |
| [**getUserSource**](UserApi.md#getUserSource) | **GET** /user/{user_id}/resource | 获取用户资源 |
| [**getUserinfo**](UserApi.md#getUserinfo) | **GET** /user/{user_id}/userinfo | 获取其他用户信息 |
| [**updatePermission**](UserApi.md#updatePermission) | **PATCH** /user/{user_id}/permission | 更新其他用户的权限 |
| [**updateSelfinfo**](UserApi.md#updateSelfinfo) | **PATCH** /user/self/userinfo | 更新自己的用户信息 |
| [**updateUserConfig**](UserApi.md#updateUserConfig) | **PATCH** /user/{user_id}/config | 更新用户配置 |
| [**updateUserinfo**](UserApi.md#updateUserinfo) | **PATCH** /user/{user_id}/userinfo | 更新其他用户信息 |


<a name="bindWechatConfirm"></a>
# **bindWechatConfirm**
> BindWechatConfirmSuccessResponse bindWechatConfirm(BindWechatConfirmBody)

确认微信账号绑定结果

    确认微信绑定结果结果

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **BindWechatConfirmBody** | [**BindWechatConfirmBody**](../Models/BindWechatConfirmBody.md)|  | |

### Return type

[**BindWechatConfirmSuccessResponse**](../Models/BindWechatConfirmSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createUser"></a>
# **createUser**
> CreateUserSuccessResponse createUser(CreateUserBody)

创建用户

    一般情况下都是组织机构的管理员创建当前单位下的用户，特殊情况会由系统管理员为任何一个单位创建用户，此时需要提供&#x60;unit_id&#x60;参数

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateUserBody** | [**CreateUserBody**](../Models/CreateUserBody.md)|  | |

### Return type

[**CreateUserSuccessResponse**](../Models/CreateUserSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="deleteUser"></a>
# **deleteUser**
> DeleteUserSuccessResponse deleteUser(user\_id)

删除用户

    删除用户，需要当前用户拥有对该用户的访问权限

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**DeleteUserSuccessResponse**](../Models/DeleteUserSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="generateOTP"></a>
# **generateOTP**
> GenerateOTPSuccessResponse generateOTP()

Generate Otp

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenerateOTPSuccessResponse**](../Models/GenerateOTPSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getPermission"></a>
# **getPermission**
> GetPermissionSuccessResponse getPermission(user\_id)

获取其他用户的权限信息

    获取其他用户的权限信息，需要当前用户拥有对该用户的访问权限  - 系统管理员  - 组织机构管理员

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**GetPermissionSuccessResponse**](../Models/GetPermissionSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSelfPermission"></a>
# **getSelfPermission**
> GetSelfPermissionSuccessResponse getSelfPermission()

获取自己的权限信息

    获取自己的权限信息

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSelfPermissionSuccessResponse**](../Models/GetSelfPermissionSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSelfinfo"></a>
# **getSelfinfo**
> GetSelfinfoSuccessResponse getSelfinfo()

获取自己的用户信息

    获取自己的用户信息，无需任何权限

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSelfinfoSuccessResponse**](../Models/GetSelfinfoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUserConfig"></a>
# **getUserConfig**
> GetUserConfigSuccessResponse getUserConfig(user\_id)

获取用户配置

    获取用户配置

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**GetUserConfigSuccessResponse**](../Models/GetUserConfigSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUserSource"></a>
# **getUserSource**
> GetUserSourceSuccessResponse getUserSource(user\_id)

获取用户资源

    获取用户所拥有的资源

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**GetUserSourceSuccessResponse**](../Models/GetUserSourceSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUserinfo"></a>
# **getUserinfo**
> GetUserinfoSuccessResponse getUserinfo(user\_id)

获取其他用户信息

    获取其他用户信息，需要当前用户拥有对该用户的访问权限  - 系统管理员  - 在同一组织机构下

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**GetUserinfoSuccessResponse**](../Models/GetUserinfoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="updatePermission"></a>
# **updatePermission**
> UpdatePermissionSuccessResponse updatePermission(user\_id, UpdatePermissionBody)

更新其他用户的权限

    更新其他用户的权限信息，需要当前用户拥有对该用户的访问权限，并且此次要修改的权限不能超过当前用户的权限  - 系统管理员  - 组织机构管理员

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |
| **UpdatePermissionBody** | [**UpdatePermissionBody**](../Models/UpdatePermissionBody.md)|  | |

### Return type

[**UpdatePermissionSuccessResponse**](../Models/UpdatePermissionSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="updateSelfinfo"></a>
# **updateSelfinfo**
> UpdateSelfinfoSuccessResponse updateSelfinfo()

更新自己的用户信息

    更新自己的用户信息，无需任何权限，能更新的字段仅包括&#x60;username&#x60;、&#x60;nickname&#x60;、&#x60;password&#x60;，留空则表示不更新

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpdateSelfinfoSuccessResponse**](../Models/UpdateSelfinfoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="updateUserConfig"></a>
# **updateUserConfig**
> UpdateUserConfigSuccessResponse updateUserConfig(user\_id)

更新用户配置

    更新用户配置

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |

### Return type

[**UpdateUserConfigSuccessResponse**](../Models/UpdateUserConfigSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="updateUserinfo"></a>
# **updateUserinfo**
> UpdateUserinfoSuccessResponse updateUserinfo(user\_id, UpdateUserinfoBody)

更新其他用户信息

    更新其他用户信息，需要当前用户拥有对该用户的访问权限  - 系统管理员  - 组织机构管理员

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **user\_id** | **String**|  | [default to null] |
| **UpdateUserinfoBody** | [**UpdateUserinfoBody**](../Models/UpdateUserinfoBody.md)|  | |

### Return type

[**UpdateUserinfoSuccessResponse**](../Models/UpdateUserinfoSuccessResponse.md)

### Authorization

[AuthHeader](../README.md#AuthHeader), [SignHeader](../README.md#SignHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

